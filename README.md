# AI-Powered Customer Sentiment Analysis

## 📌 Project Overview
This project analyzes customer reviews using Natural Language Processing (NLP) techniques to determine whether the sentiment of a review is **Positive**, **Negative**, or **Neutral**.  
The project also identifies common customer complaint areas (service gaps) and evaluates model accuracy using manually labeled data.

---

## 🎯 Objectives
- Analyze customer reviews using sentiment analysis
- Classify sentiments into Positive, Negative, and Neutral
- Perform real-time sentiment prediction
- Identify service gaps from negative feedback
- Validate model accuracy using manual labeling

---

## 🛠️ Technologies Used
- **Python**
- **Pandas** (Data handling)
- **NLTK / VADER Sentiment Analyzer**
- **CSV datasets**
- **VS Code**

---

## 📂 Project Structure
Customer_Sentiment_Analysis/
│
├── sentiment_analysis.py # Main sentiment analysis script
├── live_sentiment.py # Real-time sentiment prediction
├── accuracy_check.py # Accuracy calculation using manual labels
├── service_gap_analysis.py # Service gap identification
│
├── reviews.csv # Cleaned customer reviews dataset
├── sentiment_output.csv # Reviews with predicted sentiment
├── manual_test.csv # Manually labeled validation data
├── accuracy_results.csv # Accuracy comparison output
├── service_gaps.csv # Identified service gaps
│
└── README.md


---

## ⚙️ How the Project Works

### 1️⃣ Sentiment Analysis
- Customer reviews are loaded from a CSV file
- VADER sentiment analyzer calculates sentiment scores
- Reviews are classified as Positive, Negative, or Neutral
- Output is saved as `sentiment_output.csv`

### 2️⃣ Real-Time Sentiment Prediction
- User enters a review in the terminal
- The system instantly predicts sentiment

### 3️⃣ Accuracy Evaluation
- 50 reviews are manually labeled
- Model predictions are compared with actual labels
- Accuracy is calculated and saved in `accuracy_results.csv`

### 4️⃣ Service Gap Identification
- Negative reviews are analyzed
- Common complaint keywords are extracted
- Frequent issues are saved in `service_gaps.csv`

---

## ▶️ How to Run the Project

### Install required libraries
```bash
pip install pandas nltk vaderSentiment

Run sentiment analysis
python sentiment_analysis.py

Run live sentiment prediction
python live_sentiment.py

Run accuracy calculation
python accuracy_check.py

Run service gap analysis
python service_gap_analysis.py


📊 Sample Output

Positive reviews: Majority

Negative reviews: Identified for complaint analysis

Accuracy: ~90% (rule-based NLP model)


🧠 Key Learnings

Practical use of NLP for text analysis

Understanding sentiment scoring and polarity

Model validation using manual labeling

Extracting business insights from customer feedback


🚀 Future Improvements

Use machine learning models for higher accuracy

Add web interface using Flask

Improve neutral sentiment handling

Support multilingual sentiment analysis