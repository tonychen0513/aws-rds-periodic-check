"""
Method to access Ress DB data.
Copyright © 2019, Swann Communications, All rights reserved
"""
import os
from contextlib import contextmanager
import pymysql


db_Read_Endpoint = os.environ['RESS_DB_READ_ENDPOINT']
db_Write_Endpoint = os.environ['RESS_DB_ENDPOINT']


class RessDb:
    def __init__(self, connection):
        self.connection = connection

    @staticmethod
    @contextmanager
    def readonly():
        connection = _connect(db_Read_Endpoint)
        try:
            yield RessDb(connection)
        finally:
            connection.close()

    @staticmethod
    @contextmanager
    def readwrite():
        connection = _connect(db_Write_Endpoint)
        try:
            yield RessDb(connection)
        finally:
            connection.close()

    def execute_sql(self, sql, parameters):
        """ Execute SQL statement and returns cursor. """
        cursor = self.connection.cursor()
        cursor.execute(sql, parameters)
        return cursor

    def query_all(self, sql, parameters):
        cursor = self.execute_sql(sql, parameters)
        return cursor.fetchall()


def _connect(endpoint):
    """ Connects to the RESS database and returns the pymysql connection object."""
    return pymysql.connect(
        user=os.environ.get('RESS_DB_USER'),
        password=os.environ.get('RESS_DB_PSWD'),
        db=os.environ.get('RESS_DB_DATABASE', 'ress'),
        host=endpoint,
        port=int(os.environ.get('RESS_DB_PORT', 3306)),
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=200,
        autocommit=True
    )
