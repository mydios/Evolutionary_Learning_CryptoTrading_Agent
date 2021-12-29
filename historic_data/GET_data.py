import json
from typing import List

from binance.client import Client
import pandas as pd
from tqdm import tqdm

with open('../secrets.json', 'r') as file_to_read:
    json_data = json.load(file_to_read)
    api_key = json_data['API_KEY']
    api_secret = json_data['API_SECRET']

print(api_key)

client = Client(api_key, api_secret)

tickers: List[str] = ['BTC', 'ETH', 'BNB']
start_date: str = "01/01/2018"

for coin in tqdm(tickers):
    ticker = coin + 'USDT'
    binance_data: List[List] = \
        client.futures_historical_klines(ticker, Client.KLINE_INTERVAL_5MINUTE, start_str=start_date)
    df: pd.DataFrame = pd.DataFrame(binance_data)
    df.columns = ['Open time',
                  'Open',
                  'High',
                  'Low',
                  'Close',
                  'Volume',
                  'Close time',
                  'Quote asset volume',
                  'Number of trades',
                  'Taker buy base asset volume',
                  'Taker buy quote asset volume',
                  'Ignore']
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')
    time_start = str(min(df['Close time'])).split(' ')[0].replace('-', '')
    df.to_feather(f'/historic_data/{ticker}_since_{time_start}.ftr')
