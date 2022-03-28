import json;
import sqlite3;
import pandas as pd;
import statistics;


con = sqlite3.connect('SISTINF.db');
lista = [];

def sql_select():
    cursorObj = con.cursor()
    cursorObj.execute('SELECT creacion as a FROM legal')
    rows = cursorObj.fetchall()
    for row in rows:
        df_1 = pd.DataFrame(row);
        lista.append(row[0]);
    print(str(statistics.pstdev(lista)));

sql_select();

