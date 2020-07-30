# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:38:43 2020

"""

from step1 import clustering_step_1  # import the function performing the first step of clustering
from step2 import clustering_step_2  # import the function performing the second step of clustering
   

verbose_mode_1 = 0  # step1: 0 do not display anything, 1 for displaying details about the processing
verbose_mode_2 = 1  # step2: 0 do not display anything, 1 for displaying details about the processing

# execute the 1st step of clustering: extract the ideal number of clusters to be used in step 2
# num_elbows = clustering_step_1(verbose_mode_1)
# execute the 2nd step of clustering: extract the ideal number of features to be used in step 3
num_elbows = 3
num_features = clustering_step_2(num_elbows, verbose_mode_2)

