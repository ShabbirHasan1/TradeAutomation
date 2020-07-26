import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from DBOperator import DBOperator
from matplotlib.animation import FuncAnimation
from PlotData import PlotData
import threading



class Plotter:
    
    dbOperator=None
    table=None
    ObjectList=None
    fig=None
    ax=None
    mainThread=None


    def __init__(self,table,DBOperatorType,ObjectList):
        self.fig,self.ax=plt.subplots(len(ObjectList))
        self.dbOperator=DBOperatorType
        self.ObjectList=ObjectList
        plt.style.use('fivethirtyeight')


    def plot(self,index,instrument):       

        x,y1,y2=self.dbOperator.Retrieve(instrument)
        
        print("Inside plot")
        self.ax[index].cla()
        self.ax[index].plot(x,y1,label="LTP",color='k', linestyle = '--' , marker='s' , linewidth=2)
        self.ax[index].plot(x,y2,label="Ratio",color='b', linestyle = '--' , marker='o' , linewidth=2)
        self.ax[index].legend(loc='upper left')
         


    def Animate(self,index,instrument):
        if not Plotter.mainThread:
            Plotter.mainThread=threading.currentThread().getName()
        ani = FuncAnimation(plt.gcf(), self.plot ,fargs=(index,instrument), interval=4000)
        #if(threading.currentThread().getName()==Plotter.mainThread):
        plt.show()

           


    

   

        










