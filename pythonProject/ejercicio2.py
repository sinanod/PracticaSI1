import json;
import sqlite3;
import pandas as pd;
import statistics;


con = sqlite3.connect('SISTINF.db');

query = con.execute("SELECT * From legal")
cols = [column[0] for column in query.description]
dLegal = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From users")
cols = [column[0] for column in query.description]
dUsers = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From fechas_user")
cols = [column[0] for column in query.description]
dFechas_User = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

query = con.execute("SELECT * From ips_user")
cols = [column[0] for column in query.description]
dIPS_User = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

con.close()


print("La media de correos recibidos son: ", dUsers['emailsPhising'].describe()['mean'])
print("La desviacion estándar de correos recibidos son: ", dUsers['emailsPhising'].describe()['std'])
print("El valor máximo de correos recibidos es: ", dUsers['emailsPhising'].describe()['max'])
print("La valor mínimo de correos recibidos es: ", dUsers['emailsPhising'].describe()['min'])

print("El valor máximo de las fechas que se ha iniciado sesión es: ", dFechas_User['fecha'].describe()['top'])

