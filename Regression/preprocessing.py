import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

horario1 = pd.read_csv("https://raw.githubusercontent.com/jorgelgf/ML/master/exemplos/horario002.csv") 
horario2 = pd.read_csv("https://raw.githubusercontent.com/jorgelgf/ML/master/exemplos/horario003.csv") 

horario1.head()

horario2.head()

# Separando os dados para a variável independente e para variável dependete 
X1 = horario1.iloc[:,: -1].values
Y1 = horario1.iloc[:, 1].values

X2 = horario2.iloc[:,: -1].values
Y2 = horario2.iloc[:, 1].values

print(X2)

horario1.describe()

horario2.describe()

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X1, Y1)

# Make predictions using the testing set
Y_pred = regr.predict(X2)

# The coefficients
print('Coefficients: \n', regr.coef_)

print(Y_pred)

# Plot outputs
plt.scatter(X2, Y2,  color='black')
plt.scatter(X2, Y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()


