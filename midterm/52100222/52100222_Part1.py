#mean(data)
from statistics import mean
A = [5,2,6,22,11]
print(mean(A))
#fmean(data)
from statistics import fmean
data= [8,10,20,22]
weight=[0.2,0.3,0.2,0.3]
print(fmean(data,weight))
#geometric_mean(data)
from statistics import geometric_mean
data = [5,22,30,25]
print(geometric_mean(data))
#harmonic_mean(data,weights)
from statistics import harmonic_mean
print(harmonic_mean([60,40],weights=[10,20]))
#median(data)
from statistics import median
A =[1,3,7]
B = [1,4,6,7]
print(median(A))
print(median(B))
#median)low(data)
from statistics import median_low
A =[1,3,7]
B = [1,4,6,7]
print(median_low(A))
print(median_low(B))
#median_high(data)
from statistics import median_high
A =[1,3,7]
B = [1,4,6,7]
print(median_high(A))
print(median_high(B))
#median_grouped
from statistics import median_grouped
set3 = [2, 4, 8, 9, -2, -3, -5, -6]
print(median_grouped(set3))
A = [1,4,5,5,7]
print(median_grouped(A,interval=2))
#median Mode(data)
from statistics import mode
A = [1,2,3,2,2,7,8,4,3] 
print(mode(A))
#Multimode(data)
from statistics import multimode
S = 'aabbbbccddddeeffffgg'
print(multimode(S))
#pstdev(data)
from statistics import pstdev
A = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
print(pstdev(A))
#pvariance(data)
from statistics import pvariance
data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
print(pvariance(data))
#stdev(data)
from statistics import stdev
A = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
print(stdev(A))
#variance(data)
from statistics import variance
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(variance(data))
#quantiles(data)
from statistics import quantiles
data = [105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110,
        100, 75, 105, 103, 109, 76, 119, 99, 91, 103, 129,
        106, 101, 84, 111, 74, 87, 86, 103, 103, 106, 86,
        111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95,
        103, 107, 101, 81, 109, 104]
print([round(q, 1) for q in quantiles(data, n=10)])
#covariance(data1,data2)
from statistics import covariance
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(covariance(x,y))
#correlation(data1,data2)
from statistics import correlation
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(correlation(x, y))
#linear_regression(data1,data2)
from statistics import linear_regression
year = [1971, 1975, 1979, 1982, 1983]
films_total = [1, 2, 3, 4, 5]
slope, intercept = linear_regression(year, films_total)
print(round(slope * 2019 + intercept))