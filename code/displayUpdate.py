import tkinter as tk
from tkinter import ttk
import uiabstract
import math
import mysql.connector.errors as mysqlerrors
# the abstract update form class
class DisplayUpdateUI(uiabstract.ChildUI):
    def __init__(self, *args, **kwargs):
        uiabstract.ChildUI.__init__(self, *args, **kwargs)

        # data dictionary
        self.fields = {}

        # rows
        self.rows = []
        # name to identify the table.. since the class is polymorphic
        self.tableName = None

    # populates the self.fields object
    def get_data_structure(self, table):
        # storing the current table info
        self.tableName = table
        if self.cursor is not None:
            # getting the table descriptor object
            self.cursor.execute("desc " + table)
            column_names = []
            index = 0
            for descriptor in self.cursor.fetchall():
                column_names.insert(index, descriptor[0])  # descriptor[0] contains column name
                self.fields[column_names[index]] = []
                index += 1

            # getting values
            self.cursor.execute("select * from " + table)
            for row in self.cursor.fetchall():
                index = 0

                for column in row:
                    self.fields[column_names[index]].insert(index, row[index])
                    index += 1

    def displayData(self):
        if self.fields is not None:

            # the main label
            self.tableLabel = tk.Label(self.container, text=self.tableName)
            self.tableLabel.grid(row=0, column=0)

            # the widgets for columns and data
            self.columnLabels = []
            # the data entry widget matrix
            self.dataEntryMat = []
            # the corresponding text variable
            self.dataTextVarMat = []
            # row and column iterators for column labels
            r = 1
            c = 0

            # row iterator inside the loop

            # the label of the columns
            for key, value in self.fields.items():
                self.columnLabels.append(tk.Label(self.container, text=key))
                self.columnLabels[c].grid(row=r, column=c)
                self.dataEntryMat.append([])  # making the dataEntryMat 2 dimensional
                self.dataTextVarMat.append([])

                # now, the value is the column of data
                # j is the row iterator
                for j in range(len(value)):
                    # adding a stringvar object and setting its value
                    self.dataTextVarMat[c].append(tk.StringVar())
                    self.dataTextVarMat[c][j].set(value[j])
                    # populating the dataEntryMat

                    print(self.dataTextVarMat[c][j].get())
                    entry = tk.Entry(self.container, textvariable=self.dataTextVarMat[c][j],state="readonly")
                    self.dataEntryMat[c].append(entry)
                    self.dataEntryMat[c][j].grid(row=j + 2, column=c)
                    r = j + 2 # saving r for reference

                # increasing the column number for the next iteration
                c += 1
            self.btnEdit = ttk.Button(self.container,text="Edit entries",command=self.btnEditHandler)
            self.btnSave = ttk.Button(self.container,text="Save entries",command=self.btnSaveHandler)
            num_of_cols = len(self.fields)
            self.btnEdit.grid(row=r+1,column = 0,columnspan = math.floor(num_of_cols/2))
            self.btnSave.grid(row=r+1,column = 1,columnspan = num_of_cols-math.floor(num_of_cols/2))

    def getRows(self):
        # input: {key1: [a1,a2,...,aj],key2:[b1,b2,...,bj],...,keyi:[x1,x2...xi],...}
        # output: rows[[a1,b1...x1..],[a2,b2...x2,...],..,[aj,bj,...xj]...]
        self.rows=[]
        i=0

        for key, value in self.fields.items():
            for j in range(len(value)):
                if i==0:
                    self.rows.append([])
                self.rows[j].append(value[j])
            i+=1
        return self.rows

    def btnEditHandler(self):
        for i in range(len(self.dataEntryMat)):
            for j in range(len(self.dataEntryMat[i])):
                (self.dataEntryMat[i][j])['state'] = 'normal'


    def btnSaveHandler(self):

        # updating the self.fields data structure according to user input
        c=0
        for key, value in self.fields.items():
            dataCurr = self.dataTextVarMat[c]
            for r in range(len(dataCurr)):
                value[r] = dataCurr[r].get()

            c += 1

        # flattening the dictionary into rows
        self.getRows()
        # getting the names of the primary key fields
        self.cursor.execute("SHOW KEYS FROM "+self.tableName+" WHERE Key_name = 'PRIMARY'")
        primary_cols_info = self.cursor.fetchall()
        primary_cols_names=[] # this array contains the names of the columns of the superkey
        for entry in primary_cols_info:
            primary_cols_names.append(entry[4]) # the column name is the fourth entry in the info data

        # the final update query
        i=0
        for row in self.rows:
            queryString = "update " + self.tableName + " set "
            j=0
            for key,value in self.fields.items():
                queryString+=key
                queryString+="="+row[j]

                # except for the last key=value declaration, append a comma at the end
                if j!=len(row)-1:
                    queryString+=", "
                j += 1

            queryString+=" where "
            l=0
            for name in primary_cols_names:
                queryString += name+"="
                queryString += self.fields[name][i] # since i is the row number
                if l!=len(primary_cols_names)-1:
                    queryString+=", "
                else:
                    queryString+=";"
                l+=1
            i+=1

            # try to execute the query, if fails roll it back
            try:
                self.cursor.execute(queryString)
                self.cursor.execute('COMMIT')
                print("Update successful")
            except mysqlerrors.ProgrammingError:
                self.cursor.execute('COMMIT')
                print("Update Failed")

        self.connection.close()

