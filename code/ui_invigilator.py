import tkinter as tk
from tkinter import ttk
import displayUpdate


class DisplayUpdateInvigilatorUI(displayUpdate.DisplayUpdateUI):
    def __init__(self, *args, **kwargs):
        displayUpdate.DisplayUpdateUI.__init__(self, *args, **kwargs)
        self.connect_to_db()
        self.get_data_structure("invigilator")
        self.displayData()
        self.mainloop()



