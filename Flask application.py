import sqlite3
import pandas as pd
import sqlalchemy
from IPython.display import display
import re
from pymongo import MongoClient
from flask import Flask
app = Flask(__name__)
# from tabulate install Tabulate



def konektiranjesosqlite(): #funkcija za konektianje na db so sqlite (imame konektiranje i cursor)
    try:
        konekcija = sqlite3.connect('test.db')
        cursor = konekcija.cursor()
        print("Database Successfully Connected to SQLite")
        return konekcija,cursor

    except Exception as error:
        print("Error while connecting to sqlite", error)
        return None, None

def procistuvanje(st):
    procistuvanje1 = re.sub(r'\(.*\)', "", st)
    procistuvanje2 = re.sub(r',.*', "", procistuvanje1)
    procistuvanje2.replace(' - ',"")
    procistuvanje3 = procistuvanje2\
        .replace("LIMITED", "")\
        .replace("Limited", "")\
        .replace("LTD.", "")\
        .replace('ltd.','')\
        .replace('Ltd', "") \
        .replace('ltd', "") \
        .replace('.ltd', "") \
        .replace("LTD", "")\
        .replace("limited", "")\
        .lower()\
        .title()
    procistuvanje4 = re.sub(r' - ', "", procistuvanje3)
    return procistuvanje4


@app.route("/", methods=["GET" , "POST"])
def home():
    konekcija, cursor = konektiranjesosqlite()
    if konekcija is None or cursor is None:
        return 'Error'
    df = pd.read_sql("select * from companies", con=konekcija)
    df['company_came_cleaned'] = df['name'].apply(procistuvanje)   # tuka se povikuva funkcijata procistuvanje i se
    # izvrsuva i od name se prefluva vo cleaned
    # df.to_sql(name='companies', if_exists='replace', con = konekcija)
    # display(df)
    client = MongoClient('localhost', 27017)
    db = client.semos_database
    collection = db.companies
    collection.insert_many(df.to_dict('records'))
    return "Connected to SQLite DB"




print(procistuvanje('AAAAA-kjhk (asdasdas) - SJKFFJF -LIMITED LIMITED LTD. ltd. Limited limited LTD ltd' ))

# df['name'].apply(funkicja(lambda a : a.replace('Limited', '')))
app.run(debug=True)
# SELECT * FROM ime na kolonata e se sto teba da znaeme od SQL za da ja seletiame datata od

# conn = sqlite3.connect(database)
#
# df = pd.read_sql("select * from name", con=conn)
# print(df)
# conn.close()

# "Ahl":{
#     name: ah
#     city:...
#
# }