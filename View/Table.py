from tkinter import *


class Table: 
    listOfSubscription=[]
    total_rows = 0
    total_columns =2
    root=None
    NumberEntry=[]
    InstrumentWidget=[]

    def __init__(self,root): 
        self.root=root


        

    def AddToTable(self,Instrument):
        self.listOfSubscription.append(Instrument)
        self.total_rows+=1
        self.NumberEntry.append(Entry(self.root, width=5, fg='blue', font=('Arial',12,'bold')))
        self.NumberEntry[self.total_rows-1].grid(row=(self.total_rows+10), column=0) 
        self.NumberEntry[self.total_rows-1].insert(END,self.total_rows) 
        self.InstrumentWidget.append(Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')))
        self.InstrumentWidget[self.total_rows-1].grid(row=(self.total_rows+10), column=1) 
        self.InstrumentWidget[self.total_rows-1].insert(END,self.listOfSubscription[self.total_rows-1]) 



        
                    
    def ClearTable(self):
        for numberEntry in self.NumberEntry:
            numberEntry.destroy()
        self.NumberEntry.clear()

        for instrumentWidget in self.InstrumentWidget:
            instrumentWidget.destroy()
        self.InstrumentWidget.clear()

        self.listOfSubscription.clear()
        self.total_rows=0






               
                  
                