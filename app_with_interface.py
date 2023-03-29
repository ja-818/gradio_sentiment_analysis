import gradio as gr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Main app function
def model_predict(sentence):
    prediction = predict(sentence)
    return prediction

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

# Create gradio app structure
app = gr.Interface(fn=model_predict, inputs="text", outputs="text")

# Launch gradio app
app.launch()