import tkinter as tk
from tkinter import ttk
import updateform


class UpdateStaffForm(updateform.UpdateForm):
    def __init__(self, *args, **kwargs):
        updateform.UpdateForm.__init__(self, *args, **kwargs)
        self.connect_to_db(user='root', host='127.0.0.1', database='invigilators')




