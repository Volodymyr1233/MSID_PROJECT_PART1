import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
from read_file import read_file

def create_Habits_Age():
    df = read_file("depr_dataset.csv")[["Dietary Habits", "Age", "Gender"]]

    sns.boxplot(x="Dietary Habits", y="Age", data=df, hue="Gender")

    plt.show()

def create_Gender_CGPA():
    df = read_file("depr_dataset.csv")[["Work/Study Hours", "Study Satisfaction", "Gender"]]
    sns.boxplot(x="Work/Study Hours", y="Study Satisfaction", data=df, hue="Gender")
   
    plt.show()


create_Habits_Age()
create_Gender_CGPA()