import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import errorcode

load_dotenv()

MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get("MYSQL_DB")
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_PORT = os.environ.get("MYSQL_PORT")

config = {
    'host': MYSQL_HOST,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'database': MYSQL_DB
}


def db_read(query, params=None):
    try:
        cnx = mysql.connector.connect(**config, auth_plugin='mysql_native_password')
        cursor = cnx.cursor(dictionary=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        entries = cursor.fetchall()
        cursor.close()
        cnx.close()

        content = []

        for entry in entries:
            content.append(entry)

        return content

    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("User authorization error")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database doesn't exist")
    #     else:
    #         print(err)

    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("Connection closed")


def db_write(query, params=None):
    try:
        cnx = mysql.connector.connect(**config, auth_plugin='mysql_native_password')
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True

        except mysql.connector.Error as err:
            cursor.close()
            cnx.close()
            return False

    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("User authorization error")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database doesn't exist")
    #     else:
    #         print(err)
    #     return False

    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("Connection closed")
