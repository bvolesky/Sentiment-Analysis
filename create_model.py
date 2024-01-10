"""
This script performs text classification using a TF-IDF vectorizer and logistic regression classifier, and then saves the trained models and vectorizer to files.

Steps:
1. Reads preprocessed data from a MessagePack file ('data/clean/dataset.msgpack').
2. Converts the data into lists of texts and labels.
3. Performs text vectorization (TF-IDF) on the entire dataset.
4. Splits the dataset into training and testing sets.
5. Creates and trains a logistic regression classifier on the training data.
6. Makes predictions on the test set and calculates accuracy.
7. Saves the trained TF-IDF vectorizer and logistic regression model to files.

Dependencies:
- joblib: Serialization library for saving Python objects (vectorizer and classifier).
- msgpack: Serialization library for loading preprocessed data.
- scikit-learn (sklearn): Machine learning library for text vectorization,
model training, and evaluation.

Input:
- 'data/clean/dataset.msgpack': Preprocessed data in MessagePack format.

Output:
- 'models/vectorizer.joblib': Trained TF-IDF vectorizer saved as a joblib file.
- 'models/logistic_regression_model.joblib': Trained logistic regression classifier
  saved as a joblib file.
- Prints the accuracy of the classifier on the test data.
"""

import joblib
import msgpack

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Read the MessagePack data from the file
input_filepath = "data/clean/dataset.msgpack"
with open(input_filepath, "rb") as file:
    data = msgpack.load(file)

# Convert data to lists
texts = list(data.keys())
labels = list(data.values())

# Text Vectorization (TF-IDF) with the entire dataset
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train a logistic regression classifier
classifier = LogisticRegression(max_iter=1000)
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate and print the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"The accuracy of the classifier is: {accuracy*100}%")

# Save the TF-IDF vectorizer and trained logistic to a file
joblib.dump(vectorizer, "models/vectorizer.joblib")
joblib.dump(classifier, "models/logistic_regression_model.joblib")
