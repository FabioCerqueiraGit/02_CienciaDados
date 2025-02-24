from data_loader import load_financial_data
from sentiment_analysis import analyze_sentiment
from trading_strategy import TradingStrategy

def main():
    # Coleta de dados financeiros
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    data = load_financial_data(ticker, start_date, end_date)
    
    # Análise de sentimentos (exemplo com notícias fictícias)
    news_articles = [
        "Apple announces record profits for the quarter.",
        "Market crashes due to unexpected economic downturn.",
        "Tech stocks rise as investors gain confidence."
    ]
    sentiment_results = analyze_sentiment(news_articles)
    
    # Estratégia de negociação
    strategy = TradingStrategy(data, sentiment_results)
    decision = strategy.decide_trade()
    print(f"Decisão de Negociação: {decision}")

if __name__ == "__main__":
    main()