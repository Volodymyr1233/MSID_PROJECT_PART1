import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
from read_file import read_file

def create_depression_press_work():
    df = read_file("depr_dataset.csv")[["Work Pressure", "Job Satisfaction"]]


    sns.lmplot(x="Work Pressure", y="Job Satisfaction", data=df)
    plt.show()

def create_depression_finance():
    df = read_file("depr_dataset.csv")[["Financial Stress", "Depression"]]
    df["Financial Stress"] = pd.to_numeric(df["Financial Stress"], errors="coerce")


    sns.lmplot(x="Financial Stress", y="Depression", data=df)
    plt.show()

def create_depression_academic():
    df = read_file("depr_dataset.csv")[["Work/Study Hours", "Study Satisfaction"]]


    sns.lmplot(x="Work/Study Hours", y="Study Satisfaction", data=df)
    plt.show()




create_depression_finance()
create_depression_press_work()
create_depression_academic()