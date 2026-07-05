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

values = df.loc[0, cols].astype(float)
std = values.std()
var = values.var()

fig, ax = plt.subplots()

sb.lineplot(
    data=df,
    x="Month",
    y="Deployment Frequency",
    marker="o",
    ax=ax
)

stats_text = f"Std Dev: {std:.2f} | Variance: {var:.2f}"
ax.text(
    0.5, 1.05,
    stats_text,
    transform=ax.transAxes,
    ha="center",
    fontsize=12,
    fontweight="bold"
)

ax.set_title("Monthly Trend with Statistics")
st.pyplot(fig)
