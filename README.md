# Sentiment Analysis API using NLTK's VADER

## Overview
This project is a **Flask API** that performs **sentiment analysis** using **NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner)**. It determines whether a given text is **positive, negative, or neutral** based on predefined lexicon-based sentiment scores.

## Features
- **Rule-based sentiment analysis** using NLTK's VADER.
- **REST API** built with Flask for easy integration.
- **JSON-based input and output** for seamless communication.
- **Bonus:** Sentiment trend visualization using Matplotlib or Seaborn.

## Technologies Used
- **Python**
- **Flask** (for API development)
- **NLTK** (for sentiment analysis)
- **Matplotlib/Seaborn** (optional, for visualization)

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed.

### 1. Clone the Repository
```bash
git clone https://github.com/fatma20010/sentiment-analysis-tool-using-NLTK-s-VADER.git
cd sentiment-analysis-tool-using-NLTK-s-VADER
```

### 2. Create a Virtual Environment 
```bash
conda create -n sentiment_analysis
conda activate sentiment_analysis
```

### 3. Install Dependencies

### 4. Run the Flask API
```bash
python app.py
```
By default, the API runs on `http://127.0.0.1:5000`.

## API Usage
### Endpoint: `/analyze`
- **Method:** `POST`
- **Request Format:** JSON
- **Request Body:**
```json
{
  "text": "I love this product!"
}
```
- **Response:** JSON with sentiment scores
```json
{
  "neg": 0.0,
  "neu": 0.254,
  "pos": 0.746,
  "compound": 0.8316
}
```

### Example cURL Request
```bash
curl -X POST "http://127.0.0.1:5000/analyze" -H "Content-Type: application/json" -d '{"text": "I love this product!"}'
```

## Optional: Sentiment Trend Visualization
You can extend this project by analyzing multiple texts and visualizing sentiment trends using **Matplotlib** or **Seaborn**.

## Future Improvements
- Add support for **multilingual sentiment analysis**.
- Implement **deep learning models** (BERT, LSTMs) for better accuracy.
- Deploy the API on **Heroku, AWS, or Render** for public use.

## Contributing
Feel free to **fork** this repository and submit **pull requests**. Any improvements or bug fixes are welcome!


