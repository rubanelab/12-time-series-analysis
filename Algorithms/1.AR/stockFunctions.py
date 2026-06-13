import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

def conversion(y_train, stk_data):
    actual_y_train = pd.DataFrame(index = range(len(y_train)), columns = stk_data.columns)
    for i in range(len(y_train)):
        actual_y_train.iloc[i] = y_train[i]
        
    return actual_y_train

def graph(actual, predicted, act_label, pred_label, title, x_label, y_label):
    plt.figure(figsize=(10,5))
    plt.plot(actual, color = 'blue', label=act_label)
    plt.plot(predicted, color = 'green', label =pred_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()
    
def rmsemape(y_test, y_pred):
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mape = mean_absolute_percentage_error(y_test, y_pred)
    
    print("RMSE-Testset:", rmse)
    print("maPe-Testset:", mape)

def conversion_single(y_train, stk_data):
    actual_y_train = pd.DataFrame(index = range(len(y_train)), columns = stk_data)
    for i in range(len(y_train)):
        actual_y_train.iloc[i] = y_train[i]
        
    return actual_y_train
















    