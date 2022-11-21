import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
import wf_ml_prediction
import wf_ml_training

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
    model_folder = "models/"
    model_file_name = "finalized_model.sav"
    reg_model = pickle.load(open(model_folder + model_file_name, 'rb'))
    processed_folder_path = 'data_processed/'
    x_sample = pd.read_csv(processed_folder_path + "sample.csv")
    predicted_y = reg_model.predict(x_sample[feature_cols])
    print(predicted_y)


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
