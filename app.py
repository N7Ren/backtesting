import os
from dotenv import load_dotenv
import backtrader as bt
import yfinance as yf
import quandl

from strategies.ma_crossover import MACrossover
from strategies.rsi import RSI

quandl.ApiConfig.api_key = '<insert-quandl-api-key>'

if __name__ == '__main__':
    #load_dotenv()
    #quandl_api_key = os.getenv("QUANDL_API_KEY")

    data = bt.feeds.PandasData(dataname=yf.download("AAPL", 
                                            start="2023-01-01", 
                                            end="2023-12-31"))

    #dataset_code = 'WIKI/AAPL'  # Example for Apple stock data
    #data = bt.feeds.QuandlData(dataname=dataset_code)
    #data = bt.feeds.QuandlData(dataname=dataset_code, start="2020-01-01", end="2023-12-31")

    cerebro = bt.Cerebro()
    cerebro.adddata(data)

    #cerebro.addstrategy(MACrossover)
    cerebro.addstrategy(RSI)

    cerebro.broker.setcash(10000)

    cerebro.run()

    print(f"Final Portfolio Value: {cerebro.broker.getvalue()}")

    cerebro.plot()
