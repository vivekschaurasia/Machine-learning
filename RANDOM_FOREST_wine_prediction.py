# Random Forest Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("winequalityN.csv")
dataset.dropna(axis=0, how='any', thresh=None, subset=['fixed acidity' , 'volatile acidity' ,'citric acid' , 'residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality'], inplace=True)
x = dataset.iloc[: , 1:-1].values
y = dataset.iloc[: , -1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""



# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(x, y)

y_pred = regressor.predict(x_test)

y_pred = np.round(regressor.predict(x_test))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test , y_pred)
