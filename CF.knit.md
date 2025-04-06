---
title: "CF"
author: "rachel_cassway"
date: "2025-04-02"
output:
  html_document: default
  pdf_document: default
---

### Load and Clean Data
Getting data into the following format:
- Rows = users
- Columns = recipes
- Values = ratings (stars)


``` r
# load libraries
library(dplyr)
```

```
## 
## Attaching package: 'dplyr'
```

```
## The following objects are masked from 'package:stats':
## 
##     filter, lag
```

```
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

``` r
library(tidyr)
library(proxy)
```

```
## 
## Attaching package: 'proxy'
```

```
## The following objects are masked from 'package:stats':
## 
##     as.dist, dist
```

```
## The following object is masked from 'package:base':
## 
##     as.matrix
```

``` r
library(scales)

# load csv into dataframe
df <- read.csv("recipe_review_data.csv")

# select collab filtering columns
df <- df %>%
  mutate(
    user_id = trimws(as.character(user_id)),
    recipe_code = trimws(as.character(recipe_code)),
    stars = as.numeric(stars)
  )

# clean ratings: take average if user rated the same item multiple times
ratings_cleaned <- df %>%
  filter(!is.na(stars)) %>%
  group_by(user_id, recipe_code) %>%
  summarise(stars = mean(stars, na.rm = TRUE), .groups = "drop")

# pivot_wider, to prep for matrix
rating_wide <- ratings_cleaned %>%
  pivot_wider(names_from = recipe_code, values_from = stars)

# convert to data.frame before setting rownames
rating_wide <- as.data.frame(rating_wide)

# set user_id as rownames
rating_wide$user_id <- trimws(as.character(rating_wide$user_id))
rownames(rating_wide) <- rating_wide$user_id
rating_wide <- rating_wide %>% select(-user_id)

# convert to numeric matrix
rating_wide[] <- lapply(rating_wide, function(x) as.numeric(as.character(x)))
rating_matrix <- as.matrix(rating_wide)

