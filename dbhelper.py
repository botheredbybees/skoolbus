import pymysql
import dbconfig


class DBHelper:


    def connect(self, database="skoolbus"):

        return pymysql.connect(host='localhost',
                           user=dbconfig.db_user,
                           passwd=dbconfig.db_password,
                           db=database)


    def get_all_inputs(self):

        connection = self.connect()
        try:
            query = "SELECT userName FROM users;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            connection.close()


    def add_input(self, data):

        connection = self.connect()
        try:
            query = "INSERT INTO users (userName) VALUES ('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()


    def clear_all(self):

        connection = self.connect()
        try:
            query = "DELETE FROM users;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
