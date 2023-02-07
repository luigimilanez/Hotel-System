import mysql.connector
from mysql.connector import errorcode
from time import sleep as ts  # sleep function
# from tkinter import messagebox


def conexao(cnx):  # just repeat the 'cnx'
    while True:
        try:
            cnx = mysql.connector.connect(host='localhost', user='root', database='Hotel')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                ts(5)
                # messagebox.showwarning('Error', 'Database: Something is wrong with your user name or password')
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                ts(5)
                # messagebox.showwarning('Error', 'Database: Database does not exist')
                print("Database does not exist")
            else:
                ts(5)
                # messagebox.showwarning('Error', 'Database: Inexpected Error')
                print(err)
        else:
            return cnx  # usado na manipulação fora da função


if __name__ == '__main__':
    cnx = conexao('cnx')
    print('Connection Sucessful')