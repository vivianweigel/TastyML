![Cover Photo](Figures/cover_photo.png)
# TastyML
#### Rachel Cassway, Simone Ritcheson, & Vivian Weigel
##### Machine Learning 2 - DS 4420
There are countless recommendation systems for TV shows, restaurants, and travel locations, however, when trying to stay home and save money by cooking, it can be hard to find new recipes to try. Further, there are many recommender systems for the nutrition behind diets and food intake, pertaining to calories, macros, and overall nutrition knowledge. However, there were not any available recommender systems based on the recipes ratings for home chefs. The main goal was to create a recipe recommender that considers one’s personal preferences and past ratings of meals, then have a system that would recommend a meal to make the decision process easier and more personalized. Two Machine Learning methods were utilized, Collaborative Filtering (CF) and Multilayer Perceptron (MLP), to build models and compare the best techniques to generate recommendations for users. By building TastyML, a recipe recommendation system that considers past preferences and how others rate the recipes, less experienced chefs can explore what is possible in the kitchen.

Final findings and discussion of results can be found in our paper [Feeding the Algorithm: Building Smarter Recipe Recommenders with ML.](https://docs.google.com/document/d/1GAl89seOvv264gRqhJNJVndyUBb7bOQsP3iJYP6fIVQ/edit?usp=sharing)

#### Repo and Code Information
Recipe review data is sourced from the UC Irvine Machine Learning Repository and can be found [here.](https://archive.ics.uci.edu/dataset/911/recipe+reviews+and+user+feedback+dataset) 

Collaborative filtering code:
  - Code can be found in the file [CF.rmd](CF.Rmd)
  - CF was coded without the use of any libraries
    
MLP Code:
  - Initial draft of a traditional model found in [MLP_traditional_v1.ipynb](MLP_traditional_v1.ipynb)
  - Final MLP code found in [MLP_final_v2.ipynb](MLP_final_v2.ipynb)
  - This file also contains a reccomender function and comparison of CF and MLP results.
  - MLP code utilized libraries.

#### Website - Interactive Recipe Recommender
Our website provides a project overview as well as an interactive results comparison tool. The tool allows you to select a user and view their top 5 reccomended recipes by both CF and MLP. 
Our goal with this project was to provide a useful reccomendation system for recipes and the reccommendation tool demonstrates how both models practically achieve this as well as highlights the differing results between the two methodologies.

To run the streamlit website: save the folder with all of the files, go to a terminal console, navigate to where the folder is, and run the command: streamlit run Home.py. Navigate through the website from Home, to project description, to our interactive results page that filters and shows top five recipies for MLP and CNN recommendations. 

###### TastyML Website Demo
https://github.com/user-attachments/assets/5b971630-9e89-432a-8314-32022af505ce