# preview matrix
head(rating_matrix)
```

```
##                386 2912 8431 39334 100276 12700 17826 42386 41101 11767 27626
## u_05PZUpOV27Pv   5   NA   NA    NA     NA    NA    NA    NA    NA    NA    NA
## u_09Pspx0F3ZKy  NA    5   NA    NA     NA    NA    NA    NA    NA    NA    NA
## u_0BYS3gNJ4rI0  NA   NA    5    NA     NA    NA    NA    NA    NA    NA    NA
## u_0GfixeKJgmAL  NA   NA   NA     5     NA    NA    NA    NA    NA    NA    NA
## u_0HraB0BMR3qu  NA   NA   NA    NA      0    NA    NA    NA    NA    NA    NA
## u_0S8No1lOgccx  NA   NA   NA    NA     NA     5    NA    NA    NA    NA    NA
##                28058 9735 7708 1196 957 18341 2832 7752 43675 1152 3309 32480
## u_05PZUpOV27Pv    NA   NA   NA   NA  NA    NA   NA   NA    NA   NA   NA    NA
## u_09Pspx0F3ZKy    NA   NA   NA   NA  NA    NA   NA   NA    NA   NA   NA    NA
## u_0BYS3gNJ4rI0    NA   NA   NA   NA  NA    NA   NA   NA    NA   NA   NA    NA
## u_0GfixeKJgmAL    NA   NA   NA   NA  NA    NA   NA   NA    NA   NA   NA    NA
## u_0HraB0BMR3qu    NA   NA   NA   NA  NA    NA   NA   NA    NA   NA   NA    NA
## u_0S8No1lOgccx    NA   NA   NA   NA  NA    NA   NA   NA    NA   NA   NA    NA
##                141947 16579 32264 7539 9010 14299 15805 19731 23222 2872 32248
## u_05PZUpOV27Pv     NA    NA    NA   NA   NA    NA    NA    NA    NA   NA    NA
## u_09Pspx0F3ZKy     NA    NA    NA   NA   NA    NA    NA    NA    NA   NA    NA
## u_0BYS3gNJ4rI0     NA    NA    NA   NA   NA    NA    NA    NA    NA   NA    NA
## u_0GfixeKJgmAL     NA    NA    NA   NA   NA    NA    NA    NA    NA   NA    NA
## u_0HraB0BMR3qu     NA    NA    NA   NA   NA    NA    NA    NA    NA   NA    NA
## u_0S8No1lOgccx     NA    NA    NA   NA   NA    NA    NA    NA    NA   NA    NA
##                39545 41384 11588 12347 36450 38183 7178 12540 39549 16458 1693
## u_05PZUpOV27Pv    NA    NA    NA    NA    NA    NA   NA    NA    NA    NA   NA
## u_09Pspx0F3ZKy    NA    NA    NA    NA    NA    NA   NA    NA    NA    NA   NA
## u_0BYS3gNJ4rI0    NA    NA    NA    NA    NA    NA   NA    NA    NA    NA   NA
## u_0GfixeKJgmAL    NA    NA    NA    NA    NA    NA   NA    NA    NA    NA   NA
## u_0HraB0BMR3qu    NA    NA    NA    NA    NA    NA   NA    NA    NA    NA   NA
## u_0S8No1lOgccx    NA    NA    NA    NA    NA    NA   NA    NA    NA    NA   NA
##                27434 33121 26937 12003 1063 17310 6086 11330 14600 31278 4383
## u_05PZUpOV27Pv    NA    NA    NA    NA   NA    NA   NA    NA    NA    NA   NA
## u_09Pspx0F3ZKy    NA    NA    NA    NA   NA    NA   NA    NA    NA    NA   NA
## u_0BYS3gNJ4rI0    NA    NA    NA    NA   NA    NA   NA    NA    NA    NA   NA
## u_0GfixeKJgmAL    NA    NA    NA    NA   NA    NA   NA    NA    NA    NA   NA
## u_0HraB0BMR3qu    NA    NA    NA    NA   NA    NA   NA    NA    NA    NA   NA
## u_0S8No1lOgccx    NA    NA    NA    NA   NA    NA   NA    NA    NA    NA   NA
##                46655 74724 21444 3290 35948 36217 1081 32535 39581 41095 4444
## u_05PZUpOV27Pv    NA    NA    NA   NA    NA    NA   NA    NA    NA    NA   NA
## u_09Pspx0F3ZKy    NA    NA    NA   NA    NA    NA   NA    NA    NA    NA   NA
## u_0BYS3gNJ4rI0    NA    NA    NA   NA    NA    NA   NA    NA    NA    NA   NA
## u_0GfixeKJgmAL    NA    NA    NA   NA    NA    NA   NA    NA    NA    NA   NA
## u_0HraB0BMR3qu    NA    NA    NA   NA    NA    NA   NA    NA    NA    NA   NA
## u_0S8No1lOgccx    NA    NA    NA   NA    NA    NA   NA    NA    NA    NA   NA
##                6504 82745 9739 10252 12734 20170 33206 3058 191775 42873 18274
## u_05PZUpOV27Pv   NA    NA   NA    NA    NA    NA    NA   NA     NA    NA    NA
## u_09Pspx0F3ZKy   NA    NA   NA    NA    NA    NA    NA   NA     NA    NA    NA
## u_0BYS3gNJ4rI0   NA    NA   NA    NA    NA    NA    NA   NA     NA    NA    NA
## u_0GfixeKJgmAL   NA    NA   NA    NA    NA    NA    NA   NA     NA    NA    NA
## u_0HraB0BMR3qu   NA    NA   NA    NA    NA    NA    NA   NA     NA    NA    NA
## u_0S8No1lOgccx   NA    NA   NA    NA    NA    NA    NA   NA     NA    NA    NA
##                33457 27696 42083 12259 10248 1821 24886 8015 1324 38550 33743
## u_05PZUpOV27Pv    NA    NA    NA    NA    NA   NA    NA   NA   NA    NA    NA
## u_09Pspx0F3ZKy    NA    NA    NA    NA    NA   NA    NA   NA   NA    NA    NA
## u_0BYS3gNJ4rI0    NA    NA    NA    NA    NA   NA    NA   NA   NA    NA    NA
## u_0GfixeKJgmAL    NA    NA    NA    NA    NA   NA    NA   NA   NA    NA    NA
## u_0HraB0BMR3qu    NA    NA    NA    NA    NA   NA    NA   NA   NA    NA    NA
## u_0S8No1lOgccx    NA    NA    NA    NA    NA   NA    NA   NA   NA    NA    NA
##                27675 35766 414 3143 18345 34347 3683 45495 19201 8202 17022
## u_05PZUpOV27Pv    NA    NA  NA   NA    NA    NA   NA    NA    NA   NA    NA
## u_09Pspx0F3ZKy    NA    NA  NA   NA    NA    NA   NA    NA    NA   NA    NA
## u_0BYS3gNJ4rI0    NA    NA  NA   NA    NA    NA   NA    NA    NA   NA    NA
## u_0GfixeKJgmAL    NA    NA  NA   NA    NA    NA   NA    NA    NA   NA    NA
## u_0HraB0BMR3qu    NA    NA  NA   NA    NA    NA   NA    NA    NA   NA    NA
## u_0S8No1lOgccx    NA    NA  NA   NA    NA    NA   NA    NA    NA   NA    NA
```

``` r
# make sure each recipe is distinct in lookup table
recipe_lookup <- df %>%
  select(recipe_code, recipe_name) %>%
  distinct(recipe_code, .keep_all = TRUE)  
