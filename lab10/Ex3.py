import matplotlib.pyplot as plt
import numpy as np
import random
import math
import pandas as pd
def line(a,b,str):
    plt.plot(b,a,marker ='x')
    plt.title(str,color = 'r')
    plt.xlabel('year')
    plt.ylabel('yield')
    plt.show()
    return 0
read_file = pd.read_csv('company-sales_data.csv',delimiter=',')
all_columns = []
a = read_file.toothpaste
b = read_file.shampoo
c = read_file.facecream
d = read_file.month_number
line(a,d,'toothpaste')
line(b,d,'shampoo')
line(c,d,'facecream')
