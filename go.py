import pypyodbc as pyodbc
import pprint

from config import *

# S'il n'y a pas de fihcier config.py, il faut une variable de ce type:
# connStr = (
#     r'Driver={SQL Server};'
#     r'Server=IpOuNomServeur;'
#     #r'Server=127.0.0.1,52865;' +
#     #r'Server=(local)\SQLEXPRESS;'
#     r'Database=NomBase;'
#     r'Trusted_Connection=True;'
#     r'UID=Domaine\User;' #Voir avec Trusted_Connection
#     #r'PWD=sapassword;'
#     )

db = pyodbc.connect(connStr)
cursor = db.cursor()

cursor.execute("SELECT * FROM Province")

pp = pprint.PrettyPrinter(indent=4)

# Méthode 1
# while True:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print("Id: " + str(row[0]))

# Méthode 2

# columns = [column[0] for column in cursor.description]
# for row in cursor.fetchall():
#     pp.pprint(dict(zip(columns, row)))

# Method 3, we obtain a list of dict's (represents the entire query)
query_results = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
pp.pprint(query_results)

# On ferme tout !
cursor.close()
db.close()