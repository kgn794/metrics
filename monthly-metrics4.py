import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import plotly.graph_objects as go

# Sample data
df = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Sales": [100, 120, 150, 130, 170, 160, 180]
})

# Statistics
mean = df["Sales"].mean()
std = df["Sales"].std()

upper = mean + std
lower = mean - std

# Create figure
fig = go.Figure()

# Main line
fig.add_trace(
    go.Scatter(
        x=df["Day"],
        y=df["Sales"],
        mode="lines+markers",
        name="Sales",
        line=dict(color="royalblue", width=3)
    )
)

# Mean baseline
fig.add_hline(
    y=mean,
    line_dash="solid",
    line_color="green",
    annotation_text=f"Mean = {mean:.2f}",
    annotation_position="top left"
)

# +1 Std
fig.add_hline(
    y=upper,
    line_dash="dash",
    line_color="orange",
    annotation_text=f"+1 Std = {upper:.2f}",
    annotation_position="top left"
)

# -1 Std
fig.add_hline(
    y=lower,
    line_dash="dash",
    line_color="orange",
    annotation_text=f"-1 Std = {lower:.2f}",
    annotation_position="bottom left"
)

fig.update_layout(
    title="Sales Trend with Mean and Standard Deviation",
    xaxis_title="Day",
    yaxis_title="Sales",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)
ax.set_title("Monthly Trend with Statistics")
