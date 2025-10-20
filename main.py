# Main Script for Task 1 Preprocessing

import pandas as pd
from src.data_cleaning import cleaned_data
from src.encoading_scaling import encoaded_scaled_data
from src.outlier_detection import detected_removed_outliers
from src.visuals import save_outlier_pltb_boxplot, saved_correlation_heatmap

def run_pipeline():
    df = pd.read_csv("Data/titanic-Dataset.csv")
    df = cleaned_data(df)
    save_outlier_pltb_boxplot(df, 'Fare')

    df = encoaded_scaled_data(df)
    df = detected_removed_outliers(df, columns=['Fare', 'Age'])
    saved_correlation_heatmap(df)

    df.to_csv("outputs/cleaned_titanic.csv", index=False)
    print("Data preprocessing completed and saved to cleaned_titanic.csv, Check out there!")

if __name__ == "__main__":
    run_pipeline()