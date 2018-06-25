import mysql.connector as connector
import tkinter as tk
from tkinter import ttk

mainWindow = tk.Tk()
# gui code goes here
mainWindow.mainloop()

# database connection
connection = connector.connect(user='root',host='127.0.0.1',database='invigilators')

cursor = connection.cursor()

# execute sql queries on the cursor using cursor.execute(SQL string)

