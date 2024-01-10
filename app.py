"""
Sentiment Analysis Web Application using Flask

This module implements a simple web application using the Flask framework to perform
sentiment analysis on user-submitted text reviews. It provides a web interface where
users can enter a review, and the application predicts whether the sentiment of the
review is positive or negative. Additionally, it includes an automatic feature to open
the web application in the default browser when the server starts.

Dependencies:
    - Flask: A micro web framework for Python.
    - joblib: A library for saving and loading machine learning models.
    - webbrowser: A module for displaying web-based documents.

The application consists of three main functions:
    - index(): Handles requests to the root URL ('/') and displays the web interface
      for sentiment analysis.
    - predict_sentiment(text: str) -> int: Predicts the sentiment of a given text
      using a pre-trained model.
    - open_browser(): Opens the web application in the default web browser once the
      server starts.

Usage:
    1. Ensure that the required dependencies are installed.
    2. Run this script, and the web application will be accessible at
       http://127.0.0.1:5000/ or http://localhost:5000/. The application will also
       automatically open in the default web browser.
    3. Users can enter text reviews, and the application will predict the sentiment.

This module should be executed directly to start the Flask application.
"""
import logging
from flask import Flask, render_template, request
import joblib

# Create a Flask web application
app = Flask(__name__)

# Set up logger
logging.basicConfig(filename='logging/app.log', level=logging.DEBUG, filemode='w',
                    format='%(asctime)s %(levelname)s %(name)s : %(message)s')

# Create a StreamHandler for logging stdout
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # or other level of your choice
console_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s : %(message)s')
console_handler.setFormatter(console_formatter)

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    """
    Handle requests to the root URL.

    Supports GET and POST methods. When a POST request is made, it predicts the
    sentiment of the provided review text and returns the result to be displayed on
    the webpage.

    Returns:
        str: HTML template with sentiment result and review text.
    """
    try:
        sentiment: str = ""
        review_text: str = ""
        if request.method == "POST":
            review_text = request.form["review"]
            sentiment_result = predict_sentiment(review_text)
            sentiment = "positive 😀" if sentiment_result == 1 else "negative 😭"
        return render_template("index.html", sentiment=sentiment, review=review_text)
    except Exception as e:
        app.logger.error('Failed to process request', exc_info=e)
        return "Internal Server Error", 500

def predict_sentiment(text: str) -> int:
    """
    Predict sentiment of a given text using a trained model.

    Args:
        text (str): The input text for which sentiment needs to be predicted.

    Returns:
        int: Predicted sentiment label (0 for negative, 1 for positive).
    """
    # Load model and vectorizer
    model = joblib.load("models/logistic_regression_model.joblib")
    vectorizer = joblib.load("models/vectorizer.joblib")

    # Predict sentiment
    text_vectorized = vectorizer.transform([text])
    return model.predict(text_vectorized)[0]


if __name__ == "__main__":
    app.run(debug=False)
