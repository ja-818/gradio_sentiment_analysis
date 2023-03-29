import gradio as gr
from model import predict

# Main app function
def model_predict(sentence):
    prediction = predict(sentence)
    return prediction

# Create gradio app structure
app = gr.Interface(fn=model_predict, inputs="text", outputs="text")

# Launch gradio app
app.launch()