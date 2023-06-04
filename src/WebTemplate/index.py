import time
import gradio as gr
import requests

# Create the web chatbot
with gr.Blocks() as demo:
    gr.Markdown("<h3><center>Insurance Policy Generation Chatbot</center></h3>")
    chatbot = gr.Chatbot([], label="Insurance ChatBot").style(height=400)
    msg = gr.Textbox(show_label=False)
    clear = gr.Button(
        "Limpiar chat",
    )

    # Function that receive the send the user message and receive the IA message from the API
    def respond(message, chat_history):
        # Request Flask API passing the message as argument
        api_url = "http://localhost:5010/chatbot_service/" + message
        response = requests.get(api_url)

        bot_message = response.text
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history

    # When user press enter, respond function will executed
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

# Launch server in port 5050
demo.launch(server_name="0.0.0.0", server_port=5050)
