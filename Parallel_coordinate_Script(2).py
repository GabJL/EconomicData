"""
Programmers: Zakaria Abdelmoiz Dahi, Gabriel Luque and Enrique Alba
Insitution: Malaga University
About:
    - This code creates the parallel coordinates of two data series: # Employees 3-5, Empployees 1000-4999: non-normalized
    - The results will be two figures for each data series: one non-normalised and the second normalised using min-max technique.
How to:
    - Just execute the script.
"""


from yellowbrick.features import ParallelCoordinates
import sklearn.datasets as sd
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.pyplot as plt

"""
Here I set my new Map using Green, Yellow and Orange colors to indicate the profiles
Note: coding is in RGBA
Green: 0,128,0,1.0
Yelow: 255,255,0,1.0
Orange: 255, 138, 30, 1
"""
vals = [[255/256, 138/256, 30/256, 1],[255/256,251/256,0/256,1.0],[0/256,128/256,0/256,1.0]]
newcmp = ListedColormap(vals)             

# generate random classification data: 3 samples: economic profiles, 30 features: economic data, 3 classes: economic profiles
X, y = sd.make_classification(n_samples=3, n_features=30, n_informative=2, n_redundant=0, n_repeated=0, n_classes=3, n_clusters_per_class=1, weights=None, flip_y=0.01, class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=None);


# Fill up the classification data with the real data
# Employees 3-5
a = [5772.10476190476,	5913.59047619048,	6076.01785714286,	6253.40357142857,	6371.44761904762,	6447.10476190476,	6588.88690476191,	6777.90119047619,	6924.87380952381,	7041.81666666667,	7118.93452380952,	7167.60595238095,	7104.36904761905,	6961.19761904762,	6816.61785714286,	6671.03214285714,	6580.89642857143,	6530.36785714286,	6363.61428571429,	6113.84285714286,	5967.12142857143,	5894.00714285714,	5891.42619047619,	5939.22619047619,	5974.86785714286,	6001.825,	6041.35714285714,	6089.87142857143,	6153.11904761905,	6226.89047619047];
b = [4638.6875,	4744.4375,	4858.64583333333,	4978.89583333333,	5065.89583333333,	5129.14583333333,	5212.375,	5309.875,	5393.52083333333,	5467.27083333333,	5550.35416666667,	5640.10416666667,	5631.27083333333,	5552.02083333333,	5484,	5424,	5372.02083333333,	5325.77083333333,	5271.35416666667,	5211.10416666667,	5067.14583333333,	4863.39583333333,	4765.66666666667,	4743.66666666667,	4753.16666666667,	4785.16666666667,	4845.89583333333,	4927.14583333333,	4943.5,	4913.5];
c = [4300.88888888889,	4419.55555555556,	4570.77222222222,	4745.23888888889,	4846.225,	4894.725,	5000.72222222222,	5147.78888888889,	5273.95277777778,	5385.18611111111,	5459.61111111111,	5507.74444444444,	5472.61666666667,	5378.01666666667,	5259.16944444444,	5123.00277777778,	5046.33611111111,	5012.16944444444,	4865.96388888889,	4639.73055555556,	4500.35555555556,	4423.02222222222,	4404.625,	4428.325,	4453.81388888889,	4480.58055555556,	4516.07777777778,	4557.81111111111,	4600.41944444444,	4643.65277777778];


# Print the centroids' min and maximum values throughout the 30 features.
print(min(a))
print(max(a))
print(min(b))
print(max(b))
print(min(c))
print(max(c))



for i in range(30):
    X[0][i] = a[i];
    X[1][i] = b[i];
    X[2][i] = c[i];


# Specify the features of interest and the classes of the target
features = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
classes = ["Profile 1", "Profile 2", "Profile 3"]


print("Empployees 3-5: non-normalized")
# Instantiate the visualizer with minmax normalisation
visualizer = ParallelCoordinates(classes=classes,vlines=False,colormap = newcmp, features=features)
# Fit and transform the data to the visualizer
visualizer.fit_transform(X, y)
# Finalize the title and axes then display the visualization
visualizer.show()


print("Empployees 3-5: normalized via minmax technique")
# Instantiate the visualizer with minmax normalisation
visualizer = ParallelCoordinates(classes=classes, features=features,vlines=False,colormap = newcmp, normalize = 'minmax')
# Fit and transform the data to the visualizer
visualizer.fit_transform(X, y)
# Finalize the title and axes then display the visualization
visualizer.show()


# Fill up the classification data with the real data
d = [11.3353658536585,	12.2865853658537,	12.9105691056911,	13.3008130081301,	13.7337398373984,	14.1971544715447,	14.5040650406504,	14.6991869918699,	14.9085365853659,	15.1280487804878,	15.4969512195122,	15.9725609756098,	15.8932926829268,	15.4176829268293,	15.0558943089431,	14.775406504065,	14.8434959349593,	15.1605691056911,	15.2286585365854,	15.1189024390244,	14.9095528455285,	14.6290650406504,	14.4908536585366,	14.4542682926829,	14.6880081300813,	15.114837398374,	15.2428861788618,	15.1575203252033,	15.3140243902439,	15.6432926829268];
e = [2.68518518518519,	2.90740740740741,	3.29166666666667,	3.79166666666667,	4.03240740740741,	4.08796296296296,	4.5,	5.16666666666667,	5.60648148148148,	5.88425925925926,	5.93518518518519,	5.82407407407407,	5.64814814814815,	5.42592592592593,	5.2037037037037,	4.98148148148148,	4.9537037037037,	5.06481481481482,	5.0462962962963,	4.93518518518519,	4.85648148148148,	4.80092592592593,	4.97222222222222,	5.30555555555556,	5.47685185185185,	5.53240740740741,	5.49074074074074,	5.37962962962963,	5.59259259259259,	6.03703703703704];
f = [0.791666666666667,	1.29166666666667,	1.64583333333333,	1.89583333333333,	1.85416666666667,	1.60416666666667,	1.5,	1.5,	1.9375,	2.6875,	3.58333333333333,	4.58333333333333,	4.41666666666667,	3.41666666666667,	3,	3,	3,	3,	3.14583333333333,	3.39583333333333,	3.20833333333333,	2.70833333333333,	2.5,	2.5,	2.64583333333333,	2.89583333333333,	3,	3,	3,	3];

# Print the centroids' min and maximum values throughout the 30 features.
print(min(d))
print(max(d))
print(min(e))
print(max(e))
print(min(f))
print(max(f))


for i in range(30):
    X[0][i] = d[i];
    X[1][i] = e[i];
    X[2][i] = f[i];



# Specify the features of interest and the classes of the target
features = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
classes = ["Profile 1", "Profile 2", "Profile 3"]

print("Empployees 1000-4999: non-normalized")
# Instantiate the visualizer with minmax normalisation
visualizer = ParallelCoordinates(classes=classes,vlines=False,colormap = newcmp, features=features)
# Fit and transform the data to the visualizer
visualizer.fit_transform(X, y)
# Finalize the title and axes then display the visualization
visualizer.show()


print("Empployees 1000-4999: normalized via minmax technique")
# Instantiate the visualizer with minmax normalisation
visualizer = ParallelCoordinates(classes=classes, features=features,vlines=False,colormap = newcmp, normalize = 'minmax')
# Fit and transform the data to the visualizer
visualizer.fit_transform(X, y)
# Finalize the title and axes then display the visualization
visualizer.show()
