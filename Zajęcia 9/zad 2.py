import gradio as gr
from transformers import pipeline

# Ładujemy model klasyfikacyjny
classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-sms-spam-detection")

def classify_email(text):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    return f"{label} ({score:.2f})"

iface = gr.Interface(
    fn=classify_email,
    inputs=gr.Textbox(lines=10, placeholder="Wklej treść e-maila tutaj..."),
    outputs="text",
    title="Spam Detector",
    description="Klasyfikacja wiadomości e-mail jako spam lub nie-spam."
)

iface.launch()
