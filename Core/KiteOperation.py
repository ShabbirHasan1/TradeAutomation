from KiteCore import KiteCore

class KiteOperation:

     kiteCore=any
     def __init__(self):
         KiteOperation.kiteCore= KiteCore()         
         

     def getQuoteInFullMode(self, stockName,exchange, sender):
        instrumentToken=KiteOperation.kiteCore.getTokenFromName(stockName,exchange)
        KiteOperation.kiteCore.getQuote([instrumentToken],sender)


     def FilterInstruments(self,exchange):
         return KiteOperation.kiteCore.FilterInstrument(exchange)


     def getOrderDetails(self, orderID):
         return true

