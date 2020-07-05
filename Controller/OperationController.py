from KiteOperation import KiteOperation

class OperationController:
    Operator=any
    def __init__(self):
        self.Operator=KiteOperation() 

    def GetOperator(self):
        return self.Operator


    
