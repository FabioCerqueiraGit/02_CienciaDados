from langchain.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def analyze_sentiment(news_articles):
    """
    Analisa o sentimento de uma lista de notícias usando um modelo da Hugging Face integrado ao LangChain.
    
    :param news_articles: Lista de strings contendo as notícias
    :return: Lista de dicionários com o sentimento e a pontuação
    """
    # Carrega o pipeline de análise de sentimentos da Hugging Face
    sentiment_pipeline = pipeline("sentiment-analysis")
    
    # Integra o pipeline ao LangChain
    llm = HuggingFacePipeline(pipeline=sentiment_pipeline)
    
    # Define um template de prompt para análise de sentimentos
    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="Analyze the sentiment of the following text: {text}"
    )
    
    # Cria uma cadeia (chain) para processar o texto
    sentiment_chain = LLMChain(llm=llm, prompt=prompt_template)
    
    # Analisa cada notícia
    results = []
    for article in news_articles:
        result = sentiment_chain.run(article)
        results.append(result)
    
    return results

if __name__ == "__main__":
    # Exemplo de uso
    news = [
        "Apple announces record profits for the quarter.",
        "Market crashes due to unexpected economic downturn.",
        "Tech stocks rise as investors gain confidence."
    ]
    sentiment_results = analyze_sentiment(news)
    for i, result in enumerate(sentiment_results):
        print(f"Notícia {i+1}: {result}")