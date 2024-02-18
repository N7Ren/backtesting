import backtrader as bt

class RSI(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))


    def __init__(self):
        self.rsi = bt.indicators.RSI(period=14)  # Calculate RSI with period 14

    def next(self):

        if self.rsi < 30:  # Buy when RSI goes below 30
            if self.position:
                self.log('POSITION BEFORE BUY CLOSE, %.2f' % self.position.size)
                self.close()
                self.log('POSITION AFTER BUY CLOSE, %.2f' % self.position.size)

            self.log('POSITION BEFORE BUY CREATE, %.2f' % self.position.size)
            self.buy()
            self.log('POSITION BEFORE BUY CREATE, %.2f' % self.position.size)
        elif self.rsi > 70:  # Sell when RSI goes above 70
            if self.position:
                self.log('POSITION BEFORE SELL CLOSE, %.2f' % self.position.size)
                self.close()
                self.log('POSITION AFTER SELL CLOSE, %.2f' % self.position.size)

            self.log('POSITION BEFORE SELL CREATE, %.2f' % self.position.size)
            self.sell()
            self.log('POSITION AFTER SELL CREATE, %.2f' % self.position.size)
