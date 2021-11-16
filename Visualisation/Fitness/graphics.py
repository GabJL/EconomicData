"""
Programmers: Zakaria Dahi, Enrique Alba and Gabriel Luque.
Institution: Universidad de Malaga, Spain

About:
    - This script reads the file "FitnessEvolution.xls" the fitness values obtained by the three cGA variants (distance-based, opposition, random)
    - The "FitnessEvolution.xls" file is the one you obtain when you run the script "statistics.py"
    - It creates a plot of the evolution of the fitness values.

How to:
    - Locate the "FitnessEvolution.xls" in the same folder as the script.
    - Run the script "graphics.py"
"""
import xlrd
import numpy as np
import matplotlib.pyplot as plt


"""
Recover the results stored in "FitnessEvolution.xls"
"""
num_iter = 50 # number of iterations the cGA is supposed to have performed
wbook = xlrd.open_workbook("FitnessEvolution.xls") # specify the excel file to read from it
sheet = wbook.sheet_by_index(0) # specify the sheet to read from it.
iter_val = np.zeros((num_iter,1)) # stocks the ID of iterations
val1_data = np.zeros((num_iter,1))
val2_data = np.zeros((num_iter,1))
val3_data = np.zeros((num_iter,1))
for i in range(num_iter):
    val1_data[i,0] = sheet.cell_value((i+1),0)
    val2_data[i,0] = sheet.cell_value((i+1),1)
    val3_data[i,0] = sheet.cell_value((i+1),2)
    iter_val[i,0] = (i+1)
"""
Plot the results
"""
plt.plot(iter_val,val1_data,'b4-')
plt.plot(iter_val,val2_data,'r.-')
plt.plot(iter_val,val3_data,'g+-')
plt.ylabel("Fitness Value")
plt.xlabel("Number of Iterations")
plt.legend(['Distance-based cGA','Opposition-based cGA','Random-based cGA'])
plt.savefig('plot_fitness.eps', format='eps')
