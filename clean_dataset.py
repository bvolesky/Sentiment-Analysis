"""
This script reads a CSV file containing sentiment data, performs data preprocessing,
and serializes the cleaned data to a MessagePack file.

Steps:
1. Reads a CSV file with specified column names ('sentiment', 'title', 'body').
2. Combines 'title' and 'body' columns into a single 'review' column.
3. Converts sentiment values (1 -> 0, 2 -> 1) for binary sentiment classification.
4. Drops 'title' and 'body' columns as they are no longer needed.
5. Removes rows where 'review' is NaN to ensure data cleanliness.
6. Reorders columns to have 'review' as the first column.
7. Converts the DataFrame to a dictionary for serialization.
8. Serializes the dictionary using MessagePack and saves it to a file
  ('data/clean/dataset.msgpack').

Dependencies:
- pandas: Data manipulation library.
- msgpack: Serialization library for storing data efficiently.

Input:
- 'data/raw/dataset.csv': CSV file containing sentiment data with
  columns 'sentiment', 'title', and 'body'.

Output:
- 'data/clean/dataset.msgpack': Serialized data in MessagePack format.
"""


import pandas as pd
import msgpack

# Define the column names for the CSV file
column_names = ["sentiment", "title", "body"]

# Read the CSV file with specified column names
new_train_df = pd.read_csv("data/raw/dataset.csv", header=None, names=column_names)

# Combine 'title' and 'body' columns into a single 'review' column
new_train_df["review"] = new_train_df["title"] + " | " + new_train_df["body"]

# Replace 'sentiment' values (1 -> 0, 2 -> 1) for binary sentiment classification
new_train_df["sentiment"] = new_train_df["sentiment"].replace({1: 0, 2: 1})

# Drop 'title' and 'body' columns as they are no longer needed
new_train_df = new_train_df.drop(["title", "body"], axis=1)

# Drop rows where 'review' is NaN to ensure data cleanliness
new_train_df = new_train_df.dropna(subset=["review"])

# Reorder columns to have 'review' as the first column
new_train_df = new_train_df[["review", "sentiment"]]

# Convert DataFrame to a dictionary for serialization
data_dict = new_train_df.set_index("review")["sentiment"].to_dict()

# Serialize the dictionary using MessagePack and save to a file
with open("data/clean/dataset.msgpack", "wb") as file:
    msgpack.dump(data_dict, file)
