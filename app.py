from flask import Flask, request, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon (only needed once)
nltk.download('vader_lexicon')

# Initialize Flask app and Sentiment Analyzer
app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentiment_scores = sia.polarity_scores(text)
    return jsonify(sentiment_scores)

if __name__ == '__main__':
    app.run(debug=True)
