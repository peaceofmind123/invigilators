import mysql.connector as connector
import tkinter as tk
from tkinter import ttk



class ViewUI(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self,*args,**kwargs)


if __name__ == "__main__":
    home_ui = HomeUI()
    home_ui.wm_title("Invigilators Database")
    home_ui.mainloop()

    # database connection
    connection = connector.connect(user='root',host='127.0.0.1',database='invigilators')

    cursor = connection.cursor()

    # execute sql queries on the cursor using cursor.execute(SQL string)

