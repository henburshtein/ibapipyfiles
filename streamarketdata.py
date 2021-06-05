from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum


class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def tickPrice(self, reqId, tickType, price, attrib):
        print("Tick Price. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price:", price, end=' ')

    def tickSize(self, reqId, tickType, size):
        print("Tick Size. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)


def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"


    ##############################
    ##############################
    ## insert the function to try,except, and try to understand why it's not working (even while passing '4' as a variable)
    ##############################
    ##############################
    try:
        app.reqMarketDataType(1)  # switch to delayed-frozen data if live is not available
        app.reqMktData(1, contract, "", False, False, [])
        
    except Exception:
        marketData=0
    
        
    else:
        app.reqMarketDataType(4)  # switch to delayed-frozen data if live is not available
        app.reqMktData(1, contract, "", False, False, [])
        marketData = -1
    
    finally:
        print (marketData)

    # app.reqMarketDataType(4)  # switch to delayed-frozen data if live is not available
    # app.reqMktData(1, contract, "", False, False, [])

    app.run()


if __name__ == "__main__":
    main()


# app.reqMarketDataType(4)  # switch to delayed-frozen data if live is not available
#     app.reqMktData(1, contract, "", False, False, [])
#     # try:
#     #     app.reqMarketDataType(4)  # switch to delayed-frozen data if live is not available
#     #     app.reqMktData(1, contract, "", False, False, [])
#     #     marketData=0
#     # else:
#     #     marketData = -1
#     # print (marketData)