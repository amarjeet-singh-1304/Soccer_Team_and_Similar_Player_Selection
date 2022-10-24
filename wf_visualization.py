import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings("ignore")


def data_visualization():

    file_folder = "data_processed/"
    visual_folder = "visuals/"
    players_data = pd.read_csv(file_folder + "processed_data.csv")
    summary_file_name = "summary.txt"

    # Computing Quantitative Summary Statistics
    quantitative_stats = players_data.agg(
                                          {"age": ["min", "max", "median"],
                                           "height_cm": ["min", "max", "median"],
                                           "pace": ["min", "max", "median"]
                                           })

    categories = pd.unique(players_data['club_jersey_number'])
    no_of_categories = len(categories)
    most_frequent_club_jersey_no = players_data['club_jersey_number'].value_counts().idxmax()
    least_frequent_club_jersey_no = players_data['club_jersey_number'].value_counts().idxmin()

    categories1 = pd.unique(players_data['nationality_name'])
    no_of_categories1 = len(categories1)
    most_frequent_body_type1 = players_data['nationality_name'].value_counts().idxmax()
    least_frequent_body_type1 = players_data['nationality_name'].value_counts().idxmin()

    with open(file_folder + summary_file_name, "w") as f:
        f.write("Quantitative stats of features: \n")
        quantitative_stats_string = quantitative_stats.to_string(header=True, index=True)
        f.write(quantitative_stats_string)
        f.write("\n\nQualitative features (Club Jersey No stats):")
        f.write("\nNo of Categories: ")
        f.write(str(no_of_categories))
        f.write("\nMost Frequent Club Jersey Number:")
        f.write(most_frequent_club_jersey_no.__str__())
        f.write("\nLeast Frequent Club Jersey Number:")
        f.write(least_frequent_club_jersey_no.__str__())
        f.write("\n\nQualitative features (Country):")
        f.write("\nNo of Categories: ")
        f.write(str(no_of_categories1))
        f.write("\nMost Frequent Country (Means having the most players from that country in our dataset): ")
        f.write(most_frequent_body_type1)
        f.write("\nLeast Frequent Country(Means having the least players from that country in our dataset): ")
        f.write(least_frequent_body_type1)
        f.close()

    # compute pairwise correlation matrix
    correlation_file_name = "correlations.txt"
    players_data_features = pd.DataFrame(players_data, columns=['height_cm', 'age', 'pace'])
    correlation_matrix = players_data_features.corr()
    correlation_matrix1 = correlation_matrix.where(np.tril(np.ones(correlation_matrix.shape)).
                                                   astype(np.bool)).fillna('')

    with open(file_folder + correlation_file_name, "w") as f:
        f.write("Correlation Matrix: \n")
        f.write(correlation_matrix1.to_string(header=True, index=True))
        f.close()

    plt.figure("Age and Height Plot")
    plt.xlabel("Age(in years)")
    plt.ylabel("Height (in cm)")
    plt.scatter(players_data['age'], players_data['height_cm'], c="grey")
    plt.savefig(visual_folder + "age_height.png")


    plt.figure("Age and Pace Plot")
    plt.xlabel("Age(in years)")
    plt.ylabel("Pace (0 -100)")
    plt.scatter(players_data['age'], players_data['pace'], c="grey")
    plt.savefig(visual_folder + "age_pace.png")

    plt.figure("Height and Pace Plot")
    plt.xlabel("Height(in cm)")
    plt.ylabel("Pace (0 -100)")
    plt.scatter(players_data['height_cm'], players_data['pace'], c="grey")
    plt.savefig(visual_folder + "height_pace.png")

    players_data['nationality_id'].hist()
    plt.grid(b=None)
    plt.xlabel("Nationality ID")
    plt.ylabel("count")
    plt.savefig(visual_folder + "nation_id_hist.png")

    players_data['club_jersey_number'].hist()
    plt.grid(b=None)
    plt.xlabel("Club Jersey Number")
    plt.ylabel("count")
    plt.savefig(visual_folder + "club_jersey_no_hist.png")


if __name__ == '__main__':
    data_visualization()
