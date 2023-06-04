# AnyOne Final Project - Group 5
> Insurance Policy Generation Chatbot

## The Business problem

The underwriting process, also known as risk assessment, is an essential process in the insurance and finance industry. It involves evaluating and analyzing the risks associated with a client or insurance application to determine whether a policy is accepted or rejected, and if accepted, to establish the appropriate conditions and premiums.

A general policy is a type of insurance contract that covers a wide range of risks, providing protection to a group of people or businesses. These policies are more standardized and offer coverage based on common and general risks.

In the insurance industry, the process of generating new policies or documents can be time-consuming and tedious. To optimize this process, we can use AI-powered chatbots that act as assistants and advisors to insurance companies during the policy creation process. These chatbots can help streamline the process and provide reliable and accurate information to customers.

In this project, you will create a chatbot that assists insurance companies. The chatbot will use ChatGPT to generate answers to questions related to insurance policies and will have access to a database of previous policies to efficiently generate new ones. Additionally, the chatbot will be able to search the internet for the latest news related to insurance companies and policies and create a summary of the most relevant information for the user.

## Technical aspects

To develop this solution you will need to have a proper working environment setup in your machine consisting of:
- Docker
- VS Code or any other IDE of your preference

The technologies involved are:
- Python is the main programming language
- Flask framework for the API
- Gradio Library for the web UI (Running locally)
- Langchaing for process policies documents and run the NLP service
- ChatGPT for generate the answer
- Pinecone VectorDB for save the documents embedding data as vectors
- Docker to run Flask API

## Code Style

Following a style guide keeps the code's aesthetics clean and improves readability, making contributions and code reviews easier. Automated Python code formatters make sure your codebase stays in a consistent style without any manual work on your end. If adhering to a specific style of coding is important to you, employing an automated to do that job is the obvious thing to do. This avoids bike-shedding on nitpicks during code reviews, saving you an enormous amount of time overall.

We use [Black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/) for automated code formatting in this project, you can run it with:

```console
$ isort --profile=black . && black --line-length 88 .
```

Wanna read more about Python code style and good practices? Please see:
- [The Hitchhiker’s Guide to Python: Code Style](https://docs.python-guide.org/writing/style/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

#### 1. Api

Run:

```bash
$ docker build -t chatbot_flask_api .
$ docker run --name=insurance_chatbot_api -p 0.0.0.0:5010:5010/tcp -e PYTHONUNBUFFERED=1 -d chatbot_flask_api
```

#### 2. Gradio

Run:

```bash
$ cd src/WebTemplate
$ python3 index.py
```


There going to open in http://localhost:5050/ the chatbot to interact with.

And ready to ask the chatbot anything about the insurance policies