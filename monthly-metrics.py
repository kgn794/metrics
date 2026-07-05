import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st

df = pd.read_excel("Documents/local-metrics.xlsx", sheet_name="Sheet1")

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Deployment Frequency": [8, 20, 24, 26, 10, 36]
})

fig, ax = plt.subplots()

sb.lineplot(
    data=df,
    x="Month",
    y="Deployment Frequency",
    marker="o",
    ax=ax
)
st.pyplot(fig)
