from KiteCore import KiteCore

class KiteOperation:

     kiteCore=any
     def __init__(self):
         KiteOperation.kiteCore= KiteCore()         
         

     def getQuoteInFullMode(self, instruments,exchange, sender):
         tokenList=[]
         for instrument in instruments:
             instrumentToken=KiteOperation.kiteCore.getTokenFromName(instrument,exchange)
             tokenList.append(instrumentToken)
         KiteOperation.kiteCore.getQuote(tokenList,sender)


     def FilterInstruments(self,exchange):
         return KiteOperation.kiteCore.FilterInstrument(exchange)


     def getOrderDetails(self, orderID):
         return true

