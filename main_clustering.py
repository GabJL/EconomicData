# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:03:32 2020

"""

from step1 import clustering_step_1  # import the function performing the first step of clustering
from step2 import clustering_step_2  # import the function performing the second step of clustering
from step3 import clustering_step_3  # import the function performing the third step of clustering
from step4 import clustering_step_4  # import the function performing the fourth step of clustering

verbose_mode_1 = 0  # step1: 0 do not display anything, 1 for displaying details about the processing
verbose_mode_2 = 0  # step2: 0 do not display anything, 1 for displaying details about the processing
verbose_mode_3 = 0  # step3: 0 do not display anything, 1 for displaying details about the processing
verbose_mode_4 = 1  # step4: 0 do not display anything, 1 for displaying details about the processing


# execute the 1st step of clustering: extract the ideal number of clusters to be used in step 2
# num_elbows = clustering_step_1(verbose_mode_1)
# execute the 2nd step of clustering: extract the ideal number of features to be used in step 3
# num_features = clustering_step_2(num_elbows, verbose_mode_2)


num_elbows = 3
num_features = 4
# lb_distance: the distance to consider in order to decide if two series are similar 
# =========================================================================
# NB: the distance is set enough large so that all 
# the pairs of series are considered similar and are 
# processed to extract the list of series to be maintained during 4th step.
# ========================================================================
lb_distance = 26  # 25% (52*0.25*2) of the locations can be classified in different cluster
list_data_series = clustering_step_3(num_elbows, num_features, lb_distance, verbose_mode_3)
# execute the 4th step of clustering: perform the final step
clust = clustering_step_4(num_elbows, num_features, list_data_series, verbose_mode_4)