```
### Some analysis on data to explore popular recipes and frequent users

``` r
# which users have rated the most recipes
user_rating_counts <- rowSums(!is.na(rating_matrix))
top_users <- sort(user_rating_counts, decreasing = TRUE)

head(top_users)
```

```
## u_1oKVZzipo1u8lcqQzDUcw4UBn9e u_1oKVZdmUbQTYMVdbXOpVfRQuHm9 
##                            25                            23 
## u_1oKVZmYPulmUFbvGiBA8U3uRR6D u_1oKVZoIOMWJ2j7TA7py2BIbf1mm 
##                            23                            23 
## u_1oKVeN9YNf07RT0P9R63Yu80P5A u_1oKVZxAOR5BEzyF4H6ENc7jwfUW 
##                            23                            22
```

``` r
length(user_rating_counts[user_rating_counts >= 10])
```

```
## [1] 52
```

``` r
# which recipe has the most ratings
recipe_popularity <- df %>%
  filter(!is.na(stars)) %>%
  count(recipe_code, recipe_name, sort = TRUE)

head(recipe_popularity)
```

```
##   recipe_code             recipe_name   n
## 1        2832       Cheeseburger Soup 725
## 2       14299      Creamy White Chili 654
## 3        3309  Best Ever Banana Bread 509
## 4       42083   Enchilada Casser-Ole! 421
## 5       32480    Basic Homemade Bread 397
## 6       21444 Favorite Chicken Potpie 395
```

``` r
# users who rated most recipes, with highest user reputation
top_reviewers <- df %>%
  filter(!is.na(stars)) %>%
  group_by(user_id, user_name) %>%
  summarise(
    num_reviews = n(),
    avg_rating = mean(stars),
    user_reputation = max(user_reputation),
    .groups = "drop" 
  ) %>%
  arrange(desc(num_reviews))
