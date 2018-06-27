import tkinter as tk
from tkinter import ttk


class ParentUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.relx = .5
        self.rely = .4

        # getting the params
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "relx":
                    self.relx = value
                elif key == "rely":
                    self.rely = value


        # configuration
        self.resizable(False,False)
        # containers
        self.outercontainer = tk.Frame(self, width=400, height=400)
        self.outercontainer.pack(fill="both", expand=True)
        self.container = tk.Frame(self.outercontainer)
        self.container.place(in_=self.outercontainer, anchor="c", relx=.5, rely=.4)
        self.outercontainer.pack_propagate(0)


class ChildUI(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.relx = .5
        self.rely = .4

        # getting the params
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "relx":
                    self.relx = value
                elif key == "rely":
                    self.rely = value

        # configuration
        self.resizable(False, False)
        # containers
        self.outercontainer = tk.Frame(self, width=400, height=400)
        self.outercontainer.pack(fill="both", expand=True)
        self.container = tk.Frame(self.outercontainer)
        self.container.place(in_=self.outercontainer, anchor="c", relx=.5, rely=.4)
        self.outercontainer.pack_propagate(0)
