from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum
from threading import Timer
from threading import *
import csv

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def tickPrice(self, reqId, tickType, price, attrib):
        #print("Tick Price. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price:", price, end=' ')
        f = open("highprice.csv","a", newline="")
        tup1 = ("high: ", reqId, " ", TickTypeEnum.to_str(tickType), " ", price)
        writer = csv.writer(f)
        writer.writerow(tup1)
        f.close()

    def tickSize(self, reqId, tickType, size):
        print("high: ", reqId, " ", tickType, " ", size)

 

    def start(self):
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.primaryExchange = "NASDAQ"

        self.reqMarketDataType(3)
        self.reqMktData(6, contract, "", False, False, [])
    
    def stop(self):        
        self.done = True
        self.disconnect() 

def main():
    app = TestApp()
    app.nextOrderId = 0
    app.connect("127.0.0.1", 7497, 0)

    Timer(3, app.stop).start()
    app.run()

if __name__ == "__main__":
    main()