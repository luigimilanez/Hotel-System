import mysql.connector
from mysql.connector import errorcode
from time import sleep as ts  # sleep function


def conexao(cnx):  # apenas repita a string 'cnx'
    while True:
        try:
            cnx = mysql.connector.connect(host='IP_HOST', user='USUARIO', password='SENHA', database='DATABASE_NAME')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                ts(5)
                print("Something is wrong with your user name or password", err)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                ts(5)
                print("Database does not exist", err)
            else:
                ts(5)
                print(err)
        else:
            return cnx


if __name__ == '__main__':
    cnx = conexao('cnx')
    print('Connection Sucessful')
