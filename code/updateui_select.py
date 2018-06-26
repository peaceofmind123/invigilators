import tkinter as tk
from tkinter import ttk
import updateui_subject as updatesub
import updateui_staff as updatestaff
import updateui_invigilator as updateinv
import updateui_examhall as updateexamhall
import updateui_exam as updateexam
import updateui_class as updateclass
import updateui_examinstance as updateexaminstance

class UpdateUISelect(tk.Toplevel):  # toplevel since these will inevitably be children windows
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        # constants
        self.FRAME_WIDTH = 1024
        self.FRAME_HEIGHT = 768

        # container widget
        self.container = tk.Frame(self, width=self.FRAME_WIDTH, height=self.FRAME_HEIGHT)

        # label
        self.mainLabel = ttk.Label(text="Please select the collection to update:")

        # button constants
        self.BTNSUBKEY = 0
        self.BTNSTAFFKEY = 1
        self.BTNINVIGILATORKEY = 2
        self.BTNEXAMHALLKEY = 3
        self.BTNEXAMKEY = 4
        self.BTNCLASSKEY = 5
        self.BTNEXAMINSTANCEKEY = 6

        # buttons
        self.btn_subject = ttk.Button(self, text="Subjects", command=lambda: self.btn_handler(self.BTNSUBKEY))
        self.btn_staff = ttk.Button(self, text="Staffs", command=lambda: self.btn_handler(self.BTNSTAFFKEY))
        self.btn_invigilator = ttk.Button(self, text="Invigilators", command=lambda : self.btn_handler(self.BTNINVIGILATORKEY))
        self.btn_examhall = ttk.Button(self, text="Examhalls", command=lambda : self.btn_handler(self.BTNEXAMHALLKEY))
        self.btn_exam = ttk.Button(self, text="Exams", command=lambda : self.btn_handler(self.BTNEXAMKEY))
        self.btn_class = ttk.Button(self, text="Classes", command=lambda : self.btn_handler(self.BTNCLASSKEY))
        self.btn_examinstance = ttk.Button(self, text="Exam instances", command=lambda : self.btn_handler(self.BTNEXAMINSTANCEKEY))

        # layout
        self.mainLabel.grid(row=0, columnspan=3)
        self.btn_subject.grid(row=1)
        self.btn_staff.grid(row=1, column=1)
        self.btn_invigilator.grid(row=1, column=2)
        self.btn_examhall.grid(row=2)
        self.btn_exam.grid(row=2, column=1)
        self.btn_class.grid(row=2, column=2)
        self.btn_examinstance.grid(row=3)

        # padding configuration
        for child in self.container.children:
            child.grid_configure(padx=10, pady=20)

        # click event handlers
    def btn_handler(self,key):
        if key == self.BTNSUBKEY:
            self.master.update_UI = updatesub.UpdateSubForm()
        elif key == self.BTNEXAMINSTANCEKEY:
            self.master.update_UI = updateexaminstance.UpdateExaminstanceForm()
        elif key == self.BTNCLASSKEY:
            self.master.update_UI = updateclass.UpdateClassForm()
        elif key == self.BTNEXAMKEY:
            self.master.update_UI = updateexam.UpdateExamForm()
        elif key == self.BTNEXAMHALLKEY:
            self.master.update_UI = updateexamhall.UpdateExamhallForm()
        elif key == self.BTNINVIGILATORKEY:
            self.master.update_UI = updateinv.UpdateInvigilatorForm()
        elif key == self.BTNSTAFFKEY:
            self.master.update_UI = updatestaff.UpdateStaffForm()
        self.master.mainloop()
        self.destroy()