```
### User-User Collaborative Filtering Function

``` r
user_user_cf <- function(df, user, sim_metric = "Cosine", k = 2, 
                         recipe_lookup_df = NULL) {
  
  # if user not in data, return not found message
  if (!(user %in% rownames(df))) {
    message("Error: User not found in dataset.")
    return(NULL)
  }

  # if the user has no missing values, return message
  if (all(!is.na(df[user, ]))) {
    message("User has no missing ratings to predict.")
    return(NULL)
  }

  # if similarity metric not Cosine or L2, return message
  if (!(sim_metric %in% c("Cosine", "L2"))) {
    message("Unsupported similarity metric. Use 'Cosine' or 'L2'.")
    return(NULL)
  }

  # 1. center data by row means
  user_means <- rowMeans(df, na.rm = TRUE)
  centered_data <- sweep(df, 1, user_means, FUN = "-")
  # fill NaN values with 0 for user-user only
  centered_data[is.na(centered_data)] <- 0  

  # 2. get target user vector
  user_vector <- as.matrix(centered_data[user, , drop = FALSE])

  # 3. compute similarity
  if (sim_metric == "Cosine") {
    sim_vec <- proxy::simil(user_vector, centered_data, method = "cosine")
    similarity_scores <- as.vector(sim_vec)
  } else if (sim_metric == "L2") {
    diff <- centered_data - matrix(rep(user_vector, nrow(centered_data)), 
                                   nrow = nrow(centered_data), byrow = TRUE)
    similarity_scores <- -sqrt(rowSums(diff^2))
  }

  # 4. normalize similarity
  similarity_scores <- rescale(similarity_scores, to = c(0, 1))
  sim_df <- data.frame(User = rownames(df), Similarity = similarity_scores)
  sim_df <- sim_df %>% filter(User != user)

  # 5. select top k similar users
  top_k_users <- sim_df %>%
  arrange(desc(Similarity)) %>%
  slice_head(n = min(k, nrow(sim_df)))


  # 6. prepare ratings for predictions
  k_ratings <- df[top_k_users$User, ]
  k_ratings <- t(apply(k_ratings, 1, function(row) {
    row[is.na(row)] <- mean(row, na.rm = TRUE)
    return(row)
  }))

  # 7. weighted prediction
  if (sum(top_k_users$Similarity) == 0) {
    message("Warning: All similarities are zero. Returning NULL.")
    return(NULL)
  }

  # calc ratings
  weighted <- sweep(k_ratings, 1, top_k_users$Similarity, FUN = "*")
  predicted_ratings <- colSums(weighted) / sum(top_k_users$Similarity)

  # return missing predictions only for target user
  result <- data.frame(recipe_code = colnames(df), Predicted_Rating = predicted_ratings)
  missing_items <- is.na(df[user, ])
  result <- result[missing_items, ]
  
  # add recipe names if provided in original df
  if (!is.null(recipe_lookup_df)) {
    result <- result %>%
      left_join(recipe_lookup_df, by = "recipe_code") %>%
      select(recipe_code, recipe_name, Predicted_Rating)
  }

  result <- result %>%
    arrange(desc(Predicted_Rating))
  
  return(result)
}
```



### Item-Item Collaborative Filtering Function

``` r
item_item_cf <- function(df, user, sim_metric = "Cosine", k = 2, 
                         recipe_lookup_df = NULL) {
  
  # if user not in data, return not found message
  if (!(user %in% rownames(df))) {
    message("Error: User not found in dataset.")
    return(NULL)
  }

  # if the user has no missing values, return message
  if (all(!is.na(df[user, ]))) {
    message("User has no missing ratings to predict.")
    return(NULL)
  }

  # if similarity metric not Cosine or L2, return message
  if (!(sim_metric %in% c("Cosine", "L2"))) {
    message("Unsupported similarity metric. Use 'Cosine' or 'L2'.")
    return(NULL)
  }
  
  # 1. center by column (item) means
  item_means <- colMeans(df, na.rm = TRUE)
  centered_data <- sweep(df, 2, item_means, FUN = "-")
  centered_data[is.na(centered_data)] <- 0

  # 2. transpose for item-based similarity (now rows = items)
  item_data <- t(centered_data)

  # 3. ratings the user has already made
  user_vector <- as.numeric(df[user, ])
  names(user_vector) <- colnames(df)

  predictions <- numeric(ncol(df))
  names(predictions) <- colnames(df)

  for (item in names(user_vector)) {
    # skip if user already rated it
    if (!is.na(user_vector[item])) next

    # get all items the user has rated
    rated_items <- names(user_vector)[!is.na(user_vector)]

    # compute similarity between this target item and all items the user rated
    if (sim_metric == "Cosine") {
      sim_scores <- proxy::simil(as.matrix(item_data[item, , drop = FALSE]),
                                 item_data[rated_items, , drop = FALSE],
                                 method = "cosine")
      sim_scores <- as.vector(sim_scores)
    } else if (sim_metric == "L2") {
      diff <- item_data[item, ] - item_data[rated_items, ]
      sim_scores <- -sqrt(rowSums(diff^2))
    }

    # 4. normalize similarity
    sim_scores <- rescale(sim_scores, to = c(0, 1))

    # grab the user’s ratings for the similar items
    rated_scores <- user_vector[rated_items]

    # 5. select top k similar users
    top_k <- order(sim_scores, decreasing = TRUE)[1:min(k, length(sim_scores))]
    top_k_sims <- sim_scores[top_k]
    top_k_sims <- top_k_sims[!is.na(top_k_sims)]
    top_k_ratings <- rated_scores[top_k]

    # 6. make predictions
    if (sum(top_k_sims) == 0) {
      predictions[item] <- NA
    } else {
      predictions[item] <- sum(top_k_sims * top_k_ratings) / sum(top_k_sims)
    }
  }

  # convert predictions to a data frame
  result <- data.frame(recipe_code = names(predictions), Predicted_Rating = predictions)
  result <- result[is.na(df[user, ]), ]

  # add recipe names if provided
  if (!is.null(recipe_lookup_df)) {
    result <- result %>%
      left_join(recipe_lookup_df, by = "recipe_code") %>%
      select(recipe_code, recipe_name, Predicted_Rating)
  }

  result <- result %>%
    filter(!is.na(Predicted_Rating)) %>%
    arrange(desc(Predicted_Rating))

  return(result)
}
```


### Gelper Function to Find Rating for One Target User and One Target Recipe

``` r
predict_one_recipe <- function(rating_matrix, user_id, recipe_code, k = 5, 
                               sim_metric = "Cosine", method = "user", 
                               recipe_lookup_df = NULL) {
  # Check method type
  if (!(method %in% c("user", "item"))) {
    stop("Method must be either 'user' or 'item'")
  }

  if (method == "user") {
    # run user-user collaborative filtering
    predictions <- user_user_cf(
      df = rating_matrix,
      user = user_id,
      sim_metric = sim_metric,
      k = k,
      recipe_lookup_df = recipe_lookup_df
    )

  } else if (method == "item") {
    # run item-item collaborative filtering 
    predictions <- item_item_cf(
      df = rating_matrix,
      user = user_id,
      sim_metric = sim_metric,
      k = k,
      recipe_lookup_df = recipe_lookup_df
    )

  }
  
  # filter to just the target recipe
  prediction <- predictions[predictions$recipe_code == recipe_code, ]

  return(prediction)
}
```

### Evaluate CF Models Function
In order to test the capabilities the models, we will 
1. pick a user with a good number of ratings
2. randomly hide a few of their actual ratings (setting to NA)
3. run prediction for those recipes
4. compare predicted vs actual ratings

``` r
evaluate_user_cf <- function(test_user, rating_matrix, seed = 42, k = 5, 
                             n_holdout = 5, sim_metric = "Cosine", 
                             recipe_lookup_df = NULL) {
  # find the items this user has rated
  rated_items <- which(!is.na(rating_matrix[test_user, ]))
  
  # randomly hold out 5 of their ratings - 
  set.seed(seed)  # for reproducibility
  held_out_items <- sample(rated_items, n_holdout)
  
  # store true ratings to compare later
  true_ratings <- rating_matrix[test_user, held_out_items]
  
  # make test matrix (copied matrix with held-out values set to NA)
  test_matrix <- rating_matrix
  test_matrix[test_user, held_out_items] <- NA
  
  # Predict using user-user or item-item
  pred_user_user <- user_user_cf(test_matrix, user = test_user, 
                                 sim_metric = sim_metric, k = k, 
                                 recipe_lookup_df = recipe_lookup_df)
  pred_item_item <- item_item_cf(test_matrix, user = test_user, 
                                 sim_metric = sim_metric, k = k,
                                 recipe_lookup_df = recipe_lookup_df)
  
  # build a full comparison table
  
  # filter both prediction outputs to the held-out recipe codes
  user_preds <- pred_user_user %>%
    filter(recipe_code %in% names(true_ratings)) %>%
    select(recipe_code, recipe_name, user_pred = Predicted_Rating)
  
  item_preds <- pred_item_item %>%
    filter(recipe_code %in% names(true_ratings)) %>%
    select(recipe_code, item_pred = Predicted_Rating)
  
  # merge user and item predictions
  comparison <- user_preds %>%
    left_join(item_preds, by = "recipe_code")
  
  # add actual held-out ratings and user ID
  comparison$actual <- true_ratings[comparison$recipe_code]
  comparison$user_id <- test_user

  # reorder columns for readability
  comparison <- comparison %>%
    select(user_id, recipe_code, recipe_name, user_pred, item_pred, actual)

  
  return(comparison)
}
```

### Testing Functions Individually

``` r
# find users with at least one missing rating to predict for
users_with_missing <- rownames(rating_matrix)[
  apply(rating_matrix, 1, function(row) any(is.na(row)))
]

