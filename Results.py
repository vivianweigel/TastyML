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
st.write("Below is the visual representation of our results comparing User-User and Item-Item collaborative filtering models.")

st.write("""
### Findings:
- The User-User model performed better in terms of lower MSE.
- Item-Item collaborative filtering showed decent performance but lagged behind.

### Conclusion:
User-based collaborative filtering better captures user preferences in this recipe dataset!

Feel free to explore the other pages for more details.
""")


results_df = pd.read_csv('/Users/simoneritcheson/Desktop/TastyML/pages/results_df.csv')
# Interactive selection
selected_user = st.selectbox("Select a User ID to explore predictions:", results_df['user_id'].unique())

filtered_df = results_df[results_df['user_id'] == selected_user]

# Scatter plot: Actual vs Predicted Ratings
fig = px.scatter(
    filtered_df,
    x='actual',
    y='user_pred',
    color='recipe_name',
    title=f'User-Based CF: Actual vs. Predicted Ratings for User {selected_user}',
    labels={'actual': 'Actual Rating', 'user_pred': 'Predicted Rating'},
    hover_data=['recipe_name']
)
fig.update_traces(marker=dict(size=12), selector=dict(mode='markers'))

st.plotly_chart(fig, use_container_width=True)

# Add second plot: Item-Based CF
fig2 = px.scatter(
    filtered_df,
    x='actual',
    y='item_pred',
    color='recipe_name',
    title=f'Item-Based CF: Actual vs. Predicted Ratings for User {selected_user}',
    labels={'actual': 'Actual Rating', 'item_pred': 'Predicted Rating'},
    hover_data=['recipe_name']
)
fig2.update_traces(marker=dict(size=12), selector=dict(mode='markers'))

st.plotly_chart(fig2, use_container_width=True)

# Optional: Show errors
st.write("Prediction Errors (User-Based):")
st.dataframe(filtered_df[['recipe_name', 'error_user']])

st.write("Prediction Errors (Item-Based):")
st.dataframe(filtered_df[['recipe_name', 'error_item']])


# Navigation
if st.button("Back to Home"):
    st.switch_page("Home.py")
