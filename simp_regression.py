# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:39:36 2019

@author: vhs
"""

#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the dataset
datset = pd.read_csv('Salary_Data.csv')
x = datset.iloc[:,:-1].values
y = datset.iloc[:,-1].values

#splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state =0)

#fitting linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#predicting the test set results
y_pred = regressor.predict(x_test)

#visualizing the training set results
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color ='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of experirnce')
plt.ylabel('Salary')
plt.show()

#visualizing the test set results
plt.scatter(x_test, y_test, color = 'yellow')
#plt.scatter(x_test,y_pred, color = 'orange')
plt.plot(x_train, regressor.predict(x_train),color = 'blue')
plt.title('Salary vs Experirence (test set)')
plt.xlabel('Years of experirnce')
plt.ylabel('Salary')
plt.show()