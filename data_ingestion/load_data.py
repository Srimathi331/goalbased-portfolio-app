import yfinance as yf
import pandas as pd

def fetch_data(tickers, start="2020-01-01", end="2025-01-01"):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)['Close']
    data.to_csv("prices.csv")
    return data

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    df = fetch_data(tickers)
    print(df.tail())
