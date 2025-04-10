import streamlit as st
import pandas as pd
import plotly.express as px

# Page config at the top
st.set_page_config(page_title="Results", layout="centered")

# Custom CSS
def local_css():
    st.markdown("""
    <style>
    .stApp {
        background-color: #e0f7fa;
        background-image: linear-gradient(to bottom right, #e0f7fa, #fce4ec);
    }
    h1, h2, h3 {
        color: #ec407a;
        text-align: center;
    }
    p, div, label, span {
        color: #555555;
    }
    .stButton > button {
        background-color: #f48fb1;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5em 1em;
    }
    .stButton > button:hover {
        background-color: #f06292;
        color: white;
    }
    img {
        border-radius: 20px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.2);
    }
    .css-1d391kg {
        background-color: #fce4ec;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Page content
st.title("Results")
st.write("Below is the visual representation of our results comparing CF and MLP models.")


results_df = pd.read_csv('/Users/simoneritcheson/Desktop/TastyML/pages/results_df.csv')
import pandas as pd
import streamlit as st

import pandas as pd
import streamlit as st
import pandas as pd
import streamlit as st

# Load your actual data files
cf_df = pd.read_csv('/Users/simoneritcheson/Desktop/TastyML/pages/results_df_CF.csv')
mlp_df = pd.read_csv('/Users/simoneritcheson/Desktop/TastyML/pages/results_df_MLP.csv')
import pandas as pd
import streamlit as st

#st.write("CF Data Sample:", cf_df.head())
#st.write("CF DataFrame Columns:", cf_df.columns.tolist())


#common_users = set(cf_df['user_id']).intersection(set(mlp_df['user_id']))
#st.write("Number of common users between CF and MLP:", len(common_users))
import pandas as pd
import streamlit as st

# Load data files
#cf_df = pd.read_csv('results_df_CF.csv')
#mlp_df = pd.read_csv('results_df_MLP.csv')

# Filter user list to only common users
common_user_ids = set(cf_df['user_id']).intersection(set(mlp_df['user_id']))
user_mapping = mlp_df[mlp_df['user_id'].isin(common_user_ids)][['user_name', 'user_id']].drop_duplicates()

# Streamlit user selection dropdown
selected_username = st.selectbox(
    "Select a User to explore predictions:",
    options=user_mapping['user_name']
)

# Get user ID from selected username
selected_user_id = user_mapping[user_mapping['user_name'] == selected_username]['user_id'].values[0]

# Filter CF and MLP data for selected user
cf_user_df = cf_df[cf_df['user_id'] == selected_user_id]
mlp_user_df = mlp_df[mlp_df['user_id'] == selected_user_id]

st.markdown("### Top 5 Recommended Recipes for Users with at Least 5 Ratings")

# ----- Item-Item CF Top 5 -----
st.subheader("Item-Item Collaborative Filtering Recommendations")

if not cf_user_df.empty and 'predicted_rating' in cf_user_df.columns:
    top_item_item = cf_user_df.sort_values(by='predicted_rating', ascending=False).head(5)
    for idx, row in enumerate(top_item_item.itertuples(), 1):
        if idx == 1:
            st.markdown(f"- **{idx}. {row.recipe_name}** (Predicted Rating: {row.predicted_rating:.2f})")
        else:
            st.markdown(f"{idx}. {row.recipe_name} (Predicted Rating: {row.predicted_rating:.2f})")
else:
    st.write("No Item-Item CF recommendations available for this user.")

# ----- MLP Top 5 -----
st.subheader("MLP Model Recommendations")

if not mlp_user_df.empty and 'predicted_rating' in mlp_user_df.columns:
    top_mlp = mlp_user_df.sort_values(by='predicted_rating', ascending=False).head(5)
    for idx, row in enumerate(top_mlp.itertuples(), 1):
        if idx == 1:
            st.markdown(f"- **{idx}. {row.recipe_name}** (Predicted Rating: {row.predicted_rating:.2f})")
        else:
            st.markdown(f"{idx}. {row.recipe_name} (Predicted Rating: {row.predicted_rating:.2f})")
else:
    st.write("No MLP recommendations available for this user.")


# Navigation
if st.button("Back to Home"):
    st.switch_page("Home.py")
