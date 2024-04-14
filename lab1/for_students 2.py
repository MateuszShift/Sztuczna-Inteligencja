import numpy as np
import matplotlib.pyplot as plt

from data import get_data, inspect_data, split_data

data = get_data()
inspect_data(data)

train_data, test_data = split_data(data)

# Simple Linear Regression
# predict MPG (y, dependent variable) using Weight (x, independent variable) using closed-form solution
# y = theta_0 + theta_1 * x - we want to find theta_0 and theta_1 parameters that minimize the prediction error

# We can calculate the error using MSE metric:
# MSE = SUM (from i=1 to n) (actual_output - predicted_output) ** 2

# get the columns
y_train = train_data['MPG'].to_numpy() #dana wyjsciowa
x_train = train_data['Weight'].to_numpy() #dana wejsciowa

y_test = test_data['MPG'].to_numpy()
x_test = test_data['Weight'].to_numpy()

# TODO: calculate closed-form solution

wynikowa = np.ones((x_train.shape[0],2)) #bierzemy wiersze
wynikowa[:,1] = x_train  #tworzenie macierzy 1 i wejsciowej
wynikowa_T = wynikowa.T
theta_final = np.dot(np.dot(np.linalg.inv(np.dot(wynikowa_T,wynikowa)),wynikowa_T),y_train) #obliczona theta closed form solution 1.13


theta_best = [0, 0]

# TODO: calculate error


theta_test = np.ones((x_test.shape[0],2)) #bierzemy wiersze
theta_test[:,1] = x_test  #tworzenie macierzy 1 i wejsciowej

mse_error = np.mean((np.square(np.dot(theta_test,theta_final)-y_test))) #error z 1.3 instrukcja
print(mse_error)



# plot the regression line
x = np.linspace(min(x_test), max(x_test), 100)
y = float(theta_final[0]) + float(theta_final[1]) * x
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()

# TODO: standardization

standar_x_train = (x_train - np.mean(x_train))/np.std(x_train)
standar_y_train = (y_train - np.mean(y_train))/np.std(y_train)
standar_x_test = (x_test - np.mean(x_train))/np.std(x_train)
standar_y_test = (y_test - np.mean(y_train))/np.std(y_train)


# TODO: calculate theta using Batch Gradient Descent

plottedTheta = []

def gradient_descent(alpha, x, y, numIterations): 
    m = x.shape[0]
    th = np.zeros(2)
    x_transpose = x.transpose()
    for iter in range(0, numIterations):
        tmp = x.dot(th) - y
        gradient = 2 / m * (x_transpose.dot(tmp))       
        th = th - alpha * gradient
        pred = np.std(y) * np.dot(x,th) + np.mean(y)
        err = np.mean((np.square(pred-y)))
        plottedTheta.append(err)
        #print(plottedTheta[iter])
    return th
 

alpha = 0.01
temp = np.ones((standar_x_train.shape[0],2))
temp[:,1] = standar_x_train

theta_g = gradient_descent(alpha, temp, standar_y_train, 1000) # do gradienta dane train standarized
temp = np.ones((standar_x_test.shape[0],2))
temp[:,1] = standar_x_test

prediction= np.std(y_train) * np.dot(temp,theta_g) + np.mean(y_train) #deviation*dane_standaryzowane + średnia


#plt.plot(plottedTheta)




# TODO: calculate error

mse_error_standarized = np.mean((np.square(prediction-y_test))) #error z 1.3 instrukcja
print(mse_error_standarized)

# plot the regression line
x = np.linspace(min(standar_x_test), max(standar_x_test), 100) 
y = float(theta_g[0]) + float(theta_g[1]) * x
plt.plot(x, y)
plt.scatter(standar_x_test, standar_y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()

plt.plot(plottedTheta)
plt.show()