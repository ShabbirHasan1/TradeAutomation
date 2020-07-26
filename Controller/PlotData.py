from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import cast, select, String


Base = declarative_base()

class PlotData(Base): 
     __tablename__ = 'plotdata'
     ID = Column(Integer, primary_key=True)
     InstrumentName=Column(String(40))
     Time=Column(DateTime)
     LTP = Column(Integer)
     Ratio=Column(Integer)
     
     
# CREATE TABLE `traderdetails`.`plotdata` (
#   `ID` INT NOT NULL,
#   `InstrumentName` VARCHAR(40) NULL,
#   `Time` DATETIME NULL,
#   `LTP` INT NULL,
#   `Ratio` INT NULL,
#   PRIMARY KEY (`ID`));
