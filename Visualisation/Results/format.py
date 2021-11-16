"""
Programmers: Zakaria Dahi, Enrique Alba and Gabriel Luque.
Institution: Universidad de Malaga, Spain

About: 
    - Calculates the mean of the metrics based on the results obtained in 30 executions (i.e. considering the "resultsoo.xls" files, where x is the ID of the execution).
    - Calculates the ranking of each variant, for each metric and in each cluster (1 means the variant achieved the best results)
    - Computes the number of times a given variant has been the chieving the best result in a given economic data series

The resulting files:
    - "formatted.xls": contains the results of (1)
    - "ranking.xls: contains the results of (2)
    - "score.xls": contains the results of (3)

How to:
    - Make sure that the files containing the results of each execution are located in the same folder as the script.
    - The fildes are named "resultsID.xls" where ID is the rank of the execution from 1 to 30.
    - Run the script.
    
"""
import xlwt
import xlrd
import numpy as np


exe = 30 # number of executions
clust = 10 # number of clusters
ds = 33 # number of data series
met = 4;
"""
write down the results
# create a workbook
"""
wbook_out = xlwt.Workbook()
wbook_rank = xlwt.Workbook()
wbook_score = xlwt.Workbook()
sheet_score = wbook_score.add_sheet("scores")
sheet_score.write(0,0,"Distance-based cGA")
sheet_score.write(1,0,"Opposition-based cGA")
sheet_score.write(2,0,"Mutation-based cGA")
finale_score = np.zeros([3,ds])   
for i in range (ds): # browse data 33 series
    sheet_out = wbook_out.add_sheet(str(i)) 
    sheet_rank = wbook_rank.add_sheet(str(i))
    data_all1 = np.zeros(4);
    data_all2 = np.zeros(4);
    data_all3 = np.zeros(4);    
    score1 = np.zeros([clust,met])
    score2 = np.zeros([clust,met])
    score3 = np.zeros([clust,met])
    sheet_out.write(0,8,'Note:')
    sheet_out.write(1,8, 'Metric 1 : MEAN of sum of the distances between each cluster\'s points and centroids.')
    sheet_out.write(2,8, 'Metric 2 : MEAN of sum of the distances between the fartheset point in each cluster and the cluster\'s centroid.')
    sheet_out.write(3,8, 'Metric 3 : MEAN of sum of the distances between all the clusters\' centroids.')
    sheet_out.write(4,8, 'Metric 4 : MEAN of sum of the distances between each cluster\'s centroid and its nearest point from other clusters.')
    sheet_out.write(0,1,'Results of the cGA with Distance-based mutation')
    sheet_out.write(1,1,'Metric 1')
    sheet_out.write(1,2,'Metric 2')
    sheet_out.write(1,3,'Metric 3') 
    sheet_out.write(1,4,'Metric 4')
    sheet_out.write(19,1,'Results of the cGA with Opposition-based Mutation')
    sheet_out.write(20,1,'Metric 1')
    sheet_out.write(20,2,'Metric 2')
    sheet_out.write(20,3,'Metric 3') 
    sheet_out.write(20,4,'Metric 4')
    sheet_out.write(39,1,'Results of the cGA with Random Mutation')
    sheet_out.write(40,1,'Metric 1')
    sheet_out.write(40,2,'Metric 2')
    sheet_out.write(40,3,'Metric 3') 
    sheet_out.write(40,4,'Metric 4')
    """ 
    write down the ranking
    """
    sheet_rank.write(0,8,'Note:')
    sheet_rank.write(1,8, 'Metric 1 : 1 if the solver is achieving the best results based on the sum of the distances between each cluster\'s points and centroids.')
    sheet_rank.write(2,8, 'Metric 2 : 1 if the solver is achieving the best results based on the sum of the distances between the fartheset point in each cluster and the cluster\'s centroid.')
    sheet_rank.write(3,8, 'Metric 3 : 1 if the solver is achieving the best results based on the sum of the distances between all the clusters\' centroids.')
    sheet_rank.write(4,8, 'Metric 4 : 1 if the solver is achieving the best results based on the sum of the distances between each cluster\'s centroid and its nearest point from other clusters.')
    sheet_rank.write(0,1,'Results of the cGA with Distance-based mutation')
    sheet_rank.write(1,1,'Metric 1')
    sheet_rank.write(1,2,'Metric 2')
    sheet_rank.write(1,3,'Metric 3') 
    sheet_rank.write(1,4,'Metric 4')
    sheet_rank.write(19,1,'Results of the cGA with Opposition-based Mutation')
    sheet_rank.write(20,1,'Metric 1')
    sheet_rank.write(20,2,'Metric 2')
    sheet_rank.write(20,3,'Metric 3') 
    sheet_rank.write(20,4,'Metric 4')
    sheet_rank.write(39,1,'Results of the cGA with Random Mutation')
    sheet_rank.write(40,1,'Metric 1')
    sheet_rank.write(40,2,'Metric 2')
    sheet_rank.write(40,3,'Metric 3') 
    sheet_rank.write(40,4,'Metric 4')
    for j in range (clust): # browse the clusters
        block1 = j +2;
        block2 = j+21
        block3 = j+41
        """
        write down the cluster ID
        """
        clust_num = 'Using ' + str(j+1) + ' cluster(s)'
        sheet_out.write(block1,0,clust_num)
        sheet_out.write(block2,0,clust_num)
        sheet_out.write(block3,0,clust_num)   
        sheet_rank.write(block1,0,clust_num)
        sheet_rank.write(block2,0,clust_num)
        sheet_rank.write(block3,0,clust_num)
        for k in range(1,(exe+1)): # browse the 30 execution files
            """
            Read the data
            """
            name = "results" + str(k) +".xls"
            wbook = xlrd.open_workbook(name) 
            sheet = wbook.sheet_by_index(i)
            data1 = [sheet.cell_value(block1,1),sheet.cell_value(block1,2),sheet.cell_value(block1,3),sheet.cell_value(block1,4)] 
            data_all1 = np.array(data1) + data_all1;
            # cGA opposition-based mutation      
            data2 = [sheet.cell_value(block2,1),sheet.cell_value(block2,2),sheet.cell_value(block2,3),sheet.cell_value(block2,4)] 
            data2 = np.array(data2)
            data_all2 = np.array(data2) + data_all2;
            # cGA random mutation
            data3 = [sheet.cell_value(block3,1),sheet.cell_value(block3,2),sheet.cell_value(block3,3),sheet.cell_value(block3,4)] 
            data3 = np.array(data3)
            data_all3 = np.array(data3) + data_all3;

        """
        Read the data
        """
        data1_mean = data_all1/exe
        data2_mean = data_all2/exe
        data3_mean = data_all3/exe
        for w in range(4):  
            """
            Uncomment if you want to write down the mean values
            """
            sheet_out.write(block1,(w+1),data1_mean[w])
            sheet_out.write(block2,(w+1),data2_mean[w])
            sheet_out.write(block3,(w+1),data3_mean[w])
            ranking = [data1_mean[w],data2_mean[w],data3_mean[w]]
            # affect 1 to the best results
            compare = min(ranking)
            for x in range(3):
                if ranking[x] == compare:
                    if x == 0:
                       score1[j,w] = 1 
                       """
                       Uncomment if you want write down the ranking
                       """
                       sheet_rank.write(block1,(w+1),1)
                    if x == 1:
                       score2[j,w] = 1
                       """
                       Uncomment if you want write down the ranking             
                       """
                       sheet_rank.write(block2,(w+1),1)
                    if x == 2:
                       score3[j,w] = 1  
                       """ 
                       Uncomment if you want to write down the ranks
                       """
                       sheet_rank.write(block3,(w+1),1)

        # save the output
        wbook_out.save("formatted.xls")
        wbook_rank.save("ranking.xls")        
    """
    write down the scores
    """
    score_val1 = np.count_nonzero(score1 == 1)
    score_val2 = np.count_nonzero(score2 == 1)
    score_val3 = np.count_nonzero(score3 == 1)
    sheet_score.write(0,i+1,score_val1) # write the score of distance-based cGA for ith metric
    sheet_score.write(1,i+1,score_val2) # write the score of opposition-based cGA for ith metric
    sheet_score.write(2,i+1,score_val3) # write the score of random-based cGA for ith metric    
    wbook_score.save("scores.xls")
     
