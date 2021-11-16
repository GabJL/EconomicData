"""
Programmers: Zakaria Abdelmoiz Dahi, Enrique Alba and Gabriel Luque
Insitution: Malaga University
About:
    - This code creates a map of the obtained profiling (see Table 2 in the paper.)
    - The results are stored in the file "profiles.xlsx" of this folder.
How to:
    - Look at the list of profiled data series.
    - Select 2 IDs from the list below (you cans elect more, but need to add a call to map the data series).
    - Specify it in the main (see method at the end of the script).
    - Execute the script and you will get "N" eps figures containing the map of the profiles.
"""
"""
About the Spanish map used:
    - The shape file of Spain has been downloaded from : https://www.statsilk.com/maps/download-free-shapefile-maps
    - NB: Another intresting source to explore in HuMove: http://centrodedescargas.cnig.es/CentroDescargas/index.jsp
"""
import geopandas as gpd
import xlrd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# Define the mapping function

def plotting_function(id):
    wbook = xlrd.open_workbook("Profiling.xlsx")
    sheet = wbook.sheet_by_index(0)
    ad = [1,2,3,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31]
    ds_id = id
    ds_id_sheet = 0
    for i in range(1,(len(ad)+1)):
        if (int(sheet.cell_value(0,i)) == ds_id):
            ds_id_sheet = i
            break;
    
    geo_data_spain =  gpd.read_file('gadm36_ESP_2.shp')
    city_name = geo_data_spain['NAME_2'] # stores the spanish city name according to https://www.statsilk.com/maps/download-free-shapefile-maps
    
    for i in range (52):
        city = sheet.cell_value((i+1),0)
        for j in range(len(city_name)):
            if city_name[j] == city:
                geo_data_spain['NL_NAME_2'][j] = int(sheet.cell_value((i+1),ds_id_sheet)) # browse the cities
    
    """
    Here I set my new Map using Green, Yellow and Orange colors to indicate the profiles
    Note: coding is in RGBA
    Green: 0,128,0,1.0
    Yelow: 255,255,0,1.0
    Orange: 255, 138, 30, 1
    """
    vals = [[255/256, 138/256, 30/256, 1],[255/256,255/256,0/256,1.0],[0/256,128/256,0/256,1.0]]
    newcmp = ListedColormap(vals)             
    ax = geo_data_spain.plot('NL_NAME_2', cmap = newcmp, linewidth = 0.5, edgecolor='k')
    ax.set_axis_off() # delete surrounding axes: I do not like them
    name_fig = "series_num_" + str(id) + ".eps" 
    plt.savefig(name_fig, format='eps')



def main():
    plotting_function(23)
    plotting_function(31)
    
if __name__ == "__main__":
    main()
    
    
"""
HELP: 
    
Choose the data series you wanna display graphically:
Available profiled data series are : 1	2	3	5	6	8	9	10	11	12	13	14	15	16	17	18	19	20	21	23	24	25	26	27	28	29	30	31
Below are the exaplantions of the each data series, where the row number corrsponds to the ID:
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
"""
     Note: there are mismatch between the INE data and the one in https://www.statsilk.com/maps/download-free-shapefile-maps:
     Action : I corrected them in profile.xlsx so they match
         Alicante/Alacant
        Murcia
        Araba/Álava
        Murcia
        Bizkaia
        Murcia
        Castellón/Castelló
        Murcia
        Gipuzkoa
        Murcia
        Illes Balears
        Murcia
        Valencia/València
        Murcia
"""