# test user
test_user <- users_with_missing[50]
print(paste("Testing user:", test_user))
```

```
## [1] "Testing user: u_1oKVZayWppErhTC8Zdspk9bGr7q"
```

``` r
# predict for chosen test user with user-user CF
predicted_ratings <- user_user_cf(rating_matrix, user = test_user, 
                                  sim_metric = "Cosine", k = 5, 
                                  recipe_lookup_df = recipe_lookup)

# display predictions
print(paste("USER-USER: Predicted ratings for missing items for test user:", test_user))
```

```
## [1] "USER-USER: Predicted ratings for missing items for test user: u_1oKVZayWppErhTC8Zdspk9bGr7q"
```

``` r
head(predicted_ratings)
```

```
##   recipe_code                  recipe_name Predicted_Rating
## 1       11767 Quick Cream of Mushroom Soup         4.389094
## 2       12540    Flavorful Chicken Fajitas         4.389094
## 3        3309       Best Ever Banana Bread         4.335436
## 4       10248       Garlic Beef Enchiladas         4.335436
## 5        1821       Blueberry French Toast         4.335436
## 6        8431         Rhubarb Custard Bars         4.323228
```

``` r
# predict for chosen test user with item-item CF
predicted_ratings <- item_item_cf(rating_matrix, user = test_user, 
                                  sim_metric = "Cosine", k = 5, 
                                  recipe_lookup_df = recipe_lookup)

