import sqlite3;
import pandas as pd;
import altair as alt

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



