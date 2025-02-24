from transformers import pipeline

def analyze_sentiment(texts):
    """
    Analisa o sentimento de uma lista de textos usando um modelo da Hugging Face.
    
    :param texts: Lista de strings contendo os textos a serem analisados.
    :return: Lista de dicionários com os resultados da análise de sentimento.
    """
    sentiment_pipeline = pipeline("sentiment-analysis")
    results = sentiment_pipeline(texts)
    return results