# display predictions
print(paste("ITEM-ITEM: Predicted ratings for missing items for test user:", test_user))
```

```
## [1] "ITEM-ITEM: Predicted ratings for missing items for test user: u_1oKVZayWppErhTC8Zdspk9bGr7q"
```

``` r
head(predicted_ratings)
```

```
##   recipe_code             recipe_name Predicted_Rating
## 1       32480    Basic Homemade Bread         4.795367
## 2        7539         Fluffy Pancakes         4.794980
## 3        6086               Apple Pie         4.791142
## 4       21444 Favorite Chicken Potpie         4.765407
## 5        1081         Baked Spaghetti         4.764737
## 6        8202        Simple Taco Soup         4.757200
```

``` r
# find rating for target user and target recipe 
target_user <- "u_05PZUpOV27Pv"
target_recipe <- "3309"
head(recipe_popularity)
```

```
##   recipe_code             recipe_name   n
## 1        2832       Cheeseburger Soup 725
## 2       14299      Creamy White Chili 654
## 3        3309  Best Ever Banana Bread 509
## 4       42083   Enchilada Casser-Ole! 421
## 5       32480    Basic Homemade Bread 397
## 6       21444 Favorite Chicken Potpie 395
```

``` r
predict_one_recipe(rating_matrix, target_user, target_recipe, k = 5, method="user", 
                   recipe_lookup_df = recipe_lookup)
```

```
##    recipe_code            recipe_name Predicted_Rating
## 21        3309 Best Ever Banana Bread                4
```

``` r
predict_one_recipe(rating_matrix, target_user, target_recipe, k = 5, method="item", 
                   recipe_lookup_df = recipe_lookup)
