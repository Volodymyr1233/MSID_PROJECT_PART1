import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
from read_file import read_file

def create_depression():
    df = read_file("depr_dataset.csv")[["Depression", "Financial Stress"]]

    df["Financial Stress"] = pd.to_numeric(df["Financial Stress"], errors="coerce")


    sns.displot(df, x="Financial Stress", hue="Depression",  multiple="stack")
    plt.show()

def create_work_hours():
    df = read_file("depr_dataset.csv")[["Work/Study Hours", "Have you ever had suicidal thoughts ?"]]


    sns.displot(df, x="Work/Study Hours", hue="Have you ever had suicidal thoughts ?", multiple="stack")
    plt.show()



create_depression()
create_work_hours()