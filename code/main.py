import mysql.connector as connector

connection = connector.connect(user='root',host='127.0.0.1',database='invigilators')

cursor = connection.cursor()

