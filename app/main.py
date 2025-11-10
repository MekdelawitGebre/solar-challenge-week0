import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import load_uploaded_data, plot_ghi_boxplot,compare_countries_barplot




st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("☀ Solar Energy Insights Dashboard")

# -----------------------------
# File uploads
# -----------------------------
st.sidebar.header("Upload Clean CSVs")
benin_file = st.sidebar.file_uploader("Upload Benin CSV", type="csv")
sl_file = st.sidebar.file_uploader("Upload Sierra Leone CSV", type="csv")
togo_file = st.sidebar.file_uploader("Upload Togo CSV", type="csv")

# -----------------------------
# Load data
# -----------------------------
dfs = {}
dfs["Benin"] = load_uploaded_data(benin_file)
dfs["Sierra Leone"] = load_uploaded_data(sl_file)
dfs["Togo"] = load_uploaded_data(togo_file)

# -----------------------------
# Visualizations
# -----------------------------
for country, df in dfs.items():
    if df is not None:
        st.subheader(f"{country} Data Preview")
        st.dataframe(df.head())
        st.subheader(f"{country} GHI Distribution")
        plot_ghi_boxplot(df, title=f"{country} GHI Boxplot")

# -----------------------------
# Comparison chart
# -----------------------------
if all(df is not None for df in dfs.values()):
    st.subheader("Comparison of Average GHI Across Countries")
    compare_countries_barplot(dfs)
