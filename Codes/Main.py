import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

class StocksNSE():


    def setStockSymbol(self, sym):
        self.stockSymbol = sym

    def getData(self):
        self.path = os.path.abspath(os.path.dirname(__file__))
        self.datapath = os.path.join(self.path, '..', 'Data', '26-08-2016-TO-26-08-2017ITCALLN.csv')
        self.data = pd.read_csv(self.datapath)

    def getDailyReturns(self):
        closePriceData = self.data['Close Price']
        closePriceData = [float(x) for x in closePriceData]
        a = np.array(closePriceData[1:], dtype = np.float)
        b = np.array(closePriceData[:-1], dtype = np.float)
        #print (a/b)
        self.dailyRet = (a/b) - 1
        #plt.plot(self.dailyRet)
        #plt.show()
        print (self.dailyRet)

    def getCumulativeReturn(self):
        print ('Cumulative Return')
        print ( (float(self.data['Close Price'].iloc[-1])/float(self.data['Close Price'].iloc[0])) - 1 )

def main():
    Stock1 = StocksNSE()
    Stock1.setStockSymbol('ITC')
    Stock1.getData()
    Stock1.getDailyReturns()
    Stock1.getCumulativeReturn()

if __name__ == '__main__':
    main()
