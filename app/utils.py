import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def load_country_data(country):
    file_map = {
        "Benin": "data/benin_clean.csv",
        "Sierra Leone": "data/sierra_leone_clean.csv",
        "Togo": "data/togo_clean.csv"
    }
    return pd.read_csv(file_map[country])


def plot_ghi_boxplot(df):
    fig, ax = plt.subplots()
    ax.boxplot(df["GHI"])
    ax.set_title("GHI Distribution")
    ax.set_ylabel("GHI Value")
    st.pyplot(fig)


def top_region_table(df):
    return df.groupby("Region")["GHI"].mean().sort_values(ascending=False).head(5).reset_index()
