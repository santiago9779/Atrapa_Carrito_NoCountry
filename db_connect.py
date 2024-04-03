import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector


def conexion_db():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        print("Conectado a la base de datos")
        return mydb
    except mysql.connector.Error as err:
        print("Error al conectar a la base de datos:", err)
        exit()