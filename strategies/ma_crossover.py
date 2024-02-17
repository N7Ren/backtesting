import backtrader as bt

class MACrossover(bt.Strategy):

    def __init__(self):
        self.short_ma = bt.indicators.SMA(period=50)
        self.long_ma = bt.indicators.SMA(period=200)
        self.crossover = bt.indicators.CrossOver(self.short_ma, self.long_ma)

    def next(self):
        if self.crossover > 0: 
            self.close()
            self.buy()
        elif self.crossover < 0:  
            self.close() 
            self.sell()  
