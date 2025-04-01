import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
from read_file import read_file

def create_finStress_acadPress():
    df = read_file("depr_dataset.csv")[["Depression", "Age", "Gender"]]
    # df["Financial Stress"] = pd.to_numeric(df["Financial Stress"], errors="coerce")

    sns.catplot(x="Depression", y="Age", data=df, hue="Gender", kind="violin")

    plt.show()

def create_workHours_CGPA():
    df = read_file("depr_dataset.csv")[["Work/Study Hours", "Academic Pressure", "Gender"]]
    

    sns.catplot(x="Work/Study Hours", y="Academic Pressure", data=df, hue="Gender", kind="violin")

    plt.show()



create_finStress_acadPress()
create_workHours_CGPA()