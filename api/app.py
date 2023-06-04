from flask import Flask

from src.main import llm_service

app = Flask(__name__)


# Service that process the message with the user message
@app.route("/chatbot_service/<message>")
def chatbot_service(message):
    # Call the service
    return llm_service(message)


# Main driver function, run API server
if __name__ == "__main__":
    from waitress import serve

    print("API server listening on 0.0.0.0:5010")
    serve(app, host="0.0.0.0", port=5010)
