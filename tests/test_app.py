import unittest
from unittest.mock import patch
from flask_testing import TestCase
from app import app, predict_sentiment

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('app.joblib')
    def test_predict_sentiment(self, mock_joblib):
        # Mock the loaded model and vectorizer
        mock_model = mock_joblib.load.return_value
        mock_model.predict.return_value = [1]

        result = predict_sentiment("It was pretty good")
        self.assertEqual(result, 1)

        mock_model.predict.return_value = [0]
        result = predict_sentiment("It was pretty bad")
        self.assertEqual(result, 0)

    def test_predict_sentiment_post(self):
        response = self.client.post('/', data={"review": "This is a good review"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The model determined your review to be positive', response.data)

if __name__ == '__main__':
    unittest.main()
