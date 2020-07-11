from OperationController import OperationController
from PlotData import PlotData
import datetime
import time



class RatioExtractor:
        Instrument=any
        Exchange=any
        Sender=any
        Operator=any
        data=None

        def __init__(self):            
            controller=OperationController()
            self.Operator=controller.GetOperator()
            #############################
            self.data=data=PlotData()#To be removed
            self.data.InstrumentName="REL"
            self.data.LTP=9.0
            self.data.Ratio=4.5
            ################################

        def get_market_quotes(self,Instruments,Exchange,sender):
            self.Sender=sender
            self.Operator.getQuoteInFullMode(Instruments,Exchange,self)



        def FilterInstruments(self,exchange):
            return self.Operator.FilterInstruments(exchange)



        def on_ticks(self,ticks):
            print("===============================================")
            print(ticks)
            for i in range(10):
                time.sleep(4)
                tempData=PlotData()
                tempData.InstrumentName="NIFTY 50"
                self.data.LTP+=1
                tempData.LTP=self.data.LTP
                self.data.Ratio+=1
                tempData.Ratio=self.data.Ratio
                tempData.Time=datetime.datetime.now()
                try:
                    self.Sender.SaveToDB(tempData)

                except:
                    print("DB save failed")

            

            





       