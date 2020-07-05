from OperationController import OperationController



class RatioExtractor:
        Instrument=any
        Exchange=any
        Sender=any
        Operator=any

        def __init__(self):            
            controller=OperationController()
            self.Operator=controller.GetOperator()



        def get_market_quotes(self,Instrument,Exchange,sender):
            self.Sender=sender
            self.Operator.getQuoteInFullMode(Instrument,Exchange,self)



        def FilterInstruments(self,exchange):
            return self.Operator.FilterInstruments(exchange)



        def on_ticks(self,ticks):
            print("===============================================")
            print(ticks)



       