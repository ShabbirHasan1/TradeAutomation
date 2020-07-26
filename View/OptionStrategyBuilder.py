from tkinter import *
from Bridge import ControllerBridge
from StrategyBuilder import StrategyBuilder
import threading



master= Tk(className="Trade-Automation")

   
master.geometry("600x400")


label = Label(master, text = "Spot")
label.grid(column=3,row=1)


Spot=StringVar()
txtBox=Entry(master,textvariable=Spot)
txtBox.insert("end","11000")
txtBox.grid(column=3,row=2)
       

label = Label(master, text = "Strike")
label.grid(column=1,row=3)


Leg1Strike=StringVar()
txtBox=Entry(master,textvariable=Leg1Strike)
txtBox.insert(0,"11000")
txtBox.grid(column=2,row=3)


label = Label(master, text = "Strike")
label.grid(column=4,row=3)



Leg2Strike=StringVar()
txtBox=Entry(master,textvariable=Leg2Strike)
txtBox.insert(0,"11000")
txtBox.grid(column=5,row=3)



label = Label(master, text = "IV")
label.grid(column=1,row=4)


Leg1IV=StringVar()
txtBox=Entry(master,textvariable=Leg1IV)
txtBox.insert(0,20.5)
txtBox.grid(column=2,row=4)



label = Label(master, text = "IV")
label.grid(column=4,row=4)


Leg2IV=StringVar()
txtBox=Entry(master,textvariable=Leg2IV)
txtBox.insert(0,17.19)
txtBox.grid(column=5,row=4)


label = Label(master, text = "days to expire")
label.grid(column=1,row=5)


Leg1Exp=StringVar()
txtBox=Entry(master,textvariable=Leg1Exp)
txtBox.insert(0,7)
txtBox.grid(column=2,row=5)


label = Label(master, text = "days to expire")
label.grid(column=4,row=5)


Leg2Exp=StringVar()
txtBox=Entry(master,textvariable=Leg2Exp)
txtBox.insert(0,14)
txtBox.grid(column=5,row=5)



dd=["call","put"]
default = StringVar(master)
default.set(dd[0])
CallPut = OptionMenu(master, default , *dd)
CallPut.grid(column=3,row=6)



label = Label(master, text = "exit day")
label.grid(column=2,row=7)

time=0


def OnTimeChanged(value):
    time=int(value)
    StrategyBuilder.ResultCalculator(int(Spot.get()),int(Leg1Strike.get()),int(Leg2Strike.get()),float(Leg1IV.get())/100,float(Leg2IV.get())/100,(int(Leg1Exp.get())-int(value))/365,(int(Leg2Exp.get())-int(value))/365,default.get(),time)
    



timeScale=Scale(master,from_=0,to_=int(Leg1Exp.get()),command=OnTimeChanged)
timeScale.config(orient="horizontal")
timeScale.grid(column=3,row=7)





def clickMe():    
    build=StrategyBuilder()
    build.InitialSetUp(int(Spot.get()),int(Leg1Strike.get()),int(Leg2Strike.get()),float(Leg1IV.get())/100,float(Leg2IV.get())/100,int(Leg1Exp.get())/365,int(Leg2Exp.get())/365,default.get(),time)
    


button = Button(master, text = "Click Me", command = clickMe)
button.grid(column=3 , row = 8)



master.mainloop()



