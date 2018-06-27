import tkinter as tk
from tkinter import ttk
import updateui_subject as updatesub
import updateui_staff as updatestaff
import updateui_invigilator as updateinv
import updateui_examhall as updateexamhall
import updateui_exam as updateexam
import updateui_class as updateclass
import updateui_examinstance as updateexaminstance
import uiabstract


class HomeUI(uiabstract.ParentUI):
    def __init__(self, *args, **kwargs):
        uiabstract.ParentUI.__init__(self, *args, **kwargs)
        # child UI definitions
        self.update_UI = None


        self.mainLabel = ttk.Label(self.container, text="Please select a collection")

        # button constants
        self.BTNSUBKEY = 0
        self.BTNSTAFFKEY = 1
        self.BTNINVIGILATORKEY = 2
        self.BTNEXAMHALLKEY = 3
        self.BTNEXAMKEY = 4
        self.BTNCLASSKEY = 5
        self.BTNEXAMINSTANCEKEY = 6

        # buttons
        self.btn_subject = ttk.Button(self.container, text="Subjects", command=lambda: self.btn_handler(self.BTNSUBKEY))
        self.btn_staff = ttk.Button(self.container, text="Staffs", command=lambda: self.btn_handler(self.BTNSTAFFKEY))
        self.btn_invigilator = ttk.Button(self.container, text="Invigilators",
                                          command=lambda: self.btn_handler(self.BTNINVIGILATORKEY))
        self.btn_examhall = ttk.Button(self.container, text="Examhalls",
                                       command=lambda: self.btn_handler(self.BTNEXAMHALLKEY))
        self.btn_exam = ttk.Button(self.container, text="Exams", command=lambda: self.btn_handler(self.BTNEXAMKEY))
        self.btn_class = ttk.Button(self.container, text="Classes", command=lambda: self.btn_handler(self.BTNCLASSKEY))
        self.btn_examinstance = ttk.Button(self.container, text="Exam instances",
                                           command=lambda: self.btn_handler(self.BTNEXAMINSTANCEKEY))

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
        for child in self.container.winfo_children():
            child.grid_configure(padx=10, pady=20)

        # click event handlers

    def btn_handler(self, key):
        if key == self.BTNSUBKEY:
            self.update_UI = updatesub.UpdateSubjectForm()
        elif key == self.BTNEXAMINSTANCEKEY:
            self.update_UI = updateexaminstance.UpdateExaminstanceForm()
        elif key == self.BTNCLASSKEY:
            self.update_UI = updateclass.UpdateClassForm()
        elif key == self.BTNEXAMKEY:
            self.update_UI = updateexam.UpdateExamForm()
        elif key == self.BTNEXAMHALLKEY:
            self.update_UI = updateexamhall.UpdateExamhallForm()
        elif key == self.BTNINVIGILATORKEY:
            self.update_UI = updateinv.UpdateInvigilatorForm()
        elif key == self.BTNSTAFFKEY:
            self.update_UI = updatestaff.UpdateStaffForm()




