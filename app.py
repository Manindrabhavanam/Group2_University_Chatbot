from transformers import pipeline
import gradio as gr

chatbot = pipeline(
    "text-generation",
    model="gpt2"
)

def respond(message):
    result = chatbot(
        message,
        max_length=80,
        num_return_sequences=1,
        truncation=True
    )

    response = result[0]["generated_text"]

    return response

interface = gr.Interface(
    fn=respond,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask a university-related question..."
    ),
    outputs="text",
    title="University Student Support Chatbot",
    description="AI-powered chatbot using Hugging Face and Gradio"
)

interface.launch()