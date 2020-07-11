from tkinter import *
from Bridge import ControllerBridge
import threading
from Table import Table
from PlotData import PlotData
from Plotter import Plotter
from PlotDataDBOperator import PlotDataDBOperator

class CurrentState:    
    AllInstruments=[]
    FilteredInstruments=[]
    Exchanges=["NSE","BSE","MCX"]
    TextBoxString=None
    selectedExchange=None
    selectedInstrument=None
    InstrumentDropDown=None
    ExchangeDropDown=None
    txtBox=None
    ListOfActiveInstruments=[]
    table=None



class view:
    state=None
    bridge=None

    def __init__(self):
        view.state=CurrentState()
        self.bridge=ControllerBridge()
        
        
        master.geometry("200x100")

        DefaultExchange = StringVar(master)
        DefaultExchange.set(view.state.Exchanges[0]) # default value

        view.state.ExchangeDropDown = OptionMenu(master, DefaultExchange, *view.state.Exchanges,command=self.OnExchangeChanged)
        view.state.ExchangeDropDown.grid(column=2,row=1)


        view.state.TextBoxString=StringVar()
        view.state.TextBoxString.trace("w",view.OnTxtChanged)
        view.state.txtBox=Entry(master,textvariable=view.state.TextBoxString)
        view.state.txtBox.grid(column=1,row=1)

        Add_Btn=Button(master,text="Add",command=self.OnAdd)
        Add_Btn.grid(column=1,row=3)

        Clear_Btn=Button(master,text="Clear", command=self.OnClear)
        Clear_Btn.grid(column=2,row=3)

        getQuote_Btn=Button(master,text="GetQuote",command=self.OnGetQuotes)
        getQuote_Btn.grid(column=3,row=3)
    
        view.state.table=Table(master)




    def OnExchangeChanged(self,value):
        view.state.selectedExchange=value
        view.state.AllInstruments=self.bridge.GetInstruments(view.state.selectedExchange)
        DefaultInstrument=StringVar(master)
        DefaultInstrument.set(view.state.AllInstruments[0])
        if view.state.InstrumentDropDown :
            view.state.InstrumentDropDown.destroy()  
        try:
            view.state.InstrumentDropDown=OptionMenu(master, DefaultInstrument,*view.state.AllInstruments,command=view.OnInstrumentSelected)
            view.state.InstrumentDropDown.grid(column=1,row=2)
        except IndexError as error:
            print(error)
            print("cannotcreate new drop down(Possible error: wrong exchange name has been give) : OnExchangeChanged")

        


    def OnInstrumentSelected(value):
        view.state.TextBoxString=value
        view.state.selectedInstrument=value
        view.state.txtBox.delete(0,'end')
        view.state.txtBox.insert(END,value)
        
        


    def OnTxtChanged(arg1,arg2,arg3):
        startsWith=view.state.TextBoxString.get().upper()
        view.state.FilteredInstruments.clear()
        for each in view.state.AllInstruments:
            if each.startswith(startsWith):
                view.state.FilteredInstruments.append(each)

        try:
             DefaultInstrument = StringVar(master)
             DefaultInstrument.set(view.state.FilteredInstruments[0]) # default value
             if view.state.InstrumentDropDown :
                 view.state.InstrumentDropDown.destroy()
             view.state.InstrumentDropDown=OptionMenu(master, DefaultInstrument, *view.state.FilteredInstruments,command=view.OnInstrumentSelected)
             view.state.InstrumentDropDown.grid(column=1,row=2)
             view.state.selectedInstrument=view.state.TextBoxString.get().upper()

        except IndexError as error:
            print(error)
            print("instrument Doesnot exist")





    def OnAdd(self):
        view.state.ListOfActiveInstruments.append(view.state.selectedInstrument)
        view.state.table.AddToTable(view.state.selectedInstrument)




    def OnClear(self):
        view.state.ListOfActiveInstruments.clear()
        view.state.table.ClearTable()



    def OnGetQuotes(self):  
            self.bridge.SubscribeMarketQuotes(view.state.ListOfActiveInstruments,view.state.selectedExchange)
            for instrument in view.state.ListOfActiveInstruments:
                plotter=Plotter(PlotData,PlotDataDBOperator(PlotData),instrument)
                threading.Thread(target = plotter.Animate).start()
            
            
            
        


master = Tk(className="Trade-Automation")
viewer=view()
master.mainloop()



