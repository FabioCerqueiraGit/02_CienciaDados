import pandas as pd

class TradingStrategy:
    def __init__(self, data, sentiment_results):
        """
        Inicializa a estratégia de negociação com dados financeiros e resultados de análise de sentimentos.
        
        :param data: DataFrame com dados financeiros
        :param sentiment_results: Lista de dicionários com os resultados de análise de sentimentos
        """
        self.data = data
        self.sentiment_results = sentiment_results
    
    def decide_trade(self):
        """
        Decide se deve comprar, vender ou segurar com base na análise de sentimentos.
        
        :return: String com a decisão de negociação
        """
        # Exemplo simples: se a maioria das notícias for positiva, compra; se negativa, vende.
        positive_count = sum(1 for result in self.sentiment_results if result['label'] == 'POSITIVE')
        negative_count = sum(1 for result in self.sentiment_results if result['label'] == 'NEGATIVE')
        
        if positive_count > negative_count:
            return "BUY"
        elif negative_count > positive_count:
            return "SELL"
        else:
            return "HOLD"

if __name__ == "__main__":
    # Exemplo de uso
    data = pd.read_csv('../data/AAPL_2020-01-01_2023-01-01.csv', index_col='Date', parse_dates=True)
    sentiment_results = [
        {'label': 'POSITIVE', 'score': 0.95},
        {'label': 'NEGATIVE', 'score': 0.85},
        {'label': 'POSITIVE', 'score': 0.90}
    ]
    strategy = TradingStrategy(data, sentiment_results)
    decision = strategy.decide_trade()
    print(f"Decisão de Negociação: {decision}")