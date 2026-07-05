import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st

df = pd.read_excel("Documents/local-metrics.xlsx", sheet_name="Sheet1")

row_index = st.selectbox("Deployment Frequency", df.index)

row = df.iloc[row_index, 1:]

st.write("Selected Row:")
st.write(row)

st.line_chart(row)
