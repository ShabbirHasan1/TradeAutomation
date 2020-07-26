from BlackAndScholes import BlackAndScholesModel
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math



class StrategyBuilder:

    cmp1=None
    cmp2=None
    nearstrikeResult=None
    farStrikeResult=None
    Spot=None
    result=None
    fig=None
    ax=None
    lowCutoff=None
    Mid=None
    UpCutoff=None
    lowerlow=None
    upperup=None
    fiftylow=None
    fiftyHigh=None


    def plot(self):
        StrategyBuilder.ax[0].cla()
        StrategyBuilder.ax[1].cla()
        StrategyBuilder.ax[2].cla()
        StrategyBuilder.ax[0].plot(StrategyBuilder.Spot,StrategyBuilder.nearstrikeResult,color='k')        
        StrategyBuilder.ax[1].plot(StrategyBuilder.Spot,StrategyBuilder.farStrikeResult,color='k')        
        StrategyBuilder.ax[2].plot(StrategyBuilder.Spot,StrategyBuilder.result,color='k')
        StrategyBuilder.ax[2].axhline(0, color='r', linewidth=0.5)
        StrategyBuilder.ax[2].axvline(StrategyBuilder.lowCutoff, color='b', linewidth=1)
        StrategyBuilder.ax[2].axvline(StrategyBuilder.Mid, color='r', linewidth=0.5)
        StrategyBuilder.ax[2].axvline(StrategyBuilder.UpCutoff, color='b', linewidth=1)

        StrategyBuilder.ax[2].axvline(StrategyBuilder.lowerlow, color='g', linewidth=1)
        StrategyBuilder.ax[2].axvline(StrategyBuilder.upperup, color='g', linewidth=1)

        StrategyBuilder.ax[2].axvline(StrategyBuilder.fiftyHigh, color='y', linewidth=1)
        StrategyBuilder.ax[2].axvline(StrategyBuilder.fiftylow, color='y', linewidth=1)



        StrategyBuilder.ax[0].grid()
        StrategyBuilder.ax[1].grid()
        StrategyBuilder.ax[2].grid()



    def InitialSetUp(self,spot,strike1,strike2,iv1,iv2,exp1,exp2,Otype,holdingTime):
         StrategyBuilder.cmp1=BlackAndScholesModel.euro_vanilla(spot,strike1,exp1,0.07,iv1,option=Otype)
         StrategyBuilder.cmp2=BlackAndScholesModel.euro_vanilla(spot,strike2,exp2,0.07,iv2,option=Otype)
         print(StrategyBuilder.cmp1)
         print(StrategyBuilder.cmp2)
         StrategyBuilder.ResultCalculator(spot,strike1,strike2,iv1,iv2,exp1,exp2,Otype,holdingTime)
         StrategyBuilder.fig,StrategyBuilder.ax=plt.subplots(3)
         ani = FuncAnimation(plt.gcf(), StrategyBuilder.plot)         
         plt.show()






    def StaticTimeDynamicSpotResultCalculator(spot,strike1,strike2,iv1,iv2,exp1,exp2,Otype,holdingTime):
        diff=spot*(math.sqrt(holdingTime/365))*iv1
        StrategyBuilder.Mid=spot
        StrategyBuilder.lowCutoff=spot-diff
        StrategyBuilder.UpCutoff=spot+diff
        StrategyBuilder.upperup=spot+(1.5*diff)
        StrategyBuilder.lowerlow=spot-(1.5*diff)
        StrategyBuilder.fiftyHigh=spot+(0.5*diff)
        StrategyBuilder.fiftylow=spot-(0.2*diff)
        diff=700
        upSpot=spot+diff
        lowSpot=spot-diff
        nearstrikeResult=[]
        farStrikeResult=[]
        Spot=[]
       
        while lowSpot<upSpot:
            nearstrikeResult.append(StrategyBuilder.cmp1-BlackAndScholesModel.euro_vanilla(lowSpot,strike1,exp1,0.07,iv1,option=Otype))
            farStrikeResult.append(BlackAndScholesModel.euro_vanilla(lowSpot,strike2,exp2,0.07,iv2,option=Otype)-StrategyBuilder.cmp2)
            Spot.append(lowSpot)
            lowSpot=lowSpot+10

        return nearstrikeResult,farStrikeResult,Spot





    
        

    
    def ResultCalculator(spot,strike1,strike2,iv1,iv2,exp1,exp2,Otype,holdingTime):   
       
        StrategyBuilder.nearstrikeResult,StrategyBuilder.farStrikeResult,StrategyBuilder.Spot=StrategyBuilder.StaticTimeDynamicSpotResultCalculator(spot,strike1,strike2,iv1,iv2,exp1,exp2,Otype,holdingTime)
        StrategyBuilder.result=[]
        for i in range(len(StrategyBuilder.nearstrikeResult)):
            StrategyBuilder.result.append(StrategyBuilder.nearstrikeResult[i]+StrategyBuilder.farStrikeResult[i])

        


