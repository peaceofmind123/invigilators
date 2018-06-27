import tkinter as tk
from tkinter import ttk
import uiabstract
# the abstract update form class
class UpdateForm(uiabstract.ChildUI):
    def __init__(self,*args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        # data dictionary
        self.fields = None

