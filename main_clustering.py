# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:38:43 2020
"""

from step1 import clustering_step_1  # import the function performing the first step of clustering
from step2 import clustering_step_2  # import the function performing the second step of clustering
from step3 import clustering_step_3  # import the function performing the third step of clustering

verbose_mode_1 = 0  # step1: 0 do not display anything, 1 for displaying details about the processing
verbose_mode_2 = 0  # step2: 0 do not display anything, 1 for displaying details about the processing
verbos_mode_3 = 0 # step3: 0 do not display anything, 1 for displaying details about the processing


# execute the 1st step of clustering: extract the ideal number of clusters to be used in step 2
# num_elbows = clustering_step_1(verbose_mode_1)
# execute the 2nd step of clustering: extract the ideal number of features to be used in step 3
#num_features = clustering_step_2(num_elbows, verbose_mode_2)


num_elbows = 3
num_features = 4
# lb_distance represents the distance to consider in order to decide if two series are similar
# NB: the distance is set enough large so that all the pairs of series are considered similar and are processed to extract the list of series to be maintained during 4th step.
lb_distance = 1000000 
list_data_series = clustering_step_3(num_elbows,num_features,lb_distance,verbos_mode_3)
