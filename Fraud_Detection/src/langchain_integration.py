from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate

# Configurar o modelo da Hugging Face
llm = HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature":0, "max_length":64})

# Definir o template de prompt
template = """Você é um assistente de detecção de fraudes. Analise a seguinte transação e forneça uma recomendação:
Transação: {transaction}
Recomendação:"""
prompt = PromptTemplate(template=template, input_variables=["transaction"])

# Criar a cadeia de processamento
chain = LLMChain(llm=llm, prompt=prompt)

# Função para obter recomendação
def get_recommendation(transaction):
    return chain.run(transaction=transaction)

# Exemplo de uso
transaction = "1000,5000,4000,10000,11000"
recommendation = get_recommendation(transaction)
print(f'Recomendação: {recommendation}')