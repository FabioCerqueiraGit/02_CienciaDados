import yfinance as yf
import pandas as pd
import os

def load_financial_data(ticker, start_date, end_date, data_dir='../data'):
    """
    Carrega dados financeiros usando yfinance e salva em um arquivo CSV.
    
    :param ticker: Símbolo do ativo (ex: 'AAPL')
    :param start_date: Data de início no formato 'YYYY-MM-DD'
    :param end_date: Data de término no formato 'YYYY-MM-DD'
    :param data_dir: Diretório para salvar os dados
    :return: DataFrame com os dados financeiros
    """
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    data = yf.download(ticker, start=start_date, end=end_date)
    file_path = os.path.join(data_dir, f'{ticker}_{start_date}_{end_date}.csv')
    data.to_csv(file_path)
    
    return data

if __name__ == "__main__":
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    data = load_financial_data(ticker, start_date, end_date)
    print(data.head())