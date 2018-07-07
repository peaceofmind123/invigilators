import tkinter as tk
from tkinter import ttk
import uiabstract
import math
import mysql.connector.errors as mysqlerrors
import mysql
import copy
# the abstract update form class
class DisplayUpdateUI(uiabstract.ChildUI):
    def __init__(self, *args, **kwargs):
        uiabstract.ChildUI.__init__(self, *args, **kwargs)

        # data dictionary
        self.fields = {}

        # rows
        self.rows = []

        # data types info
        self.dataTypes = {}
        # name to identify the table.. since the class is polymorphic
        self.tableName = None
        self.rowsAdded = 0

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
                self.rows.append(list(row))
                for column in row:
                    self.fields[column_names[index]].append(row[index])
                    index += 1

            # getting data types
            self.cursor.execute("select DATA_TYPE from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+table+"';")
            i = 0
            datatypes = self.cursor.fetchall()
            for key,value in self.fields.items():
                self.dataTypes[key] = datatypes[i][0]
                i+=1

    def getRows(self):
        # input: {key1: [a1,a2,...,aj],key2:[b1,b2,...,bj],...,keyi:[x1,x2...xi],...}
        # output: rows[[a1,b1...x1..],[a2,b2...x2,...],..,[aj,bj,...xj]...]
        self.rows = []
        i = 0

        for key, value in self.fields.items():
            for j in range(len(value)):
                if i == 0:
                    self.rows.append([])
                self.rows[j].append(value[j])
            i += 1
        return self.rows

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

            self.finalRowNum =0
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


                    entry = tk.Entry(self.container, textvariable=self.dataTextVarMat[c][j],state="readonly")
                    self.dataEntryMat[c].append(entry)
                    self.dataEntryMat[c][j].grid(row=j + 2, column=c)
                    self.finalRowNum = j + 2
                # increasing the column number for the next iteration
                c += 1
            self.btnEdit = ttk.Button(self.container,text="Edit entries",command=self.btnEditHandler)
            self.btnSave = ttk.Button(self.container,text="Save entries",command=self.btnSaveHandler)
            self.btnAdd = ttk.Button(self.container,text="Add entry",command=self.btnAddHandler)
            num_of_cols = len(self.fields)
            self.btnEdit.grid(row=self.finalRowNum + 1, column = 0)
            self.btnSave.grid(row=self.finalRowNum + 1, column = 1)
            self.btnAdd.grid(row=self.finalRowNum + 1, column=2)
            self.btnSave['state'] = 'disabled'

    def btnEditHandler(self):
        for i in range(len(self.dataEntryMat)):
            for j in range(len(self.dataEntryMat[i])):
                (self.dataEntryMat[i][j])['state'] = 'normal'
        self.btnSave['state'] = 'normal'

    def btnSaveHandler(self):
        if self.rowsAdded > 0:
            for i in range(self.rowsAdded):
                c = 0
                for key, value in self.fields.items():

                    val = self.dataEntryMat[c][len(value)+i].get()
                    if self.dataTypes[key] == "int": # to be verified
                        value.append(int(val))
                    else:
                        value.append(val)

                    c += 1
        # getting the names of the primary key fields
        self.cursor.execute("SHOW KEYS FROM "+self.tableName+" WHERE Key_name = 'PRIMARY'")
        primary_cols_info = self.cursor.fetchall()
        primary_cols_names=[] # this array contains the names of the columns of the superkey

        # saving the primary key values for where clause reference
        primary_key_vals = {}
        i=0
        for entry in primary_cols_info:
            primary_cols_names.append(entry[4]) # the column name is the fourth entry in the info data
            primary_key_vals[primary_cols_names[i]] = copy.deepcopy(self.fields[primary_cols_names[i]]) # deepcopy reqd
            i+=1

        # updating the self.fields data structure according to user input
        c = 0

        for key, value in self.fields.items():
            dataCurr = self.dataEntryMat[c]
            for r in range(len(dataCurr)):
                value[r] = dataCurr[r].get()

            c += 1

        # flattening the data structure into rows
        self.getRows()

        # if rows are added run an add query
        if self.rowsAdded > 0:
            for i in range(self.rowsAdded):
                count=1
                addQueryString = "insert into "+self.tableName+" ("
                for key,value in self.fields.items():
                    addQueryString += key
                    if (count != len(self.rows[0])):
                        addQueryString += ", "
                    else:
                        addQueryString += ") values ("
                    count += 1

                count=1
                for key,value in self.fields.items():
                    addQueryString+="'"
                    addQueryString += value[len(value)-i-1] # since the value already contains the values
                    addQueryString += "'"
                    if count != len(self.rows[0]):
                        addQueryString += ", "
                    else:
                        addQueryString += ");"
                    count += 1
                try:
                    self.cursor.execute(addQueryString)
                    self.connection.commit()
                except mysqlerrors.Error as e:
                    print(e)
                    self.connection.rollback()
        # the final update query
        i=0
        for row in self.rows:
            queryString = "update " + self.tableName + " set "
            j=0
            for key,value in self.fields.items():
                queryString+=key
                queryString+="="
                if self.dataTypes[key]=="varchar" or self.dataTypes[key]=="date":
                    queryString+="'"

                queryString+=str(row[j])
                if self.dataTypes[key]=="varchar" or self.dataTypes[key]=="date":
                    queryString+="'"

                # except for the last key=value declaration, append a comma at the end
                if j!=len(row)-1:
                    queryString+=", "
                j += 1

            queryString+=" where "
            l=0
            for name in primary_cols_names:
                queryString += name+"="
                if self.dataTypes[name] == "varchar" or self.dataTypes[name]=="date":
                    queryString += "'"

                queryString += str(primary_key_vals[name][i]) # since i is the row number
                if self.dataTypes[name] == "varchar" or self.dataTypes[name]=="date":
                    queryString += "'"

                if l!=len(primary_cols_names)-1:
                    queryString+=" and "
                else:
                    queryString+=";"
                l+=1
            i+=1
            self.btnSave['state']='disabled'
            for k in range(len(self.dataEntryMat)):
                for l in range(len(self.dataEntryMat[i])):
                    (self.dataEntryMat[k][l])['state'] = 'readonly'

            # try to execute the query, if fails roll it back
            try:
                print(queryString)
                self.cursor.execute(queryString)
                self.connection.commit()

            except mysqlerrors.Error as e:

                print(e)

    def btnAddHandler(self):
        # the column iterator, again
        c=0
        self.rowsAdded += 1
        for key, value in self.fields.items():

            entry = tk.Entry(self.container)
            self.dataEntryMat[c].append(entry)

            self.dataEntryMat[c][len(value)].grid(row=len(value)+2,column=c)
            if c == 0:
                self.btnEdit.grid(row=len(value) + 3, column=0)
                self.btnSave.grid(row=len(value) + 3, column=1)
                self.btnAdd.grid(row=len(value) + 3, column=2)
            c += 1

        self.btnSave['state'] = 'normal'