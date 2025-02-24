from src.data_loader import load_data
from src.sentiment_analysis import analyze_sentiment
from src.trading_strategy import execute_strategy

def main():
    print("Carregando dados financeiros...")
    data = load_data()
    
    print("Analisando sentimentos...")
    sentiment = analyze_sentiment(data)
    
    print("Executando estratégia de trading...")
    execute_strategy(sentiment)
    
if __name__ == "__main__":
    main()
