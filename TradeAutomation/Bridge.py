from RatioExtractor import RatioExtractor

class ControllerBridge:

    Operator=any

    def __init__(self):
        self.Operator=RatioExtractor()

    
    def GetInstruments(self,exchange):
        instruments= self.Operator.FilterInstruments(exchange)
        return instruments

    def SaveToDBAndPlot(self):
        #connect database and send the data to 
        return

    def SubscribeMarketQuotes(self,Instrument,Exchange):
        self.Operator.get_market_quotes(Instrument,Exchange,self)




    


class ModelBridge:

    def __init(self):
        a=0

