import gradio as gr
from model import predict

def model_predict(input):
    output = predict(input)
    return output

with gr.Blocks() as demo:
    gr.Markdown("This app analyses a review to determine if it's positive, negative, or neutral")
    input = gr.Textbox(label="Review", placeholder="Write a review...")
    output = gr.Textbox(label="Prediction")
    btn = gr.Button("Analyze the sentiment!")
    btn.click(fn=model_predict, inputs=input, outputs=output)

demo.launch()