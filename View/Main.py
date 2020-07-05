from tkinter import *
from Bridge import ControllerBridge



class view:
    AllInstruments=[]
    FilteredInstruments=[]
    Exchanges=["NSE","BSE","MCX"]
    TextBoxString=None
    selectedExchange=None
    selectedInstrument=None
    InstrumentDropDown=None
    ExchangeDropDown=None
    bridge=None
    txtBox=None

    def __init__(self):
        master.geometry("200x100")

        view.bridge=ControllerBridge()
        DefaultExchange = StringVar(master)
        DefaultExchange.set(view.Exchanges[0]) # default value

        ExchangeDropDown = OptionMenu(master, DefaultExchange, *view.Exchanges,command=view.OnExchangeChanged)
        ExchangeDropDown.grid(column=2,row=1)

        view.TextBoxString=StringVar()
        view.TextBoxString.trace("w",view.OnTxtChanged)
        view.txtBox=Entry(master,textvariable=view.TextBoxString)
        view.txtBox.grid(column=1,row=1)

        submit_Btn=Button(master,text="Submit",command=self.OnSubmit)
        submit_Btn.grid(column=1,row=3)
    

    def OnExchangeChanged(value):
        view.selectedExchange=value
        view.AllInstruments=view.bridge.GetInstruments(view.selectedExchange)
        DefaultInstrument=StringVar(master)
        DefaultInstrument.set(view.AllInstruments[0])
        if view.InstrumentDropDown :
            view.InstrumentDropDown.destroy()        
        view.InstrumentDropDown=OptionMenu(master,DefaultInstrument,*view.AllInstruments,command=view.OnInstrumentSelected)
        view.InstrumentDropDown.grid(column=1,row=2)


    def OnInstrumentSelected(value):
        view.selectedInstrument=value
        view.txtBox.delete(0,'end')
        view.txtBox.insert(END,value)
        
        


    def OnTxtChanged(arg1,arg2,arg3):
        startsWith=view.TextBoxString.get().upper()
        view.FilteredInstruments=[]
        for i in view.AllInstruments:
            if i.startswith(startsWith):
                view.FilteredInstruments.append(i)

        DefaultInstrument = StringVar(master)
        DefaultInstrument.set(view.FilteredInstruments[0]) # default value
        if view.InstrumentDropDown :
            view.InstrumentDropDown.destroy()
        view.InstrumentDropDown=OptionMenu(master, DefaultInstrument, *view.FilteredInstruments,command=view.OnInstrumentSelected)
        view.InstrumentDropDown.grid(column=1,row=2)
        view.selectedInstrument=view.TextBoxString.get().upper()
                    

            

    def OnSubmit(self):
        view.bridge.SubscribeMarketQuotes(view.selectedInstrument,view.selectedExchange)
        print("submit")



    def PlotCallback(ratio,ltp):
       #enter logic for plot in matplotlib
       return



master = Tk(className="Trade-Automation")
viewer=view()
master.mainloop()



