import gradio as gr

def my_function(input_text):
    # Your machine learning model logic here
    return "Model Output: " + input_text

iface = gr.Interface(fn=my_function, inputs="text", outputs="text")
iface.launch()

