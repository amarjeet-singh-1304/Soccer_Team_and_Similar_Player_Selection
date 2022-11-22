import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
import warnings
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
import wf_ml_prediction
import wf_ml_training


warnings.filterwarnings("ignore")
evaluation_folder = "evaluation/"
evaluation_file_name = "summary.txt"
model_folder = "models/"

feature_cols = ['potential', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic',
                'attacking_crossing', 'attacking_finishing',
                'attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys', 'skill_dribbling',
                'skill_curve',
                'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control', 'movement_acceleration',
                'movement_sprint_speed',
                'movement_agility', 'movement_reactions', 'movement_balance', 'power_shot_power', 'power_jumping',
                'power_stamina',
                'power_strength', 'power_long_shots', 'mentality_aggression', 'mentality_interceptions',
                'mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure',
                'defending_marking_awareness',
                'defending_standing_tackle', 'defending_sliding_tackle', 'goalkeeping_diving',
                'goalkeeping_handling', 'goalkeeping_kicking',
                'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed', 'preferred_foot',
                'weak_foot',
                'age', 'height_cm', 'weight_kg', 'year']


def experimentation():
    model_file_name = "linear_regression_model.sav"
    reg_model = pickle.load(open(model_folder + model_file_name, 'rb'))
    processed_folder_path = 'data_processed/'
    x_sample = pd.read_csv(processed_folder_path + "sample.csv")
    predicted_y = reg_model.predict(x_sample[feature_cols])
    print(predicted_y)


def calculate_and_write_evaluation_metrics(model_name, y_test, y_predicted, mode):
    mean_avg_perentage_error = mean_absolute_percentage_error(y_test, y_predicted)
    root_mean_square_error = np.sqrt(mean_squared_error(y_test, y_predicted))
    with open(evaluation_folder + evaluation_file_name, mode) as f:
        f.write(model_name + " metrics results:")
        f.write(("\nMean Average Percentage Error: " + str(mean_avg_perentage_error)))
        f.write("\nRoot Mean Square Error: " + str(root_mean_square_error))
        f.close()


def linear_reg_with_grid_cv(x_train, y_train, x_test, y_test):
    linear_model = LinearRegression()
    parameters = {'fit_intercept': [True, False], 'normalize': [True, False], 'copy_X': [True, False]}
    grid = GridSearchCV(linear_model, parameters, cv=5)
    grid.fit(x_train, y_train)
    # below 2 lines are saving models into the model folder
    filename = 'grid_cv_regression_model.sav'
    pickle.dump(grid, open(model_folder + filename, 'wb'))
    #  Uncomment below to load directly from model folder and comment above ones
    # grid = pickle.load(open(model_folder + filename, 'rb'))
    y_pred = grid.predict(x_test)
    calculate_and_write_evaluation_metrics("\n\nGrid Search CV with Linear Regression", y_test, y_pred, "a")


def lasso_model_and_predict(x_train, y_train, x_test, y_test):
    lasso_model = Lasso(alpha=0.001, random_state=10, max_iter=10000, normalize=True)
    lasso_model.fit(x_train, y_train)
    # below 2 lines are saving models into the model folder
    filename = 'lasso_regression_model.sav'
    pickle.dump(lasso_model, open(model_folder + filename, 'wb'))
    #  Uncomment below to load directly from model folder and comment above ones
    # lasso_model = pickle.load(open(model_folder + filename, 'rb'))
    y_pred = lasso_model.predict(x_test)
    calculate_and_write_evaluation_metrics("\n\nLasso Regression", y_test, y_pred, "a")


def ridge_model_and_predict(x_train, y_train, x_test, y_test):
    ridge_reg_model = Ridge(alpha=0.001, random_state=10, max_iter=10000, normalize=True)
    parameters = {'fit_intercept': [True, False], 'normalize': [True, False], 'copy_X': [True, False]}
    grid_ridge_reg_model = GridSearchCV(ridge_reg_model, parameters, cv=2)
    grid_ridge_reg_model.fit(x_train, y_train)
    # below 2 lines are saving models into the model folder
    filename = 'ridge_regression_model.sav'
    pickle.dump(grid_ridge_reg_model, open(model_folder + filename, 'wb'))
    #  Uncomment below to load directly from model folder and comment above ones
    # grid_ridge_reg_model = pickle.load(open(model_folder + filename, 'rb'))
    y_pred = grid_ridge_reg_model.predict(x_test)
    calculate_and_write_evaluation_metrics("\n\nRidge Regression", y_test, y_pred, "a")


def standardize(df):
    scaler = StandardScaler()
    data_std = scaler.fit_transform(df)
    normalized_df = pd.DataFrame(data_std, columns=df.columns, index=df.index)
    return normalized_df


def split_data():
    processed_folder_path = 'data_processed/'
    filename = processed_folder_path + "processed_data.csv"
    df = pd.read_csv(filename)

    encoding = {"preferred_foot": {"Left": 1, "Right": 0}}
    df.replace(encoding, inplace=True)

    x = df[feature_cols]
    y = df['overall']

    x1 = standardize(x)
    x_train, x_test, y_train, y_test = train_test_split(x1, y, random_state=20, train_size=.80)

    x_train.to_csv(processed_folder_path + "x_train.csv")
    x_test.to_csv(processed_folder_path + "x_test.csv")
    y_train.to_csv(processed_folder_path + "y_train.csv")
    y_test.to_csv(processed_folder_path + "y_test.csv")


def main():
    split_data()


if __name__ == '__main__':
    main()
    wf_ml_training.main()
    wf_ml_prediction.main()
