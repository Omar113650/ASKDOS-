import gradio as gr
import requests

BACKEND_URL = "http://localhost:8000"

def upload_file(file):
    with open(file.name, "rb") as f:
        files = {"file": (file.name, f.read(), "application/octet-stream")}
        response = requests.post(f"{BACKEND_URL}/upload", files=files)
    return response.json()["message"]

def chat_fn(message, history):
    response = requests.post(f"{BACKEND_URL}/rag/invoke", json={"input": {"question": message}})
    return response.json()["output"]

with gr.Blocks() as demo:

    gr.Markdown("<h1> Smart Contract Q&A Assistant</h1>", elem_id="title")


    with gr.Column():
        gr.Markdown("### Upload your contract file")
        file_input = gr.File(file_types=[".pdf", ".docx"], label="Select File")
        upload_btn = gr.Button("Process Document")
        upload_output = gr.Textbox(label="Result", interactive=False)
        upload_btn.click(upload_file, inputs=file_input, outputs=upload_output)


    gr.Markdown("### Ask questions about your uploaded contract")
    gr.ChatInterface(
        fn=chat_fn,
        title="Contract Chat",
        description="Type your question below:",
    )


demo.launch(css="""
    body {background-color: #f0f2f5; font-family: 'Arial';}
    h1 {color: #2c3e50; text-align: center;}
    .gr-button {background-color: #2c3e50; color: white; border-radius: 8px; font-weight: bold; margin-top: 10px;}
    .gr-file {border-radius: 8px; border: 2px dashed #2c3e50; padding: 10px; background-color: #ffffff;}
    .gr-chat-interface .message.user {background-color: #4e73df; color: white; border-radius: 15px 15px 0 15px; padding: 8px;}
    .gr-chat-interface .message.bot {background-color: #ecf0f1; color: #2c3e50; border-radius: 15px 15px 15px 0; padding: 8px;}
    .gr-chat-interface {border: 2px solid #2c3e50; border-radius: 12px; padding: 10px; background-color: #ffffff;}
""")




























