import pickle
import random
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

def calculateBias(y_actual, y_pred):
    return np.mean(y_actual - y_pred)

def calculateVariance(y_actual, y_pred):
    return np.mean(((y_pred - y_actual) - np.mean(y_pred - y_actual)) ** 2)


def calculateMSE(y_actual, y_pred):
    return np.mean((y_actual - y_pred) ** 2)

def main():
    with open('data.pickle', 'rb') as file:
        loaded_data = pickle.load(file)

    random.shuffle(loaded_data['train'])

    subset_size = len(loaded_data['train']) // 15

    training_datasets = [loaded_data['train'][i:i+subset_size] for i in range(0, len(loaded_data['train']), subset_size)]

    test  = loaded_data['test']
    X_test = test[:, 0].reshape(-1, 1)
    y_test = test[:, 1]

    bias = []
    variance = []
    MSE = []
    Irreducible = []
    X = []
    y = []

    for i in range(len(training_datasets)):
        X.append(training_datasets[i][:, 0].reshape(-1, 1))
        y.append(training_datasets[i][:, 1])



    for degree in range(1,11):
        tempB = []
        tempV = []
        tempM = []
        for i in range(len(training_datasets)):

            model = LinearRegression()

            poly_features = PolynomialFeatures(degree=degree)
            X_poly = poly_features.fit_transform(X[i])
            X_poly_test = poly_features.transform(X_test)

            model.fit(X_poly, y[i])
            y_pred = model.predict(X_poly_test)

            bias_value = calculateBias(y_test,y_pred)
            tempB.append(bias_value**2)

            # print(np.var(y_pred - y_test))
            variance_value = calculateVariance(y_test,y_pred)
            # print(variance_value)
            tempV.append(variance_value)
            tempM.append(calculateMSE(y_test,y_pred))
            

        bias.append(np.mean(tempB))
        variance.append(np.mean(tempV))
        MSE.append(np.mean(tempM))
        Irreducible.append(MSE[degree - 1] - bias[degree - 1] - variance[degree - 1])

    # print(bias)
    # print(variance)
    # print(MSE)
    # print(Irreducible)

    degrees = list(range(1, 11))
    plt.figure(figsize=(20, 12))

    plt.plot(degrees, MSE, label='MSE', marker='o')
    plt.plot(degrees, Irreducible, label='Irreducible Error', marker='o')
    plt.plot(degrees, bias, label='Bias^2', marker='o')
    plt.plot(degrees, variance, label='Variance', marker='o')

    plt.title('Bias-Variance Trade-off with Polynomial Degree')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()