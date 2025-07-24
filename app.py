# app.py
import streamlit as st
import plotly.express as px
import pandas as pd

# Load the PCA-clustered dataset
df = pd.read_csv("df_pca_4_test_scaled_4.csv")

# Define a manual color mapping for clusters
cluster_color_map = {
    '0': '#1f77b4',  # Blue
    '1': '#ff7f0e',  # Orange
    '2': '#2ca02c',  # Green
    '3': '#d62728'   # Red
}

# Ensure 'Cluster' is string
df_pca_4_test_scaled_4['Cluster'] = df_pca_4_test_scaled_4['Cluster'].astype(str)

fig = px.scatter_3d(
    df_pca_4_test_scaled_4,
    x='PC1', y='PC2', z='PC3',
    color='Cluster',
    color_discrete_map=cluster_color_map,
    size='PC4_scaled',
    opacity=0.7,
    title='PCA 3D Clusters on Test Data'
)

# Streamlit app layout
st.title("Interactive 3D PCA Clustering View")
st.plotly_chart(fig, use_container_width=True)
