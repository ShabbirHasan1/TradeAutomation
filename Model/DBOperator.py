from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from datetime import datetime
from PlotData import PlotData


class DBOperator():
    session=None
    engine =create_engine('mysql+mysqlconnector://root:harsha123@127.0.0.1:3306/traderdetails')
    table=None

    def __init__(self,table):
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=self.engine)
        DBOperator.table=table
        DBOperator.session = Session()
    

    def Add(self,data):        
        DBOperator.session.add(data)
        DBOperator.session.commit()


    def RetrieveAllID(self):
        All=self.RetrieveAll()
        ID=[]
        for each in All:
            ID.append(each.ID)
        return ID



    def RetrieveAll(self):        
        all=DBOperator.session.query(self.table).all()
        return all

            
    def Commit(self):
        DBOperator.session.commit()


    def Delete(self,data):
        DBOperator.session.delete(data)
        DBOperator.session.commit()

    

    


   

   


 


                 