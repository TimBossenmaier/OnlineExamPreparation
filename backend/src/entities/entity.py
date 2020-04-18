# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

dict_db_params = None

# read the cofig JSON and load it as JSON
with open('./db_config.json', encoding='utf-8') as F:
    dict_db_params = json.load(F)

db_url = dict_db_params["host"]
db_name = dict_db_params["db_name"]
db_user = dict_db_params["user"]
db_password = dict_db_params["password"]

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

