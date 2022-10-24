import glob
import warnings
import pandas as pd
import hashlib

warnings.filterwarnings("ignore")


def calculate_md5(filename):
    with open(filename, "rb") as f:
        get_bytes = f.read()
        readable_hash = hashlib.md5(get_bytes).hexdigest()


def data_processing():
    original_folder_path = 'data_original/'
    processed_folder_path = 'data_processed/'
    filenames = glob.glob(original_folder_path + "*.csv")
    aggregated_df = pd.DataFrame()
    for file in filenames:
        players_df = pd.read_csv(file)
        calculate_md5(file)
        players_df['year'] = "20" + file[-6:-4]
        aggregated_df = pd.concat([players_df, aggregated_df], axis=0)

    columns_list_tobe_dropped = ['club_logo_url', 'club_flag_url', 'nation_logo_url',
                                 'nation_flag_url', 'player_face_url', 'player_url', 'real_face',
                                 'club_loaned_from', 'nation_position', 'nation_jersey_number', 'long_name',
                                 'nation_team_id', 'player_tags', 'ls', 'st', 'rs', 'lw', 'lf', 'cf', 'rf',
                                 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm',
                                 'rdm', 'rwb', 'lb', 'lcb', 'cb', 'rcb', 'rb']

    # Dropping the unnecessary columns
    aggregated_df = aggregated_df.drop(columns_list_tobe_dropped, axis=1)

    # Checking for missing data
    aggregated_df.isnull().sum()
    aggregated_df.to_csv(processed_folder_path + "merged_removed_columns_data.csv")

    # Filling some missing values
    missing_values_list = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'release_clause_eur',
                           'league_level', 'club_jersey_number']

    for x in missing_values_list:
        aggregated_df[x].fillna(aggregated_df[x].min(), inplace=True)

    column_list = ['physic', 'goalkeeping_speed', 'mentality_composure', 'club_contract_valid_until',
                   'club_team_id', 'value_eur', 'wage_eur']
    for x in column_list:
        aggregated_df[x].fillna(aggregated_df[x].mean(), inplace=True)

    aggregated_df['player_traits'].fillna('No traits available', inplace=True)

    # dropping another rows as there are very less-number of rows having multiple columns with null values
    aggregated_df.dropna(how='any', axis=0, inplace=True)

    # checking for duplicate rows
    aggregated_df[aggregated_df.duplicated(keep='last')]

    aggregated_df.to_csv(processed_folder_path + "processed_data.csv")


if __name__ == '__main__':
    data_processing()
