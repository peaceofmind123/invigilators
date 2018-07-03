import tkinter as tk
from tkinter import ttk
import mysql.connector as connector

class ParentUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.relx = .5
        self.rely = .4

        # getting the params
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "relx":
                    self.relx = value
                elif key == "rely":
                    self.rely = value


        # configuration
        self.resizable(False,False)
        # containers
        self.outercontainer = tk.Frame(self, width=400, height=400)
        self.outercontainer.pack(fill="both", expand=True)
        self.container = tk.Frame(self.outercontainer)
        self.container.place(in_=self.outercontainer, anchor="c", relx=.5, rely=.4)
        self.outercontainer.pack_propagate(0)


class ChildUI(tk.Toplevel):
    # internal class to hold database metadata
    class DB:
        def __init__(self):
            self.user=None
            self.host=None
            self.database=None

    class Fields:
        pass

    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.relx = .5
        self.rely = .4
        self.connection = None
        self.cursor = None
        self.db = self.DB()
        self.db.user="root"
        self.db.host="localhost"
        self.db.database="invigilators"

        # getting the params
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "relx":
                    self.relx = value
                elif key == "rely":
                    self.rely = value

        # configuration
        self.resizable(False, False)
        # containers
        self.container = tk.Frame(self)
        self.container.pack()


    def connect_to_db(self,*args,**kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "user":
                    self.db.user = value
                elif key == "host":
                    self.db.host = value
                elif key == "database":
                    self.db.database = value

        # database connection
        try:
            self.connection = connector.connect(user=self.db.user, host=self.db.host, database=self.db.database,autocommit=True)

            self.cursor = self.connection.cursor()

        except connector.errors.DatabaseError:
            print("Database connection could not be established")
            self.master.quit()
            # execute sql queries on the cursor using cursor.execute(SQL string)
