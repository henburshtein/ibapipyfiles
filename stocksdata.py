from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum
from threading import Timer
from threading import *
import csv
import storage_handler as sh

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId ):
        self.nextOrderId = orderId
        self.start()

    def tickPrice(self, reqId, tickType, price, attrib):
        group = [1, 2, 4, 6, 7, 35, 37, 57, 75]
        i = 0
        while i < len(group):
            if reqId == group[i]:
                print(str(reqId), reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price:", price, end=' ')
                f = open(str(reqId) + ".csv","a", newline="")
                tup1 = (str(reqId) + ": ", reqId, " ", TickTypeEnum.to_str(tickType), " ", price)
                sh.csvhandler(self, f, tup1)
            i += 1

    def tickSize(self, reqId, tickType, size):
        group = [0, 3, 5, 8, 21, 34, 63, 64, 65, 89]
        i = 0
        while i < len(group):
            if reqId == group[i]:
               f = open(str(reqId) + ".csv","a", newline="")
               tup1 = (str(reqId) + ": ", reqId, " ", TickTypeEnum.to_str(tickType), " ", size)
               sh.csvhandler(self, f, tup1)
            i += 1

    
    def tickGeneric(self, redId, tickType, value):
        group = [46, 49, 54, 55, 56, 58]
        i = 0
        while i < len(group):
            if reqId == group[i]:
                print("halted:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "value:", value)
                f = open(str(reqId) + ".csv","a", newline="")
                tup1 = (str(reqId) + ": ", reqId, " ", TickTypeEnum.to_str(tickType), " ", value)
                sh.csvhandler(self, f, tup1)
            i += 1

    def tickString(self, reqId, tickType, value):
        group = [48, 62, 85]
        i = 0
        while i < len(group):
            if reqId == group[i]:
                f = open(str(reqId) + ".csv","a", newline="")
                tup1 = (str(reqId) + ": ", reqId, " ", TickTypeEnum.to_str(tickType), " ", value)
                sh.csvhandler(self, f, tup1)
            i += 1
 
    def start(self):
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.primaryExchange = "NASDAQ"

        self.reqMarketDataType(3)
        #app.reqMktData(0, contract, "", False, False, [])
        #app.reqMktData(1, contract, "", False, False, [])
        self.reqMktData(2, contract, "", False, False, [])
        self.reqMktData(3, contract, "", False, False, [])
        #app.reqMktData(4, contract, "", False, False, [])
        self.reqMktData(49, contract, "", False, False, [])
        self.reqMktData(85, contract, "", False, False, [])
    
    def stop(self):        
        self.done = True
        self.disconnect() 

def main():
    app = TestApp()
    app.nextOrderId = 0
    app.connect("127.0.0.1", 7497, 0)

    Timer(4, app.stop).start()
    app.run()

if __name__ == "__main__":
    main()