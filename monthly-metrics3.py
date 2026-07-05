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

std = df["Deployment Frequency"].std()
mean = df["Deployment Frequency"].mean()

ax = sb.lineplot(data=df, x="Month", y="Deployment Frequency", marker="o")

ax.axhline(mean, color="green", linestyle="-", label="Mean")

ax.axhline(mean + std, color="orange", linestyle="--", label="+1 Std")
ax.axhline(mean - std, color="orange", linestyle="--", label="-1 Std")

ax.legend()
plt.show()

ax.set_title("Monthly Trend with Statistics")
