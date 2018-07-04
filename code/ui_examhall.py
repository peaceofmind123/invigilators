import tkinter as tk
from tkinter import ttk
import displayUpdate


class DisplayUpdateExamhallUI(displayUpdate.DisplayUpdateUI):
    def __init__(self, *args, **kwargs):
        displayUpdate.DisplayUpdateUI.__init__(self, *args, **kwargs)
        self.connect_to_db()
        self.get_data_structure("examhall")
        self.displayData()
        self.mainloop()



