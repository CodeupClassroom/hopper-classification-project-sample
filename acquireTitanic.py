import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
    This function takes in as arguments the database, username, host, and password for 
    the mysql database and returns a string that can be used to open a connection to the server
    and query the db in the read_sql function. 
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_data():
    '''
    This function takes in no arguments, uses the get_connection() function 
    and returns the mysql titanic_db.passengers table in the form of a dataframe. 
    '''
    return pd.read_sql('select * from passengers', get_connection('titanic_db'))