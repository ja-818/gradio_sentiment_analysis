from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Model logic
def predict(user_input):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(user_input)
    prediction = ""
    
    # Stablish prediction according to polarity score
    if sentiment_dict['compound'] >= 0.05 :
        prediction = "Positive"

    elif sentiment_dict['compound'] <= - 0.05 :
        prediction = "Negative"

    else :
        prediction = "Neutral"  

    return prediction