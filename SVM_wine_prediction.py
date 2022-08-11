import pandas as pd

dataset = pd.read_csv("winequalityN.csv")
dataset.dropna(axis=0, how='any', thresh=None, subset=['fixed acidity' , 'volatile acidity' ,'citric acid' , 'residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality'], inplace=True)
x = dataset.iloc[: , 1:-1].values
y = dataset.iloc[: , -1].values

import numpy as np

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)



from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.2)

from sklearn.svm import SVR
regresion = SVR(kernel = 'rbf')
regresion.fit(x_train , y_train)

y_pred = np.round(regresion.predict(x_test))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test , y_pred)