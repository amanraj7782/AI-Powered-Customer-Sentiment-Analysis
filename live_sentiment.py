from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# Import VADER's sentiment analyzer to analyze text emotion

# Create an object of SentimentIntensityAnalyzer
# This object will calculate sentiment scores
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    """
    This function takes a review (text) as input
    and returns whether the sentiment is
    Positive, Negative, or Neutral
    """

    # Get sentiment scores for the given text
    # It returns a dictionary with keys:
    # positive, negative, neutral, and compound
    score = analyzer.polarity_scores(text)

    # 'compound' score represents overall sentiment
    # Range: -1 (most negative) to +1 (most positive)
    compound = score["compound"]

    # Decide sentiment based on compound score
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Take live review input from the user
review = input("Enter your review: ")

# Analyze sentiment of the entered review
sentiment = get_sentiment(review)

# Display the final sentiment result
print("\nSentiment:", sentiment)
