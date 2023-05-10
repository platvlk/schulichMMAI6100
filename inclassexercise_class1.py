import numpy as np
from scipy import stats

data = np.array([45, 55, 60, 50, 80, 62, 54, 58, 71, 48])

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)[0][0]

print("Mean: {:.2f}".format(mean))
print("Median: {:.2f}".format(median))
print("Mode: {}".format(mode))

variance = np.var(data)
std_deviation = np.std(data)

print("Variance: {:.2f}".format(variance))
print("Standard deviation: {:.2f}".format(std_deviation))

skewness = stats.skew(data)

print("Skewness: {:.2f}".format(skewness))

kurtosis = stats.kurtosis(data)

print("Kurtosis: {:.2f}".format(kurtosis))
