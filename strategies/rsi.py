import backtrader as bt

class RSI(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(period=14)  # Calculate RSI with period 14

    def next(self):
        if self.rsi < 30:  # Buy when RSI goes below 30
            self.close()
            self.buy()
        elif self.rsi > 70:  # Sell when RSI goes above 70
            self.close()
            #self.sell()
