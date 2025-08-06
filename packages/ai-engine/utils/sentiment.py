from textblob import TextBlob

def detect_sentiment(msg):
    analysis = TextBlob(msg)
    polarity = analysis.sentiment.polarity
    if polarity < -0.3:
        return "angry"
    elif polarity < 0:
        return "sad"
    elif polarity > 0.5:
        return "happy"
    else:
        return "neutral"
