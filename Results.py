import streamlit as st
import pandas as pd
import numpy as np

import os
import pandas as pd

csv_path = os.path.join(os.path.dirname(__file__), "ml2_finaldata.csv")
df = pd.read_csv(csv_path)

# Convert timestamps to datetime
df["created_at"] = pd.to_datetime(df["created_at"], unit="s")

# Get list of all users
all_users = sorted(df["user_name"].dropna().unique())

with st.container(border=True):
    users = st.multiselect("Select users", all_users, default=all_users[:3])
    rolling_average = st.toggle("Rolling average")

# Filter by selected users
filtered = df[df["user_name"].isin(users)]

# Group and pivot data to get a timeseries per user
pivot = (
    filtered[["created_at", "user_name", "stars"]]
    .sort_values("created_at")
    .pivot_table(index="created_at", columns="user_name", values="stars")
)

if rolling_average:
    pivot = pivot.rolling(7).mean().dropna()

tab1, tab2 = st.tabs(["Chart", "Dataframe"])
tab1.line_chart(pivot, height=250)
tab2.dataframe(pivot.reset_index(), height=250, use_container_width=True)
