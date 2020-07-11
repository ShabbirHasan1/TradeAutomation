from RatioExtractor import RatioExtractor
from DBOperator import DBOperator
from Plotter import Plotter
from PlotData import PlotData
import threading


class ControllerBridge:

    LogicOperator=None
    dbOperator=None
    plotter=None

    def __init__(self):
        self.LogicOperator=RatioExtractor()
        self.dbOperator=DBOperator(PlotData)


    
    def GetInstruments(self,exchange):
        instruments= self.LogicOperator.FilterInstruments(exchange)
        return instruments



    def SaveToDB(self,data):
        self.dbOperator.Add(data)
        

             

    def SubscribeMarketQuotes(self,Instruments,Exchange):
        self.LogicOperator.get_market_quotes(Instruments,Exchange,self)






