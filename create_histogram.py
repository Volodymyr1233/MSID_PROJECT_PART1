import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
from read_file import read_file

def create_depression():
    df = read_file("depr_dataset.csv")[["Depression"]]

    sns.displot(df, x="Depression")
    plt.show()

def create_work_study():
    df = read_file("depr_dataset.csv")[["Work/Study Hours"]]

    sns.displot(df, x="Work/Study Hours")
    plt.show()

def create_dietary_habbits():
    df = read_file("depr_dataset.csv")[["Dietary Habits"]]

    sns.displot(df, x="Dietary Habits")
    plt.show()
def create_sex():
    df = read_file("depr_dataset.csv")[["Gender"]]

    sns.displot(df, x="Gender")
    plt.show()


create_depression()
create_work_study()
create_dietary_habbits()
create_sex()