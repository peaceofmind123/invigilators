import tkinter as tk
from tkinter import ttk
import displayUpdate


class DisplayUpdateClassUI(displayUpdate.DisplayUpdateUI):
    def __init__(self, *args, **kwargs):
        displayUpdate.DisplayUpdateUI.__init__(self, *args, **kwargs)
        self.connect_to_db()
        # get data into the self.fields dictionary
        self.get_data_structure("class")
        self.displayData()
        self.mainloop()





