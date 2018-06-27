import tkinter as tk
from tkinter import ttk
import ui_subject as uisub
import ui_staff as uistaff
import ui_invigilator as uiinv
import ui_examhall as uiexamhall
import ui_exam as uiexam
import ui_class as uiclass
import ui_examinstance as uiexaminstance
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
            self.update_UI = uisub.DisplayUpdateSubjectUI()
        elif key == self.BTNEXAMINSTANCEKEY:
            self.update_UI = uiexaminstance.DisplayUpdateExaminstanceUI()
        elif key == self.BTNCLASSKEY:
            self.update_UI = uiclass.DisplayUpdateClassUI()
        elif key == self.BTNEXAMKEY:
            self.update_UI = uiexam.DisplayUpdateExamUI()
        elif key == self.BTNEXAMHALLKEY:
            self.update_UI = uiexamhall.DisplayUpdateExamhallUI()
        elif key == self.BTNINVIGILATORKEY:
            self.update_UI = uiinv.DisplayUpdateInvigilatorUI()
        elif key == self.BTNSTAFFKEY:
            self.update_UI = uistaff.DisplayUpdateStaffUI()




