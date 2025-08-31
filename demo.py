#coding=utf-8

import pandas as pd
import numpy as np

df = pd.DataFrame({'a':['a','b', 'c'],'b':[3,4,5]})
print(pd.get_dummies(df))

df = pd.read_csv('.\data\202508261937\202508261937_gh_v1.csv')
df.head()

