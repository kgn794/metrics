import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st

df = pd.read_excel("Documents/local-metrics.xlsx", sheet_name="Sheet1")

obj_cols = df.select_dtypes(include="object").columns
df[obj_cols] = df[obj_cols].astype(str)

row_index = st.selectbox("Deployment Frequency", df.index)

row = df.iloc[row_index, 1:]

chart_df = pd.DataFrame({
    "Month": cols,
    "Value": row[cols].values
}).set_index("Month")

st.write("Selected Row:")
st.write(row)
st.write(chart_df)

st.bar_chart(chart_df)

