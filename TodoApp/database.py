from fastapi import FastAPI
import sqlalchemy
from sqlalchemy.orm  import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABSE_URL= 'sqlite:///./todosapp.db'#postgresql://postgres:Shreyash@localhost/TodoApplicationDatabase
engine= create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal= sessionmaker(autocommit=False,autoflush=False, bind= engine)

Base= sqlalchemy.orm.declarative_base()