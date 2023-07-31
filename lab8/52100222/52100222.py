import numpy as np
import pandas as pd
import math
# data = np.loadtxt("sample.txt",delimiter=',')
# print(data)
# data2 = pd.read_csv("sample.txt",delimiter=',')
# print(data2)
# data = pd.read_csv("sample1.txt",delimiter=',')
# print(data)
#ex1
# Require 1
iris = pd.read_csv('iris.csv', delimiter=',')

# Require 2
print(iris.head(5))

# Require 3
all_columns = []

for i in iris:
    if (i != "species"):
        all_columns.append(iris[i])
def imean(data):
    tong = np.sum(data)
    return tong/(len(data))
def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev
res = []

for i in all_columns:
    sub_res = []
    sub_res.append(len(i))
    sub_res.append(imean(i))
    sub_res.append(stdev(i))
    sub_res.append(i.min())
    sub_res.append(i.max())
    res.append(sub_res)

df = pd.DataFrame(np.array(res).T,
                  columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
                  index=['count', 'mean', 'std', 'min', 'max'])

print(df)

# Require 1
population = pd.read_csv('population.csv', delimiter=',')

# Require 2
print(population.head(5))

# Require 3
all_country_name = population.get(["Country Code"]).drop_duplicates()["Country Code"]
res = []
all_mean = []
all_std = []
all_min = []
all_max = []
for i in all_country_name:
    temp = population.loc[population["Country Code"] == i]["Value"]
    all_mean.append(imean(temp))
    all_std.append(stdev(temp))
    all_min.append(temp.min())
    all_max.append(temp.max())

temp = population.get(["Country Name", "Country Code"]).drop_duplicates()
all_country_name = list(temp["Country Name"])
all_country_code = list(temp["Country Code"])

result = pd.DataFrame({'Country Name': all_country_name,
                       'Country Code': all_country_code,
                       'Mean': all_mean,
                       'Std': all_std,
                       'Min': all_min,
                       'Max': all_max
                       })

print(result)