```

```
##    recipe_code            recipe_name Predicted_Rating
## 21        3309 Best Ever Banana Bread                5
```

``` r
# test evaluate function
rated_10 <- user_rating_counts[user_rating_counts >= 10]
test_user <- names(rated_10)[1]  # first user in the group
evaluate_user_cf(test_user, rating_matrix, seed = 42, 
                 k = 5, n_holdout = 5, sim_metric = "Cosine", 
                 recipe_lookup_df = recipe_lookup)
```

```
##                         user_id recipe_code                  recipe_name
## 1 u_1oKVZT7bnHOk8MH7Aom0wkTCJNo        2912     Zucchini Pizza Casserole
## 2 u_1oKVZT7bnHOk8MH7Aom0wkTCJNo        3309       Best Ever Banana Bread
## 3 u_1oKVZT7bnHOk8MH7Aom0wkTCJNo       19731             Cauliflower Soup
## 4 u_1oKVZT7bnHOk8MH7Aom0wkTCJNo       32248    Smothered Chicken Breasts
## 5 u_1oKVZT7bnHOk8MH7Aom0wkTCJNo       41384 Black Bean ‘n’ Pumpkin Chili
##   user_pred item_pred actual
## 1  4.583422  4.663893      4
## 2  4.551441  4.679517      5
## 3  4.551441  4.780001      5
## 4  4.551441  4.423024      5
## 5  4.551441  4.345472      2
```

# Loop Through Eval Functino to See Accuracy Accross Methods

``` r
eval_cf_multiple_users <- function(recipes_rated_min = 1, rating_matrix, 
                                   seed = 42, k = 5, n_holdout = 3, 
                                   sim_metric = "Cosine",
                                   recipe_lookup_df = recipe_lookup) {
  
  user_matrix <- rating_matrix[rowSums(!is.na(rating_matrix)) 
                               >= recipes_rated_min, ]
  
  # initialize empty data frame
  results_df <- data.frame()  

  for (user in rownames(user_matrix)) {
    result <- evaluate_user_cf(user, rating_matrix, seed = seed, k = k, 
                               n_holdout = n_holdout, sim_metric = sim_metric, 
                               recipe_lookup_df = recipe_lookup_df)
    
    if (!is.null(result) && nrow(result) > 0) {
      results_df <- rbind(results_df, result)
    }
  }
  
  return(results_df)
  
}
```

### Testing CF Models by Hiding Ratings, Plus Analysis

``` r
library(ggplot2)
library(dplyr)

# recommending for users with >= 5 recipes, hiding 3, whole ratings matrix 
results_df <- eval_cf_multiple_users(recipes_rated_min = 5, 
                                     rating_matrix = rating_matrix, 
                                     seed = 42,
                                     k = 5, 
                                     n_holdout = 3, 
                                     sim_metric = "Cosine", 
                                     recipe_lookup_df = recipe_lookup)


results_df$error_user <- results_df$user_pred - results_df$actual
results_df$error_item <- results_df$item_pred - results_df$actual

ggplot(results_df, aes(x = error_user)) + 
  geom_histogram(binwidth = 0.5) + 
  ggtitle("User-User Prediction Error Distribution")
```

<img src="CF_files/figure-html/unnamed-chunk-9-1.png" width="672" />

``` r
ggplot(results_df, aes(x = error_item)) + 
  geom_histogram(binwidth = 0.5) + 
  ggtitle("Item-Item Prediction Error Distribution")
```

<img src="CF_files/figure-html/unnamed-chunk-9-2.png" width="672" />

``` r
user_rating_counts <- data.frame(
  user_id = rownames(rating_matrix),
  num_ratings = rowSums(!is.na(rating_matrix))
)

# which model performs better PER USER
user_level_perf <- results_df %>%
  group_by(user_id) %>%
  summarise(
    mse_user = mean((user_pred - actual)^2, na.rm = TRUE),
    mse_item = mean((item_pred - actual)^2, na.rm = TRUE),
    mae_user = mean(abs(user_pred - actual), na.rm = TRUE),
    mae_item = mean(abs(item_pred - actual), na.rm = TRUE)
  ) %>%
   left_join(user_rating_counts, by = "user_id")

