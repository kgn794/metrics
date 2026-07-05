import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import plotly.graph_objects as go
import release_count


release_count = get_release_count()
# Layout
row1 = st.container()
with row1:
    st.plotly_chart(release_count, use_container_width=True)

    
