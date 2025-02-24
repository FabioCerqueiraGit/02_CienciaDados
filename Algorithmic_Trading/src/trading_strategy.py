def execute_strategy(sentiment_data):
    """
    Executa uma estratégia de trading com base nos sentimentos analisados.
    
    :param sentiment_data: Lista de dicionários contendo sentimentos e scores.
    """
    print("Executando estratégia de trading...")
    
    for entry in sentiment_data:
        sentiment = entry["label"].upper()
        score = entry["score"]
        
        if sentiment == "POSITIVE" and score > 0.9:
            print("🔼 Sinal de COMPRA gerado.")
        elif sentiment == "NEGATIVE" and score > 0.9:
            print("🔽 Sinal de VENDA gerado.")
        else:
            print("➖ Nenhum sinal claro detectado.")
