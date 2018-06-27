import tkinter as tk
from tkinter import ttk
import uiabstract


# the abstract update form class
class DisplayUpdateUI(uiabstract.ChildUI):
    def __init__(self,*args, **kwargs):
        uiabstract.ChildUI.__init__(self, *args, **kwargs)

        # data dictionary
        self.fields = {}


    # populates the self.fields object
    def get_data_structure(self, table):
        if self.cursor is not None:
            # getting the table descriptor object
            self.cursor.execute("desc "+table)
            column_names = []
            index=0
            for descriptor in self.cursor.fetchall():
                column_names.insert(index,descriptor[0]) # descriptor[0] contains column name
                self.fields[column_names[index]] = []
                index += 1

            # getting values
            self.cursor.execute("select * from "+table)
            for row in self.cursor.fetchall():
                index = 0

                for column in row:

                    self.fields[column_names[index]].insert(index,row[index])
                    index += 1

            print(self.fields)