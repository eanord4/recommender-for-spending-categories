# recommender-for-spending-categories
A purchase recommender system specialized to match items to a spending distribution across categories


## Background

Recommender systems are a useful way of directing product advertisements to the right people. In theory, any information gathered from a user's actions in any app could be used to characterize that user and thus to target the appropriate ads toward them. Traditional recommender systems are usually based on data of the same nature as that used to characterize the products themselves; [this Kaggle notebook](https://www.kaggle.com/saurav9786/recommender-system-using-amazon-reviews) explains several types of recommender systems. However, a useful resource with vast amounts of product rating data is [Amazon review data](https://nijianmo.github.io/amazon/index.html#subsets "Jianmo Ni's Amazon review data collections"), so it would be nice to be able to use this data to make recommendations in any app that gathers vaguely related data on the user, even if not perfectly analogous to Amazon's data.


## Mission

This project aims to create a recommender system that bridges the differences between this Amazon data and user data gathered in [Fundwatch](https://fundwatch.herokuapp.com/dashboard) (https://github.com/annasiatico/project3-FundWatch), a convenient expense tracker and budgeting app. Challenges in doing so include:
1. Fundwatch data is gathered for *transactions*, rather than items.
2. The practical level of detail at which Amazon's *item* data is related to Fundwatch's *transaction* data is the *category* of spending, but yet the goal is to recommend *items* instead of *categories*.
3. Category names are neither the same nor necessarily a one-to-one mapping between a user's budget data and Amazon's review data.


## Process

1. Determine the top *k* most similar Amazon users
2. Fill in any missing data (or, if possible, ensure that all the data is there in the original set of similar Amazon users)
3. Pick the "best" item by some metric (ultimately we want to maximize profit, so this is not necessarily the most highly rated one)
4. Present the item in a clickable fashion to the user, using product metadata


## Requirements

* Amazon review data in a quickly accessible format
* Precomputed spending distributions of Amazon users, using prices from product metadata
* Depending on the method of filling in missing data, a precomputed similarity matrix between Amazon users
* FundWatch-Amazon category mappings
* In practice: meaningful and consistent categorization of FundWatch transactions, likely using NLP to autocategorize



