import tkinter as tk
from tkinter import ttk
import uiabstract


# the abstract update form class
class DisplayUpdateUI(uiabstract.ChildUI):
    def __init__(self,*args, **kwargs):
        uiabstract.ChildUI.__init__(self, *args, **kwargs)

        # data dictionary
        self.fields = None

