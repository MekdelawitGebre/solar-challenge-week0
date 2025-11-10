import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# -----------------------------
# Data Loading
# -----------------------------
def load_uploaded_data(uploaded_file):
    """
    Load a CSV uploaded by the user.
    """
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            st.error(f"Error loading CSV: {e}")
            return None
    else:
        st.warning("Please upload a CSV file.")
        return None

# -----------------------------
# GHI Boxplot
# -----------------------------
def plot_ghi_boxplot(df, title="GHI Distribution"):
    """
    Plot a boxplot of GHI values from the dataset.
    """
    if df is None:
        st.warning("No data to plot.")
        return

    if "GHI" not in df.columns:
        st.warning("Column 'GHI' not found in dataset.")
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(y=df["GHI"], ax=ax)
    ax.set_title(title)
    ax.set_ylabel("GHI")
    st.pyplot(fig)

# -----------------------------
# Compare Multiple Countries
# -----------------------------
def compare_countries_barplot(dfs_dict):
    """
    Compare the mean GHI of multiple countries using a barplot.
    
    Parameters:
        dfs_dict: dict
            Dictionary of country names and their corresponding DataFrames.
            Example: {"Benin": df_benin, "Togo": df_togo}
    """
    if not dfs_dict:
        st.warning("No datasets provided for comparison.")
        return

    mean_ghi = {}
    for country, df in dfs_dict.items():
        if df is not None and "GHI" in df.columns:
            mean_ghi[country] = df["GHI"].mean()
        else:
            mean_ghi[country] = 0  # fallback if GHI column missing

    if not mean_ghi:
        st.warning("No valid GHI data found in uploaded files.")
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=list(mean_ghi.keys()), y=list(mean_ghi.values()), ax=ax)
    ax.set_title("Average GHI Comparison")
    ax.set_ylabel("Mean GHI")
    st.pyplot(fig)
