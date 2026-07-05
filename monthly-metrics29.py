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

df_story_points = pd.DataFrame({
    "Sprint": ["173", "174", "176", "177", "178", "179", "181", "182", "183", "185"],
    "Committed": [33, 57, 44, 66, 70, 58, 71, 51, 74, 59],
    "Delivered": [25, 16, 7, 24, 42, 40, 70, 34, 61, 18]
})

def get_release_count():
    df = df_rel_count
    
    # Statistics
    mean = df["Value"].mean()
    std = df["Value"].std()
    
    upper = mean + std
    lower = mean - std
    goal = 19
    mean_color = "green" if mean >= goal else "red"
    # Create figure
    fig = go.Figure()
    
    # Main line
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Value"],
            mode="lines+markers",
            name="Value",
            line=dict(color="royalblue", width=3)
        )
    )
    
    # Mean baseline
    fig.add_hline(
        y=mean,
        line_dash="dash",
        line_color=mean_color,
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
    mean_color = "green" if mean <= goal else "red"
    # Create figure
    fig = go.Figure()
    
    # Main line
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Value"],
            mode="lines+markers",
            name="Value",
            line=dict(color="royalblue", width=3)
        )
    )
    
    # Mean baseline
    fig.add_hline(
        y=mean,
        line_dash="dash",
        line_color=mean_color,
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
    df = df_inc_count
    
    # Statistics
    mean = df["Value"].mean()
    std = df["Value"].std()
    
    upper = mean + std
    lower = mean - std
    goal = 21
    mean_color = "green" if mean <= goal else "red"
    
    # Create figure
    fig = go.Figure()
    
    # Main line
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Value"],
            mode="lines+markers",
            name="Value",
            line=dict(color="royalblue", width=3)
        )
    )
    
    # Mean baseline
    fig.add_hline(
        y=mean,
        line_dash="dash",
        line_color= mean_color,
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
        xaxis_title="Sprint",
        yaxis_title="Committed & Delivered",
        template="plotly_white",
        height=500
    )
    return fig

def get_story_points():
    df = df_story_points
        
    # Statistics
    mean = df["Delivered"].mean()
    std = df["Delivered"].std()
    
    upper = mean + std
    lower = mean - std
    goal = 48
    mean_color = "green" if mean >= goal else "red"
    # Create figure
    fig = go.Figure()
    
    # Main line
    fig.add_trace(
        go.Scatter(
            x=df["Sprint"],
            y=df["Committed"],
            mode="lines+markers",
            name="Committed SP",
            line=dict(color="royalblue", width=3)
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df["Sprint"],
            y=df["Delivered"],
            mode="lines+markers",
            name="Delivered SP",
            line=dict(color="green", width=3)
        )
    )
    
    # Mean baseline
    fig.add_hline(
        y=mean,
        line_dash="dash",
        line_color=mean_color,
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
        title="Committed and Delivered Story Point Counts",
        xaxis_title="Month",
        yaxis_title="Value",
        template="plotly_white",
        height=500
    )
    return fig
    
rel_cnt = get_release_count()
sit_cnt = get_sit_bug_count()
inc_cnt = get_inc_count()
story_point = get_story_points()

# Layout
st.set_page_config(layout="wide")

sprint_row1 = st.container()
with sprint_row1:
        st.plotly_chart(story_point, use_container_width=True)
        
mon_row1 = st.container()
with mon_row1:
        col1, col2 = st.columns(2)
        with col1:
                st.plotly_chart(rel_cnt, use_container_width=True)
        with col2:
                st.plotly_chart(sit_cnt, use_container_width=True)
mon_row2 = st.container()
with mon_row2:
        col1, col2 = st.columns(2)
        with col1:
                st.plotly_chart(inc_cnt, use_container_width=True)
    

    
