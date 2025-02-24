import yfinance as yf

def load_data(ticker="AAPL", period="7d", interval="1h"):
    """
    Coleta dados históricos de um ativo usando Yahoo Finance.
    
    :param ticker: Código do ativo (ex: "AAPL" para Apple).
    :param period: Período dos dados (ex: "7d" para 7 dias).
    :param interval: Intervalo entre os dados (ex: "1h" para 1 hora).
    :return: DataFrame com os dados históricos.
    """
    print(f"Baixando dados para {ticker}...")
    data = yf.download(ticker, period=period, interval=interval)
    return data
