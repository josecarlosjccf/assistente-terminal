import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

class ChatBot:
    def __init__(self, model_name, api_key_env_var):
        load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
        self.api_key = os.getenv(api_key_env_var)
        self.client = ChatGroq(model_name=model_name, api_key=self.api_key)
        
        # Configurações do prompt
        self.template = """Você é um assistente virtual.
Responda apenas em Português.
Input: {input}"""
        self.base_prompt = PromptTemplate(
            input_variables=["input"],
            template=self.template
        )
        
        # Configuração do LLM e memória
        self.llm = ChatGroq(model_name=model_name)
        self.memory = ConversationBufferMemory(memory_key="chat_history", input_key='input')
        self.llm_chain = LLMChain(llm=self.llm, prompt=self.base_prompt, verbose=True, memory=self.memory)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def get_response(self, user_input):
        return self.llm_chain.run(user_input)
    
    def run(self):
        self.clear_screen()
        print("Bem-vindo ao chat! Digite 'sair' para encerrar.")
        user_input = input("Você: ")
        while user_input.lower() != 'sair':
            response = self.get_response(user_input)
            print(f"Assistente: {response}")
            user_input = input("Você: ")
        print("Assistente: Até logo!")

if __name__ == "__main__":
    chatbot = ChatBot(model_name="llama3-8b-8192", api_key_env_var="GROQ_API_KEY")
    chatbot.run()
