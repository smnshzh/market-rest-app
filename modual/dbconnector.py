import pyodbc
import pandas
# f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
cnx = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=127.0.0.1;DATABASE=testTarget;UID=sa;PWD=123456')

def tables():
    df = pandas.read_sql("select * from sys.tables",cnx)

    return df

