import os 
import time
import random
import psycopg2

# from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PWD = os.environ.get('POSTGRES_PWD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')

def connect():
    print(f"Connecting to DB ...")
    # Connecto to the database
    conn_string = 'postgresql://{}:{}@{}:{}/{}'.format(
        POSTGRES_USER
        , POSTGRES_PWD
        , POSTGRES_HOST
        , POSTGRES_PORT
        , POSTGRES_DB
    )

    print(f"DB Connection string {conn_string}")

    db = None
    try:
        db = psycopg2.connect(
            database=POSTGRES_DB
            , user=POSTGRES_USER
            , password=POSTGRES_PWD
            , host=POSTGRES_HOST
            , port= POSTGRES_PORT
            )
    except Exception as e:
        print(f"Error: {e}")


    if db == None:
        print(f"Could not connect to DATABASE: {POSTGRES_DB} on HOST: {POSTGRES_HOST} ")
        return False

    #Creating a cursor object using the cursor() method
    cursor = db.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute("select version()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Connection established to: ",data)
    return True

def close(db):

    #Closing the connection
    db.close()