# -*- coding: utf-8 -*-
"""advertising"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = r"D:\Users\703143501\Documents\Genpact Internal\Advertising.csv"
data = pd.read_csv(file)

# renaming a column header
data.rename(columns = {'Unnamed: 0':'idx', 'TV': 'Television'}, inplace = True)

# assigning an existing column value as index
data.set_index('idx', inplace = True)

fields = data.columns

# creating a new column with header total, and assigning it some value
data['total'] = np.NaN

for each in fields[:-1]:
    data['total'] += data[each]

sep = "_"
suffix = sep + "percentage"
old_cols = list(data.columns[:-2])
percentages = list(map(lambda x: x + suffix, old_cols))


for each in percentages:
    data[each] = data[each.split(sep)[0]] / data['total'] * 100


data['total %'] = 0
for each in percentages:
    data['total %'] += data[each]  


# drop columns by name
cols_to_drop = percentages
data.drop(labels = cols_to_drop, axis = 1, inplace = True)

# drop columns by index
cols = list(range(-1, -3, -1))
data.drop(data.columns[cols],axis=1,inplace=True)

#path_to_copy = r"D:\Users\703143501\Desktop\new.xlsx"
#data.to_excel(path_to_copy)
