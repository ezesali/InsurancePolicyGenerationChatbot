import os

import pinecone
from decouple import config
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferWindowMemory
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone

from utils.dataset_loader import dataset_loader

from src.indexed_dataset import dataset_docs



def llm_service(message):
    # Loading dataset
    docsearch = dataset_docs

    # OpenAI LLM
    llm = ChatOpenAI(
        openai_api_key=config("OPENAI_API_KEY"),
        model_name="gpt-3.5-turbo",
        temperature=0.2,
    )

    # QA Chain which take the vector store and generates an answer.
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(search_kargs={"k": 2}),
    )

    # Prompt for the agent
    PREFIX = """Sos un IA experto en polizas de seguro de una empresa en especifico. Sos amigable y conversacional. Una IA sincera sobre todo.
    Si la IA no sabe que responder no intenta generar una respuesta sino que sinceramente contesta "No tengo informacion sobre lo que me dices, puedes hacerme otra pregunta si lo deseas?"""

    FORMAT_INSTRUCTIONS = """Para usar esta herramienta, por favor usa el siguiente formato:
    '''
    Pensamiento: Tengo que usar esta herramienta? Si
    Accion: La accion para tomar, es alguna de estas herramientas: [{tool_names}]
    Pregunta de la accion: La pregunta de la accion
    Observacion: El resultado de la accion
    '''

    Si te falta informacion sobre la pregunta, podes manifestarle que especifique mas informacion haciendole otra pregunta.

    '''
    Pensamiento: Tengo que usar la herrmaienta? No
    AI: [Responde que le haga una pregunta sobre las polizas de seguro]
    '''
    """

    SUFFIX = """

    Empieza!

    Historial de conversacion anterior:
    {chat_history}

    Instrucciones: {input}
    {agent_scratchpad}
    """

    # Set conversational buffer window memory
    conversational_memory = ConversationBufferWindowMemory(
        memory_key="chat_history",
        k=5,
        return_messages=True,
        human_prefix="Usuario",
        ai_prefix="IA",
    )

    # Create tool which execute QA Chain and only have to use if there are some insurance questions
    tools = [
        Tool(
            name="Insurance Knowledge Base",
            func=qa.run,
            description=(
                "Usa esta herramienta cuando el usuario quiere saber sobre polizas de seguro y sobre "
                "el contexto que fue provisto sobre la compania de seguros. "
                "Quiero que contestes como una conversacion amigable entre un usuario y un asistente de IA experto en polizas de seguro. La IA es conversacional y provee un monton de informacion acerca de su contexto."
                'Si la IA no sabe que responder no intenta generar una respuesta sino que sinceramente contesta "No tengo mucha informacion sobre lo que me dices, puedes proveerme mas informacion por favor?'
            ),
        )
    ]

    # Inicialize the agent that going to think and return the answer
    agent = initialize_agent(
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        tools=tools,
        llm=llm,
        verbose=True,
        max_iterations=3,
        early_stopping_method="generate",
        memory=conversational_memory,
    )

    # Return output message
    return agent(message).get("output")
