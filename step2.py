# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:53:37 2020

"""


# Used to connect and query the database
import sqlite3
# libs for array use, plots, etc.
import numpy as np
# lib containing the predefined K-MEANS in python
from sklearn.cluster import KMeans
# lib used to generate the possible permutation of N digits
from itertools import permutations 
# lib to compute some statistics
import statistics as st

def clustering_step_2(clust_num,verb):
    print("***********************************************************************************************")
    print("                      THE PROCESSING OF THE SECOND STEP OF CLUSTERING HAS STARTED")  
    print("***********************************************************************************************")  
    features_number = []; # stores the number of features to be used in step 3
    # connect to the database
    conn = sqlite3.connect('db-reduced.db')
    c = conn.cursor()
    # extract the series of info
    series = c.execute('SELECT DISTINCT serie_name FROM data')
    data_ser = series.fetchall()
    # extract the locations
    locations = c.execute('SELECT DISTINCT location_name FROM data')
    data_loc = locations.fetchall()
    # define the number of months considered in each clustering
    months_considered = [0, 2, 3, 4, 6 , 12] # 0 is for a clustering considering all the months (not mean of 12 months)
    # display some information about the final data displayed
    if verb == 1:
        print("***********************************************************************************************")
        print("IMPORTANT:")
        print("  - The data displayed at the end of step II is a 1x33 array.")
        print("  - Each value in the array corresponds to the ideal number of months to consider for the clustering of each series of information.")
        print("  - The index of the value corresponds to the index of the serie of information to be used with.")
        print("  - If a given value is Y months, then 15 x Y features will be considered in the clustering.")  
        print("  - Technically speaking, 15 x 1 features will be considered since we will take the mean of Y months in each of the 15 years.")  
        print("***********************************************************************************************")  

    # ============================================== PERFORM CLUSTERING ACCORDING TO 6 CONFIGURATIONS ============================================================
    i = 0; # index to count down the series having been processed ("i" will be only used for displaying information)
    for tuple1 in data_ser: # browse series
        i = i + 1; # increment the idex of the serie each time one is browsed
        cluster_labels = np.zeros(52) # will store the number of the cluster to whome each city belongs
        if verb == 1:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Information n° %i being processed: " % i, tuple1[0])
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        for ind in months_considered: # browse the number of months considered:2, 3, 4, 6 and 12     
            if ind == 0: # 0 means that we perform a clustering using 15 x 12 features 
                data_all_months = np.zeros(180) # stores the data of 15 years x 12 months
            else: # if != 0, it means that we perform a clustering using 15 x "Y" features 
                data_x_months = np.zeros(15*ind) # stores the data of 15 years x 1 value  (The mean of "Y" months)
            for tuple2 in data_loc: # browse locations
                # print(tuple2[0]) # uncomment to know which city you are browsing
                # ====== RETRIEVE THE RECORDS OF THE GIVEN SERIE FOR THE PROCESSED CITY  ================================================
                if ind == 0: # 0 means that we perform a clustering using 15 x 12 features
                    records = c.execute('SELECT * FROM data WHERE serie_name = ? AND location_name =  ? ',(tuple1[0][:],tuple2[0][:]))
                    data_rec = records.fetchall()              
                    data_mat = [];  # the matrice that will contain the records of a city for a given serie, year and period
                    for tuple3 in data_rec:
                        # print(tuple3) # uncomment to know the tuple of info being displayed
                        data_mat = np.append(data_mat,tuple3[5]) # append the records
                    # ===== build-up the matrix of records that will undergo clustering, lines: cities, columns: records of the cities (180 = 15 years x 12 months) =========
                    data_all_months = np.vstack((data_all_months,data_mat)) 
                else: # if != 0, it means that we perform a clustering using 15 x 1 features where the value is the mean of "Y" months
                    records = c.execute('SELECT * FROM data WHERE serie_name = ? AND location_name =  ?  AND period < ?',(tuple1[0][:],tuple2[0][:],ind))     
                    data_rec = records.fetchall()              
                    data_mat = [];  # the matrice that will contain the records of a city for a given serie, year and period
                    for tuple3 in data_rec:
                        # print(tuple3) # uncomment to know the tuple of info being displayed
                        data_mat = np.append(data_mat,tuple3[5]) # append the records
                    # ===== build-up the matrix of records that will undergo clustering, lines: cities, columns: records of the cities (180:15 years x12 months) =========
                    data_x_months = np.vstack((data_x_months,data_mat)) 
            # ====================== PERFORM THE K-MEANS CLUSTERING ========================
            if ind == 0: # 0 means that we perform a clustering using 15 x 12 features
                data_all_months = np.delete(data_all_months, 0, 0)     # delete the first row of unuseful zeros (see above)
                # print(len(data_all_months[0])) # uncomment to check the number of records
                # print(len(data_all_months))  # uncomment to check the number of cities
                # ============= PERFORM K-MEANS CLUSTERING USING K CENTROIDS FOUND IN STEP I ===================================
                # perform the K-means clustering: info about parameters can be found in https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
                clust = KMeans(n_clusters=clust_num, init= 'k-means++',  n_init=10, max_iter=300, tol=0.0001, verbose=0,random_state=None,copy_x=True, algorithm='auto').fit(data_all_months)
                # print(clust.labels_) # uncomment to observe the labels of the clusters to which belong each city
                # print(clust.inertia_) # uncomment to observe the value of dispertion: sum of squared distances between each city and nearest centroid
            else: # if != 0, it means that we perform a clustering using 15 x 1 features where the value is the mean of "Y" months
                data_x_months = np.delete(data_x_months, 0, 0)     # delete the first row of unuseful zeros (see above)                             
                data_x_months_processed = np.zeros(15); # stores 15 x 1 value (where the value is the mean of "Y" months we consider)
                # convert every "Y" months value into one value (the mean of "Y" months) 
                for index_i in range(0, len(data_x_months)):
                    data_mat_process = [];
                    for index in range (0, len(data_x_months[0]), ind):
                        data_mat_process = np.append(data_mat_process,st.mean(data_x_months[index_i][index:index + ind]))
                    data_x_months_processed =  np.vstack((data_x_months_processed,data_mat_process))
                # delete the unuseful line of zeros
                data_x_months_processed = np.delete(data_x_months_processed,0,0)
                # print(len(data_x_months_processed)) # uncomment to check the number of cities
                # print(len(data_x_months_processed[0])) # uncomment to check the number of records
                # ============= PERFORM K-MEANS CLUSTERING USING K CENTROIDS FOUND IN STEP I ===================================
                # perform the K-means clustering: info about parameters can be found in https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
                clust = KMeans(n_clusters=clust_num, init= 'k-means++',  n_init=10, max_iter=300, tol=0.0001, verbose=0,random_state=None,copy_x=True, algorithm='auto').fit(data_x_months_processed)
                #print(clust.labels_) # uncomment to observe the labels of the clusters to which belong each city
                # print(clust.inertia_) # uncomment to observe the value of dispertion: sum of squared distances between each city and nearest centroid
            cluster_labels = np.vstack((cluster_labels,clust.labels_)) # append the result of the clustering using "Y" months
        cluster_labels = np.delete(cluster_labels,0,0) # delete the unuseful set of zeros at the begining 
        # print(len(cluster_labels)) # uncomment to know the number of feature configurations considered
        # print(len(cluster_labels[0])) # uncomment to know the number of cities considered
        #print(cluster_labels) # uncomment to print the result of clustering in each of the 6 feature configurations
        
        # ============================================== COMPUTE DISTANCE BETWEEN CLUSTERING USING 15x12 FEATURES CONFIGURATIONS AND 15 x 1 FEATURES ============================================================
        distance_clustering = []; # will contain the distances between the clustering using 180 features and the clusterings using 15 features only
        # create the N! permutations. Each permutation will be constitued of "X" pairs of clusters (Ai, Bi)
        # Ai: clusters obtained by performing clustering using 180 features
        # Bi: clusters obtained by performing clustering using 15 x 1 features (value =  mean of Y months that have been considered)
        index_cluster_all = [] # stored the Ai: will contain the index of the clusters of the clustering using 180 features to create later the permutations    
        for ind_clust_label in range (0,clust_num): # create an index of clusters of the clustering with 180 features. Will be used to create the permutations
            index_cluster_all = np.append(index_cluster_all,ind_clust_label)  
        # compute the distance between the clustering using 180 features (index 0) and the remaining clusterings using X months
        for ind_config in range (1,len(months_considered)): 
            distance = 1000000000000000000000000000 # initialise the distance enough big to ensure that later it get replaced with the first distance computed
            perm = permutations(index_cluster_all) # stores the Bi that will be used to create the pairs of clusters in each permutation
            for perm_comb in perm: # browse the permutations
                distance_perm = 0 # initialise the cumulative distance of a given permutation
                for ind_pair in range (0,len(perm_comb)): # browse each pair of clusters in the processed permutation
                     distance_pair = 0 # initialise the distance between the cluster of a given pair in a given permutation
                     # extract the number of cities in the union of clusters of the processed pair 
                     union = np.count_nonzero(cluster_labels[0][:] == index_cluster_all[ind_pair]) + np.count_nonzero(cluster_labels[ind_config][:] == perm_comb[ind_pair]) 
                     # extract the number of cities common between the clusters of the processed pair
                     intersec = len(np.intersect1d(np.where(cluster_labels[0][:] == index_cluster_all[ind_pair])[0], np.where(cluster_labels[ind_config][:] == perm_comb[ind_pair])[0]))
                     # compute the distance between the clusters of the processed pair in the processed permutation
                     distance_pair = union - intersec
                     # sum-up the distances of all the pairs of clusters in the processed permutation
                     distance_perm = distance_perm +  distance_pair
                # save the smallest cummulative distance among all the permutations
                if distance_perm < distance:
                    distance = distance_perm
            # display the distance between the clustering using 180 features and the one using 15 features considering "Y" months
            if verb == 1:
                print("The distance between a clustering with 180 features and the one with 15 features considering ", months_considered[ind_config], "months) is:", distance)
            # append the distance between the clustering of 180 features and the processed clustering with 15 features considering "Y" months 
            distance_clustering = np.append(distance_clustering,distance)       
        # NB: since we aim at minimising the # of features and the distance between the clutsering using 180 features and the one using 15 features considering "Y" months, we will select the clustering minimising the followig objective function: f(x) = # features + distance
        dist_feat = (np.array(months_considered[1:]) * 15) + distance_clustering
        index_best_num_feat = np.where(dist_feat == np.min(dist_feat))[0] + 1
        features_number = np.append(features_number, months_considered[index_best_num_feat[0]])
   
    if verb == 1:
        print("***********************************************************************************************")
        print("Ideal # of months to to be used for the clustering:", features_number)  
        print("***********************************************************************************************")
    
    print("***********************************************************************************************")
    print("                      THE PROCESSING OF THE SECOND STEP OF CLUSTERING HAS FINISHED")  
    print("***********************************************************************************************")
    return(features_number)