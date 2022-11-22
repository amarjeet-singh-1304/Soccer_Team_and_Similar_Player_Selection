import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error

import warnings
import wf_ml_evaluation

warnings.filterwarnings("ignore")
evaluation_folder = "evaluation/"
evaluation_file_name = "summary.txt"
model_folder = "models/"


def load_reg_model_and_predict(x_test, y_test):
    model_file_name = "linear_regression_model.sav"
    grid_reg_model = pickle.load(open(model_folder + model_file_name, 'rb'))
    predicted_y = grid_reg_model.predict(x_test)
    wf_ml_evaluation.calculate_and_write_evaluation_metrics("Basic Linear Regression", y_test, predicted_y, "w")


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
    wf_ml_evaluation.linear_reg_with_grid_cv(x_train, y_train, x_test, y_test)
    wf_ml_evaluation.ridge_model_and_predict(x_train, y_train, x_test, y_test)
    wf_ml_evaluation.lasso_model_and_predict(x_train, y_train, x_test, y_test)


if __name__ == '__main__':
    main()

