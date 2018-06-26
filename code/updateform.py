import tkinter as tk
from tkinter import ttk

# the abstract update form class
class UpdateForm(tk.Toplevel):
    def __init__(self,*args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
