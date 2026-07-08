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
        "Value": [0, 0, 0, 0, 0, 3]
    })

df_inc_count = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Value": [30, 28, 33, 38, 3, 37]
    })

df_story_points_bkp = pd.DataFrame({
    "Sprint": ["173", "174", "176", "177", "178", "179", "181", "182", "183", "184", "185"],
    "Committed": [33, 57, 44, 66, 70, 58, 71, 51, 74, 56, 59],
    "Delivered": [25, 16, 7, 24, 42, 40, 70, 34, 61, 24, 18],
    "DaySupport": [ 8, 25, 51, 31, 57, 59, 32, 24, 31, 21, 36],
    "NightSupport" : [ 0, 0, 2, 0, 4, 5, 4, 5, 0, 4, 15],
    "Bug" : [ 0, 0, 2, 0, 3, 5, 3, 1, 1, 1, 0]
        
})
df_story_points = pd.DataFrame({
    "Sprint": ["177", "178", "179", "181", "182", "183", "184", "185"],
    "Committed": [66, 70, 58, 71, 51, 74, 56, 59],
    "Delivered": [24, 42, 40, 70, 34, 61, 24, 18],
    "DaySupport": [31, 57, 59, 32, 24, 31, 21, 36],
    "NightSupport" : [ 0, 4, 5, 4, 5, 0, 4, 15],
    "Bug" : [  0, 3, 5, 3, 1, 1, 1, 0]
        
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
    goal = 1
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
        xaxis_title="Month",
        yaxis_title="Value",
        template="plotly_white",
        height=500
    )
    return fig

def get_story_points():
    df = df_story_points
    df["Velocity"] =  df["Delivered"] + df["DaySupport"]/5 + df["NightSupport"]/2 + df["Bug"]
    df["Velocity"] = df["Velocity"]
    # Statistics
    mean = df["Velocity"].mean()
    no_of_sprint = df["Velocity"].count()
    total_leaves = 40
    mean = mean + (total_leaves/no_of_sprint)
    std = df["Velocity"].std()
    
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
            y=df["Velocity"],
            mode="lines+markers",
            name="Delivered SP",
            line=dict(color="green", width=3)
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df["Sprint"],
            y=df["Bug"],
            mode="lines+markers",
            name="Bug",
            line=dict(color="red", width=1, dash="dot")
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df["Sprint"],
            y=df["DaySupport"],
            mode="lines+markers",
            name="Day Support Tickets",
            line=dict(color="brown", width=1, dash="dot")
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df["Sprint"],
            y=df["NightSupport"],
            mode="lines+markers",
            name="Night Support Tickets",
            line=dict(color="gray", width=1, dash="dot")
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
        annotation_text=f"<b>Capacity = {goal}</b>",
        annotation_position="top left",
        annotation_font=dict(
            color="green",
            size=14
        )
    )
    
    fig.update_layout(
        title="Committed and Delivered Story Point Counts",
        xaxis_title="Sprint",
        yaxis_title="Committed & Delivered",
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
        st.subheader("Delivered = Delivered SP + Support + Bug")
        st.write("5 Day support tickets = 1 Story point")
        st.write("2 Night support tickets = 1 Story point")
        st.write("1 Bug = 1 Story point")
        st.plotly_chart(story_point, width="stretch")
        
mon_row1 = st.container()
with mon_row1:
        col1, col2 = st.columns(2)
        with col1:
                st.plotly_chart(rel_cnt, width="stretch")
        with col2:
                st.plotly_chart(sit_cnt, width="stretch")
mon_row2 = st.container()
with mon_row2:
        col1, col2 = st.columns(2)
        with col1:
                st.plotly_chart(inc_cnt, width="stretch")
    

    
