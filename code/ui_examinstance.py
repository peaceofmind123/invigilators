import tkinter as tk
from tkinter import ttk
import displayUpdate


class DisplayUpdateExaminstanceUI(displayUpdate.DisplayUpdateUI):
    def __init__(self, *args, **kwargs):
        displayUpdate.DisplayUpdateUI.__init__(self, *args, **kwargs)
        self.connect_to_db(user='root', host='127.0.0.1', database='invigilators')





