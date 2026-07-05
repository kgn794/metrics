import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import plotly.graph_objects as go


df_rel_count = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Value": [8, 20, 24, 26, 10, 36]
    })

df_sit_count = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Value": [0, 0, 0, 0, 0, 0]
    })

df_inc_count = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Value": [30, 28, 33, 38, 3, 73]
    })

def get_release_count():
    df = df_rel_count
    
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
        annotation_text=f"<b>Average Count = {mean:.2f}</b>",
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
        annotation_position="bottom right",
        annotation_font=dict(
            color="green",
            size=14
        )
    )
    
    fig.update_layout(
        title="Release Count",
        xaxis_title="Month",
        yaxis_title="Value",
        template="plotly_white",
        height=500
    )
    return fig

def get_sit_bug_count():
    df = df_sit_count
    
    # Statistics
    mean = df["Value"].mean()
    std = df["Value"].std()
    
    upper = mean + std
    lower = mean - std
    goal = 0
    
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
        annotation_text=f"<b>Average Count = {mean:.2f}</b>",
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
        annotation_position="bottom right",
        annotation_font=dict(
            color="green",
            size=14
        )
    )
    
    fig.update_layout(
        title="SIT Bug Count",
        xaxis_title="Month",
        yaxis_title="Value",
        template="plotly_white",
        height=500
    )
    return fig

def get_inc_count():
    df = df_sit_count
    
    # Statistics
    mean = df["Value"].mean()
    std = df["Value"].std()
    
    upper = mean + std
    lower = mean - std
    goal = 21
    
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
        annotation_text=f"<b>Average Count = {mean:.2f}</b>",
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
        annotation_position="bottom right",
        annotation_font=dict(
            color="green",
            size=14
        )
    )
    
    fig.update_layout(
        title="Incident Count",
        xaxis_title="Month",
        yaxis_title="Value",
        template="plotly_white",
        height=500
    )
    return fig
    
rel_cnt = get_release_count()
sit_cnt = get_sit_bug_count()
inc_cnt = get_inc_count()

# Layout
row1 = st.container()
with row1:
        col1, col2 = st.columns(2)
        with col1:
                st.plotly_chart(rel_cnt, use_container_width=True)
        with col2:
                st.plotly_chart(sit_cnt, use_container_width=True)
row2 = st.container()
with row2:
        col1, col2 = st.columns(2)
        with col1:
                st.plotly_chart(inc_cnt, use_container_width=True)
    

    
