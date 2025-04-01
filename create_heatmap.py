import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
from read_file import read_file

def create_heatmap_age_financil():
    df = read_file("depr_dataset.csv")
    df["Financial Stress"] = pd.to_numeric(df["Financial Stress"], errors="coerce")

    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    correlation_matrix = numeric_df.corr()

    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.2, left=0.15)
    plt.show()

create_heatmap_age_financil()