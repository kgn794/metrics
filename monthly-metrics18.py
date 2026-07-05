import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import plotly.graph_objects as go


def get_release_count():
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Value": [8, 20, 24, 26, 10, 36]
    })
    
    # Statistics
    mean = df["Value"].mean()
    std = df["Value"].std()
    
    upper = mean + std
    lower = mean - std
    goal = 19
    
    # Create figure
    fig = go.Figure()
    
    # Main line
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Value"],
            mode="lines+markers",
            name="Sales",
            line=dict(color="royalblue", width=3)
        )
    )
    
    # Mean baseline
    fig.add_hline(
        y=mean,
        line_dash="dash",
        line_color="green",
        annotation_text=f"Mean = {mean:.2f}",
        annotation_position="top right"
    )
    
    # +1 Std
    fig.add_hline(
        y=upper,
        line_dash="dot",
        line_color="orange",
        annotation_text=f"+1 Std = {upper:.2f}",
        annotation_position="top left"
    )
    
    # -1 Std
    fig.add_hline(
        y=lower,
        line_dash="dot",
        line_color="orange",
        annotation_text=f"-1 Std = {lower:.2f}",
        annotation_position="bottom left"
    )
    
    # Goal
    fig.add_hline(
        y=goal,
        line_color="green",
        line_dash="solid",
        annotation_text=f"<b>Goal = {goal}</b>",
        annotation_position="bottom left",
        annotation_font=dict(
            color="green",
            size=14
        )
    )
    
    fig.update_layout(
        title="Deployment count with Mean and Standard Deviation",
        xaxis_title="Month",
        yaxis_title="Value",
        template="plotly_white",
        height=500
    )
    return fig

release_count = get_release_count()
# Layout
row1 = st.container()
with row1:
    st.plotly_chart(release_count, use_container_width=True)

    
