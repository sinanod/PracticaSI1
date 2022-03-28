import sqlite3;
import pandas as pd;

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
print("El número de observaciones es:", dUsers['emailsPhising'].describe()['count'])
print("La mediana es:", dUsers['emailsPhising'].median())
print("La media es:",dUsers['emailsPhising'].describe()['mean'])
print("La varianza es:", dUsers['emailsPhising'].var())
print("El valor mínimo y máximos es:", dUsers['emailsPhising'].describe()['min'],
      "y el valor máximo es", dUsers['emailsPhising'].describe()['max'])


