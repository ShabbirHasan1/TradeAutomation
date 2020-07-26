from DBOperator import DBOperator
from datetime import datetime

class PlotDataDBOperator(DBOperator):
    def __init__(self, table):
           super().__init__(table)



    def RetrieveAllTime(self):
        All=self.RetrieveAll()
        Time=[]
        for each in All:
            Time.append(each.Time)
        return Time



    def RetrieveAllRatio(self):
        All=self.RetrieveAll()
        Ratio=[]
        for each in All:
            Ratio.append(each.Ratio)
        return Ratio



    def RetrieveAllLTP(self):
        All=self.RetrieveAll()
        LTP=[]
        for each in All:
            LTP.append(each.LTP)
        return LTP



    def Retrieve(self,instrument,startdate=datetime.combine(datetime.today(),datetime.min.time()),enddate=datetime.combine(datetime.today(),datetime.max.time())):
      All=self.RetrieveAll()
      Time=[]
      Ratio=[]
      LTP=[]
      for each in All:
          if (each.InstrumentName==instrument):#&(each.Time > startdate)&(each.Time<enddate):   
              Time.append(each.Time)
              Ratio.append(each.Ratio)
              LTP.append(each.LTP)

      return Time,Ratio,LTP






