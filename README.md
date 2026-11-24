# Langchain-Demo

This is the project for the Langchain-demo

we need to install uv
pip3 install uv

and also add langchain

uv add langchain
uv add langchain-openai
uv add python-dotenv


pip install -U langchain-google-genai


install ollama in local
and then install the model 
ollama pull gemma3:270m

ollama list
NAME           ID              SIZE      MODIFIED
gemma3:270m    e7d36fb2c3b3    291 MB    33 seconds ago

to run in local
ollama run gemma3:270m