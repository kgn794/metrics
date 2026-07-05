import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import plotly.graph_objects as go
from release_count import get_release_count


rel_cnt = get_release_count()
# Layout
row1 = st.container()
with row1:
    st.plotly_chart(rel_cnt, use_container_width=True)

    
