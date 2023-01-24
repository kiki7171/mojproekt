import sqlite3
import pandas as pd
import sqlalchemy
from flask import Flask
from IPython.display import display
import re
from flask import Flask
app = Flask(__name__)
# from tabulate install Tabulate



def connectToSql():
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        return sqliteConnection,cursor

    except Exception as error:
        print("Error while connecting to sqlite", error)
        return None, None


@app.route("/")
def home():
    sqliteConnection,cursor = connectToSql()
    if sqliteConnection is None or cursor is None:
        return 'Error'
    df = pd.read_sql("select name from companies", con=sqliteConnection)
    df['name'].apply()
    display(df)
    return "Connected to SQLite DB"


def transformString(st):
    transformacija1=re.sub(r'\(.*\)', "", st)
    transformacija2=re.sub(r',.*', "", transformacija1)
    transformacija2.replace(' - ',"")
    transformacija3=transformacija2\
        .replace("LIMITED", "")\
        .replace("Limited", "")\
        .replace("LTD.", "")\
        .replace('ltd.','')\
        .replace("limited", "")\
        .lower()\
        .title()
    transformacija4=re.sub(r' - ', "", transformacija3)
    return transformacija4

print (transformString('AAAAA-kjhk (asdasdas) - SJKFFJF -LIMITED LIMITED LTD. ltd. Limited limited'))

# df['name'].apply(funkicja(lambda a : a.replace('Limited', '')))
app.run(debug=True)
# SELECT * FROM ime na kolonata e se sto teba da znaeme od SQL za da ja seletiame datata od

# conn = sqlite3.connect(database)
#
# df = pd.read_sql("select * from name", con=conn)
# print(df)
# conn.close()


