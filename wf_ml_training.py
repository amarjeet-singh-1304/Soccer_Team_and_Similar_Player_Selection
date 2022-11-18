import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings
import pickle

warnings.filterwarnings("ignore")


def create_model(x_train, y_train):
    model_folder = "models/"
    linear_reg_model = LinearRegression()
    x_train = x_train.iloc[:, 1:]
    linear_reg_model.fit(x_train, y_train['overall'])
    filename = 'finalized_model.sav'
    pickle.dump(linear_reg_model, open(model_folder + filename, 'wb'))


if __name__ == '__main__':
    processed_folder_path = 'data_processed/'
    x_train = pd.read_csv(processed_folder_path + "x_train.csv")
    y_train = pd.read_csv(processed_folder_path + "y_train.csv")
    x_test = pd.read_csv(processed_folder_path + "x_test.csv")

    create_model(x_train, y_train)
