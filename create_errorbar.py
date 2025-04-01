import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
from read_file import read_file

def plot_errors_work_study():
    df = read_file("depr_dataset.csv")[["Work/Study Hours"]]

    f, axs = plt.subplots(2, figsize=(7, 2), sharex=True, layout="tight")


    sns.pointplot(data=df, x="Work/Study Hours", capsize=.3, errorbar="sd", ax=axs[0])
    sns.stripplot(data=df, x="Work/Study Hours", jitter=.3, ax=axs[1])
    
    plt.show()

def plot_errors_academic_pressure():
    df = read_file("depr_dataset.csv")[["Academic Pressure"]]

    f, axs = plt.subplots(2, figsize=(7, 2), sharex=True, layout="tight")


    sns.pointplot(data=df, x="Academic Pressure", capsize=.3, errorbar="sd", ax=axs[0])
    sns.stripplot(data=df, x="Academic Pressure", jitter=.3, ax=axs[1])
    
    plt.show()
def plot_errors_financial_stress():
    df = read_file("depr_dataset.csv")[["Financial Stress"]]
    df["Financial Stress"] = pd.to_numeric(df["Financial Stress"], errors="coerce")

    f, axs = plt.subplots(2, figsize=(7, 2), sharex=True, layout="tight")


    sns.pointplot(data=df, x="Financial Stress", capsize=.3, errorbar="sd", ax=axs[0])
    sns.stripplot(data=df, x="Financial Stress", jitter=.3, ax=axs[1])
    
    plt.show()

plot_errors_work_study()
plot_errors_academic_pressure()
plot_errors_financial_stress()