per_user_mse <- ggplot(user_level_perf, aes(x = mse_user, y = mse_item, 
  color = num_ratings)) +
  geom_point() +
  geom_abline(slope = 1, intercept = 0, linetype = "dashed") +
  scale_color_gradient(low = "pink", high = "darkblue") +
  labs(title = "Per-User MSE: User-User vs Item-Item") 
print(per_user_mse)
```

<img src="CF_files/figure-html/unnamed-chunk-9-3.png" width="672" />

``` r
# save plot
ggsave(
  filename = "per_user_mse.png",      
  plot = per_user_mse,                       
  width = 8, height = 6, dpi = 300 
)

# MSE
paste("MSE (user-user):", mean(user_level_perf$mse_user))
```

```
## [1] "MSE (user-user): 1.23998683831408"
```

``` r
paste("MSE (item-item):", mean(user_level_perf$mse_item))
```

```
## [1] "MSE (item-item): 1.09720922370617"
```

``` r
# % of users where user-user is better
print(paste("Pct users where user-user performs better:", 
            mean(user_level_perf$mse_user < user_level_perf$mse_item)))  
```

```
## [1] "Pct users where user-user performs better: 0.282051282051282"
```

``` r
# % of users where item-item is better
print(paste("Pct users where item-item performs better:", 
            mean(user_level_perf$mse_item < user_level_perf$mse_user)))
```

```
## [1] "Pct users where item-item performs better: 0.709401709401709"
```

# Comparing Above With Using Just the Subset of Users Rating >= 5 Recipes

``` r
# subset ratings matrix (only users rating >= 5 recipes)
subset_rating_matrix <- rating_matrix[rowSums(!is.na(rating_matrix)) 
                               >= 5, ]

# recommending for users with >= 5 recipes, hiding 3, whole ratings matrix 
subset_results_df <- eval_cf_multiple_users(recipes_rated_min = 5, 
                                     rating_matrix = subset_rating_matrix, 
                                     seed = 42,
                                     k = 5, 
                                     n_holdout = 3, 
                                     sim_metric = "Cosine", 
                                     recipe_lookup_df = recipe_lookup)


user_rating_counts <- data.frame(
  user_id = rownames(subset_rating_matrix),
  num_ratings = rowSums(!is.na(subset_rating_matrix))
)

# which model performs better PER USER
user_level_perf <- subset_results_df %>%
  group_by(user_id) %>%
  summarise(
    mse_user = mean((user_pred - actual)^2, na.rm = TRUE),
    mse_item = mean((item_pred - actual)^2, na.rm = TRUE),
    mae_user = mean(abs(user_pred - actual), na.rm = TRUE),
    mae_item = mean(abs(item_pred - actual), na.rm = TRUE)
  ) %>%
   left_join(user_rating_counts, by = "user_id")

per_user_mse <- ggplot(user_level_perf, aes(x = mse_user, y = mse_item, 
  color = num_ratings)) +
  geom_point() +
  geom_abline(slope = 1, intercept = 0, linetype = "dashed") +
  scale_color_gradient(low = "pink", high = "darkblue") +
  labs(title = "Per-User MSE: User-User vs Item-Item (subset)") 

print(per_user_mse)
```

<img src="CF_files/figure-html/unnamed-chunk-10-1.png" width="672" />

``` r
# save plot
ggsave(
  filename = "subset_per_user_mse.png",      
  plot = per_user_mse,                       
  width = 8, height = 6, dpi = 300 
)

# MSE
paste("MSE (user-user):", mean(user_level_perf$mse_user))
```

```
## [1] "MSE (user-user): 0.838884448788932"
```

``` r
paste("MSE (item-item):", mean(user_level_perf$mse_item))
```

```
## [1] "MSE (item-item): 1.19667171145595"
```

``` r
# % of users where user-user is better
print(paste("Pct users where user-user performs better:", 
            mean(user_level_perf$mse_user < user_level_perf$mse_item)))  
```

```
## [1] "Pct users where user-user performs better: 0.457264957264957"
```

``` r
# % of users where item-item is better
print(paste("Pct users where item-item performs better:", 
            mean(user_level_perf$mse_item < user_level_perf$mse_user)))
```

```
## [1] "Pct users where item-item performs better: 0.235042735042735"
```

