import streamlit as st
import pandas as pd
from app.utils import load_country_data, plot_ghi_boxplot, top_region_table

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")

st.title("Solar Energy Insights Dashboard")

# Sidebar
st.sidebar.header("Filters")
country = st.sidebar.selectbox(
    "Select Country",
    ["Benin", "Sierra Leone", "Togo"]
)

# Load data dynamically
df = load_country_data(country)

st.write(f"###  Selected Country: **{country}**")
st.dataframe(df.head())

# Visualizations
st.write("### ☀GHI Distribution Comparison")
plot_ghi_boxplot(df)

# Top regions table
st.write("###  Top 5 Regions by Solar Potential (GHI)")
st.table(top_region_table(df))
