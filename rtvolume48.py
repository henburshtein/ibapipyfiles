from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum
from threading import *
from threading import Timer
import csv

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId ):
        self.nextOrderId = orderId
        self.start()
        
    def tickPrice(self, reqId, tickType, price, attrib):
        print("Tick Price. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price:", price, end=' ')

   # def tickSize(self, reqId, tickType, size):
    #   print("rt volume: ", reqId, " ", tickType, " ", size)
    def tickString(self, reqId, tickType ,value):
        print("rt volume. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "rtvolume", value, end=' ')
        f = open("RTvolume.csv","a", newline="")
        tup1 = ("RT Volume: ", reqId, " ", TickTypeEnum.to_str(tickType), " ", value)
        writer = csv.writer(f)
        writer.writerow(tup1)
        f.close() 

    def start(self):
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.primaryExchange = "NASDAQ"

        self.reqMarketDataType(3)
        self.reqMktData(48, contract, "233", False, False, [])
    
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