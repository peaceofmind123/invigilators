import mysql.connector as connector
import tkinter as tk
from tkinter import ttk
import homeui


class ViewUI(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self,*args,**kwargs)


if __name__ == "__main__":

    home_ui = homeui.HomeUI()
    home_ui.wm_title("Invigilators Database")
    home_ui.mainloop()



