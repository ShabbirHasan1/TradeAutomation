import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from DBOperator import DBOperator
from matplotlib.animation import FuncAnimation
from PlotData import PlotData



class Plotter:
    
    dbOperator=None
    table=None
    instrumentName=None

    def __init__(self,table,DBOperatorType,instrument):
        self.dbOperator=DBOperatorType
        self.instrumentName=instrument
        plt.style.use('fivethirtyeight')


    def plot(self,i):       

        x,y1,y2=self.dbOperator.Retrieve(self.instrumentName)
        for t in x:
            print(t)

        print("Inside plot")
        plt.cla()
        plt.plot(x,y1,label="LTP",color='k', linestyle = '--' , marker='s' , linewidth=2)
        plt.plot(x,y2,label="Ratio",color='b', linestyle = '--' , marker='o' , linewidth=2)
        plt.legend(loc='upper left')
         


    def Animate(self):
        ani = FuncAnimation(plt.gcf(), self.plot , interval=4000)
        plt.show()   


    

   

        










