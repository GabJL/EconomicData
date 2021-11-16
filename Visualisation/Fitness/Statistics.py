# -*- coding: utf-8 -*-
"""
Programmers: Zakaria Dahi, Enrique Alba and Gabriel Luque.
Institution: Universidad de Malaga, Spain

About:
    - This script runs the three variants of the DcGA (distance-based, opposition-based and random)
    - It writes down the results on the "FitnessEvolution.xls" file.
    - The results consist of the fitness values obtained throught N iterations you specify in the main method.

How to: 
    - Just run the script.
"""

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

# Used to connect and query the database
import sqlite3
# libs for array use, plots, etc.
import numpy as np
# the cGA producing initial centroids
from cGA1 import cGA1 # distance-based cGA 
from cGA2 import cGA2 # opposition-based cGA
from cGA3 import cGA3 # random mutation
# writing the results
import xlwt
from xlwt import Workbook

        
def statistics(verb,pop,it,pc,pm,NN,D,ds_id,cn):
    print("***********************************************************************************************")
    print("                      THE PROCESSING OF THE CGA HAS STARTED")
    print("***********************************************************************************************")
    # connect to the database
    conn = sqlite3.connect('db-reduced.db')
    c = conn.cursor()
    # extract the series of info
    series = c.execute('SELECT DISTINCT serie_name FROM data')
    data_ser = series.fetchall()
    # extract the locations
    locations = c.execute('SELECT DISTINCT location_name FROM data')
    data_loc = locations.fetchall()
    # ============================================== EXTRACT THE 33 SERIES =============================================
    i = 0  # index to count down the series having been processed
    # create an excel file
    wbook = Workbook(); 
    for tuple in [ds_id]: 
        tuple1 = data_ser[tuple]
        i = i + 1  # increment the idex of the serie each time one is browsed
        data_all = np.zeros(180)  # just used because vstack needs not null matrix
        if verb == 1:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Information n° %i being processed: " % i, tuple1[0])  # uncomment to know which serie you are browsing
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        for tuple2 in data_loc:
            # ====== RETRIEVE ALL THE RECORDS (15x12) OF THE GIVEN SERIE FOR THE PROCESSED CITY  =======================
            records = c.execute('SELECT * FROM data WHERE serie_name = ? AND location_name =  ? ',
                                (tuple1[0][:], tuple2[0][:]))
            data_rec = records.fetchall()
            data_mat = []  # the matrix that will contain the records of a city for a given serie, year and period
            for tuple3 in data_rec:
                data_mat = np.append(data_mat, tuple3[5])  # append the records
            # ===== build-up the matrix of records that will undergo clustering, lines: cities, columns: records of
            # the cities (180:15 years x12 months) =========
            data_all = np.vstack((data_all, data_mat))
        data_all = np.delete(data_all, 0, 0)  # delete the first row of unuseful zeros (see above)
        # ============= PERFORM K-MEANS CLUSTERING USING 1 .. 10 CENTROIDS =============================================
        dim = len(data_all[:,0]) # extract the number of cities = size of te GA's individual
        # serie_name = 'Note: The results contained in this sheet are of the data series: ' +str(tuple1[0]); # convert the series name into string
        for centro in [cn]: # select the number of clusters 
            centro_modif  = centro - 1 # small modification because the cGA code increments the cluster number by 1
            # compute the clustering metrics obtained by the cGA
            results1 = cGA1(pop,dim,it,pc,pm,data_all,centro_modif,NN,D) # distance-based cGA
            results2 = cGA2(pop,dim,it,pc,pm,data_all,centro_modif,NN,D) # opposition-based cGA
            results3 = cGA3(pop,dim,it,pc,pm,data_all,centro_modif,NN,D) # Random-based cGA
        # Write down the results on excel files
        sheet = wbook.add_sheet("FitnessEvolution")
        sheet.write(0,8,"Note(1): Each row represents the best fitness obtained in a given iteration")
        sheet.write(1,8,"Note(2): The 1st, 2nd and 3rd columns represent the distance, opposition and random-based cGAs' results")
        details = "Note(3): we use metric 1," + str(cn) + " cluster(s), data series:" + str(tuple1[0][:]) 
        sheet.write(2,8,details)
        sheet.write(0,0,"Distance-based")
        sheet.write(0,1,"Opposition-based")
        sheet.write(0,2,"Random-based") 
        for i in range (it):
            sheet.write((i+1),0,results1[i,0]) # write down the results of Distance-based cGAs
            sheet.write((i+1),1,results2[i,0]) # write down the results of Opposition-based cGAs
            sheet.write((i+1),2,results3[i,0]) # write down the results of Random-based cGAs
        wbook.save("FitnessEvolution.xls")
    print("***********************************************************************************************")
    print("                      THE PROCESSING OF THE cCGA HAS FINISHED")
    print("***********************************************************************************************")
    return 0;

def main():
    """
    Parameter of the cGA: 
    """
    
    it = 50; # number of iterations # use 500 for optimal results
    N = 40; # number of rows in the grid
    D = 10; # number of cols in the grid
    pop = D*N; #size of the population
    pc = 0.5; # crossover probability
    pm = 0.2; # mutation probability
    
    """
    parameters of the visualisation
    """
    """
     Select one of the data series to visualise:
    "Men Activity Percentage"
    "Women Activity Percentage"
    "Men Unemployment Percentage"
    "Women Unemployment  Percentage"
    "Men Employment Percentage"
    "Women Employment  Percentage"
    "Women Unemployment Percentage"
    "Men employment Percentage"
    "Women employment Percentage"
    "Índice general. Variación mensual."
    "Alimentos y bebidas no alcohólicas. Índice."
    "Bebidas alcohólicas y tabaco. Índice."
    "Vestido y calzado. Índice."
    "Sanidad. Índice."
    "Transporte. Índice."
    "Comunicaciones. Índice."
    "Ocio y cultura. Índice."
    "Enseñanza. Índice."
    "Restaurantes y hoteles. Índice."
    "Otros bienes y servicios. Índice."
    "Sin asalariados. Total de empresas. Total CNAE. Empresas."
    "De 1 a 2. Total de empresas. Total CNAE. Empresas."
    "De 3 a 5. Total de empresas. Total CNAE. Empresas."
    "De 6 a 9. Total de empresas. Total CNAE. Empresas."
    "De 10 a 19. Total de empresas. Total CNAE. Empresas."
    "De 20 a 49. Total de empresas. Total CNAE. Empresas."
    "De 50 a 99. Total de empresas. Total CNAE. Empresas."
    "De 100 a 199. Total de empresas. Total CNAE. Empresas."
    "De 200 a 499. Total de empresas. Total CNAE. Empresas."
    "De 500 a 999. Total de empresas. Total CNAE. Empresas."
    "De 1000 a 4999. Total de empresas. Total CNAE. Empresas."
    "De 5000 o más asalariados. Total de empresas. Total CNAE. Empresas."
    "Total. Total de empresas. Total CNAE. Empresas."
    """
    
    ds_id =2; # the id of the data series you want to visualise
    cn = 6; # number of profiles you want to create
    verbose_mode = 1  # controls the display on the command line
    statistics(verbose_mode,pop,it,pc,pm,N,D,ds_id,cn) # executes the code line
    
if __name__ == "__main__":
     main()