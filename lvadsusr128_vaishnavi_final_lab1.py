# -*- coding: utf-8 -*-
"""LVADSUSR128_vaishnavi_final_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t3bwsSguSljN45HSBhursfPW3E1QolB5
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score,recall_score

data = pd.read_csv("/content/loan_approval.csv")
df = pd.DataFrame(data)
df.head()

df.info()

df.describe()

df.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(data = df.corr())
plt.show()

from sklearn.preprocessing import LabelEncoder
l= LabelEncoder()

df[' loan_status']=l.fit_transform(df[' loan_status'])
df.head(2)

X = df[[' income_annum',' loan_amount',' commercial_assets_value',' luxury_assets_value',' bank_asset_value']]
y = df[' loan_status']

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size =0.3,random_state=0)

from sklearn.preprocessing import Normalizer
df = Normalizer(x_train)

from sklearn.ensemble import RandomForestClassifier
rfc  = RandomForestClassifier()

rfc.fit(x_train,y_train)
y_pred=rfc.predict(x_test)
accuracy = accuracy_score(y_pred,y_test)
print(accuracy)
f1 = f1_score(y_pred,y_test)
print(f1)

from sklearn.tree import DecisionTreeClassifier
dt  = DecisionTreeClassifier()

dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)
accuracy = accuracy_score(y_pred,y_test)
print(accuracy)
f1 = f1_score(y_pred,y_test)
print(f1)



