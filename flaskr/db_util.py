import psycopg2
from pprint import pprint

class DbUtil:
    def __init__(self):
        
        pprint("Initialized")

    #@staticmethod
    def connect(self):
         try:
            self.connection = psycopg2.connect(
                "dbname='posts' user='postgres' host='localhost' password='Dreamalive1' port='5432'")
            #self.connection.autocommit = True
            return self.connection
        
         except:
            pprint("Cannot connect to database")
    


