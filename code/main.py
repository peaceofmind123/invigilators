import mysql.connector as connector
import tkinter as tk
from tkinter import ttk

class HomeUI(tk.Tk):

    def update_db(self,event):
        # redirect to update ui which is a child window of self
        self.update_UI = UpdateUI()
        self.update_UI.wm_title("Update entries")
        self.update_UI.mainloop()


    def view_db(self,event):
        # redirect to view ui
        self.view_UI = ViewUI()
        self.view_UI.wm_title("View entries")

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)


        # child UI definitions
        self.update_UI = None
        self.view_UI = None

       # button definitions
        self.btn_updateDB = ttk.Button(self,text="Update/add entries")
        self.btn_viewDB = ttk.Button(self,text="View entries")

        # callback binds
        self.btn_updateDB.bind("<Button-1>", self.update_db)
        self.btn_viewDB.bind("<Button-1>", self.view_db)

        # layout definition
        self.btn_updateDB.grid(row=0,column=0,columnspan=2)
        self.btn_viewDB.grid(row=0, column=2,columnspan=2)


class UpdateUI(tk.Toplevel): # toplevel since these will inevitably be children windows
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self,*args,**kwargs)


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

