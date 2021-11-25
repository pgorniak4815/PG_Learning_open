"""
Case Study from "Using Python for Research" course.

Analyze a dataset consisting of an assortment of wines
classified as "high quality" and "low quality" and
use the k-Nearest Neighbors classifier to determine
whether or not other information about the wine helps
correctly predict whether a new wine will be of high quality.
"""

import pandas as pd
import numpy as np
import random
import sklearn.preprocessing
import sklearn.decomposition
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import scipy.stats as ss
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages


def distance(p1, p2):
    """Find the distance between points p1 and p2"""
    return np.sqrt(np.sum(np.power(p2-p1, 2)))


def accuracy(predictions, outcomes):
    """
    Finds the percent of predictions that equal outcomes.
    """
    return 100*np.mean(predictions == outcomes)


def majority_vote(votes):
    """
    Return the most common element in votes.
    """
    mode, count = ss.mstats.mode(votes)
    return mode


def find_nearest_neighbors(p, points, k=5):
    """
    Find the k nearest neighbors of point
    p and return their indices
    """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


def knn_predict(p, points, outcomes, k=5):
    """
    Predict point value based on nearest neighbors vote
    """
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])


data = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2018+type@asset+block@wine.csv")

numeric_data = data.drop("color", axis=1)
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns=numeric_data.columns)

pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)
principal_components = pca.fit(numeric_data).transform(numeric_data)

observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:, 0]
y = principal_components[:, 1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha=0.2, c=data['high_quality'], cmap=observation_colormap, edgecolors='none')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)
print("Build-in predictor accuracy = " + str(accuracy(library_predictions, data["high_quality"])))


n_rows = data.shape[0]

random.seed(123)
selection = random.sample(range(n_rows), 10)

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = np.array([knn_predict(p, predictors[training_indices, :], outcomes, 5) for p in predictors[selection]])
percentage = accuracy(np.transpose(my_predictions), np.array(data.high_quality[selection]))
print("Homemade predictor accuracy = " + str(percentage))

plt.show()
