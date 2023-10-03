# # 
from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
import os
import openai
import dotenv
dotenv.load_dotenv()



llm = OpenAI()

openai.api_key = os.environ.get('OPENAI_API_KEY')
# llm = OpenAI(openai_api_key="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")
# # chat_model = ChatOpenAI()

# print(f'llm.predict("hi!") {llm.predict("hi!")}')

# # print(f'chat_model.predict("hi!") {chat_model.predict("hi!")}')



from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI()
chat([HumanMessage(content="Translate this sentence from English to French: I love programming.")])