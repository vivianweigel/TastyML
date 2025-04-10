import streamlit as st

# Page config at the very top
st.set_page_config(page_title="Recipe Reviews", layout="centered")

# Custom CSS function
def local_css():
    st.markdown("""
    <style>
    .stApp {
        background-color: lightblue;
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
st.title("Feeding the Algorithm: Building Smarter Recipe Recommenders with Machine Learning")
st.write("🍝🍩🥪🥙🥩🥗")
st.write("""Welcome to our Machine Learning Final Project! Use the navigation on the sidebar to learn more about the project and see the results.""")
st.write("""There are countless recommendation systems for TV shows, restaurants, and travel locations, however, when trying to stay home and save money by cooking,**it can be hard to find new recipes to try.** 

In our research we found that there were many recommender systems for the nutrition behind diets and food intake, pertaining to calories, macros, and overall nutrition knowledge. 

However, we could not find **any** readily available recommender system based on the recipes that were available to users. 

**Our goal was to create a recipe recommender that considers one’s personal preferences and past ratings of meals, then have a system that would recommend a meal to make the decision process easier and more personalized.** 

We utilized two Machine Learning methods: **Multi Layer Perceptron (MLP) and Collaborative Filtering (CF)** to build a system and compare the best machine learning techniques to obtain the best recommendations for users. By building a recipe recommendation system that considers past preferences and how others rate the meals, less experienced chefs can explore what is possible in the kitchen.""")
st.write("Rachel Cassway, Vivian Weigel, Simone Ritcheson""")
st.write("🍝🍩🥪🥙🥩🥗")

# Navigation buttons
if st.button("Project Description"):
    st.switch_page("pages/Project_Description.py")

if st.button("Results"):
    st.switch_page("pages/Results.py")
