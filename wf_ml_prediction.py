import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
import warnings

warnings.filterwarnings("ignore")
evaluation_folder = "evaluation/"
evaluation_file_name = "summary.txt"


def linear_reg_with_grid_cv(x_train, y_train, x_test, y_test):
    linear_model = LinearRegression()
    parameters = {'fit_intercept': [True, False], 'normalize': [True, False], 'copy_X': [True, False]}
    grid = GridSearchCV(linear_model, parameters, cv=5)
    grid.fit(x_train, y_train)
    y_pred = grid.predict(x_test)
    with open(evaluation_folder + evaluation_file_name, "a") as f:
        f.write("\n\nGrid Search CV with Linear Regression metrics results:")
        f.write(("\nMean Average Percentage Error: " + str(mean_absolute_percentage_error(y_test, y_pred))))
        f.write("\nRoot Mean Square Error:, " + str(np.sqrt(mean_squared_error(y_test, y_pred))))
        f.close()


def lasso_model_and_predict(x_train, y_train, x_test, y_test):
    lasso_model = Lasso(alpha=0.001, random_state=10, max_iter=10000, normalize=True)
    lasso_model.fit(x_train, y_train)
    y_pred = lasso_model.predict(x_test)
    with open(evaluation_folder + evaluation_file_name, "a") as f:
        f.write("\n\nLasso Regression metrics results:")
        f.write(("\nMean Average Percentage Error: " + str(mean_absolute_percentage_error(y_test, y_pred))))
        f.write("\nRoot Mean Square Error:, " + str(np.sqrt(mean_squared_error(y_test, y_pred))))
        f.close()


def ridge_model_and_predict(x_train, y_train, x_test, y_test):
    ridge_reg_model = Ridge(alpha=0.001, random_state=10, max_iter=10000, normalize=True)
    parameters = {'fit_intercept': [True, False], 'normalize': [True, False], 'copy_X': [True, False]}
    grid_ridge_reg_model = GridSearchCV(ridge_reg_model, parameters, cv=2)
    grid_ridge_reg_model.fit(x_train, y_train)
    y_pred = grid_ridge_reg_model.predict(x_test)
    with open(evaluation_folder + evaluation_file_name, "a") as f:
        f.write("\n\nRidge Regression metrics results:")
        f.write(("\nMean Average Percentage Error: " + str(mean_absolute_percentage_error(y_test, y_pred))))
        f.write("\nRoot Mean Square Error:, " + str(np.sqrt(mean_squared_error(y_test, y_pred))))
        f.close()


def load_reg_model_and_predict(x_test, y_test):
    model_folder = "models/"
    model_file_name = "finalized_model.sav"
    grid_reg_model = pickle.load(open(model_folder + model_file_name, 'rb'))
    predicted_y = grid_reg_model.predict(x_test)
    with open(evaluation_folder + evaluation_file_name, "w") as f:
        f.write("Simple Linear Regression metrics results:")
        f.write(("\nMean Average Percentage Error: " + str(mean_absolute_percentage_error(y_test, predicted_y))))
        f.write("\nRoot Mean Square Error:, " + str(np.sqrt(mean_squared_error(y_test, predicted_y))))
        f.close()


def main():
    data_processed_folder = "data_processed/"
    x_train_filename = "x_train.csv"
    y_train_filename = "y_train.csv"
    x_test_filename = "x_test.csv"
    y_test_filename = "y_test.csv"
    x_train = pd.read_csv(data_processed_folder + x_train_filename)
    y_train = pd.read_csv(data_processed_folder + y_train_filename)
    x_test = pd.read_csv(data_processed_folder + x_test_filename)
    y_test = pd.read_csv(data_processed_folder + y_test_filename)
    x_test = x_test.iloc[:, 1:]
    x_train = x_train.iloc[:, 1:]
    y_train = y_train['overall']
    y_test = y_test['overall']
    load_reg_model_and_predict(x_test, y_test)
    linear_reg_with_grid_cv(x_train, y_train, x_test, y_test)
    ridge_model_and_predict(x_train, y_train, x_test, y_test)
    lasso_model_and_predict(x_train, y_train, x_test, y_test)


if __name__ == '__main__':
    main()


