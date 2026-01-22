# Import pandas library
# Pandas is used to read CSV files and perform data analysis
import pandas as pd

# Import VADER Sentiment Analyzer
# This library is used to calculate sentiment scores of text
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# -------------------- LOAD MANUALLY LABELED DATA --------------------

# Load the manually labeled dataset
# This file contains review text and the actual sentiment assigned manually
data = pd.read_csv("manual_test.csv")


# -------------------- INITIALIZE SENTIMENT ANALYZER --------------------

# Create an object of SentimentIntensityAnalyzer
# This object will predict sentiment for each review
analyzer = SentimentIntensityAnalyzer()


# -------------------- SENTIMENT PREDICTION FUNCTION --------------------

# Define a function to predict sentiment using VADER
def predict_sentiment(text):
    """
    Takes a review text as input
    Returns sentiment as Positive, Negative, or Neutral
    """

    # Convert review text to string and get sentiment scores
    score = analyzer.polarity_scores(str(text))

    # Extract compound score (overall sentiment score)
    compound = score["compound"]

    # Classify sentiment based on compound score thresholds
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"


# -------------------- APPLY SENTIMENT PREDICTION --------------------

# Apply sentiment prediction on each review in the Text column
# Store predicted sentiment in a new column
data["Predicted_Sentiment"] = data["Text"].apply(predict_sentiment)


# -------------------- COMPARE PREDICTION WITH ACTUAL LABELS --------------------

# Compare predicted sentiment with manually labeled sentiment
# This creates a True/False column indicating correct predictions
data["Correct"] = data["Actual_Sentiment"] == data["Predicted_Sentiment"]


# -------------------- CALCULATE ACCURACY --------------------

# Calculate accuracy as the percentage of correct predictions
accuracy = data["Correct"].mean() * 100


# -------------------- DISPLAY RESULTS --------------------

# Print overall accuracy
print("Accuracy:", round(accuracy, 2), "%")

# Print detailed comparison of actual vs predicted sentiment
print("\nPrediction Summary:")
print(data[["Actual_Sentiment", "Predicted_Sentiment"]].value_counts())


# -------------------- SAVE RESULTS --------------------

# Save the detailed accuracy comparison to a CSV file
# This file can be used as proof of validation
data.to_csv("accuracy_results.csv", index=False)
