#https://python-decompiler.com/article/2011-09/switch-between-two-frames-in-tkinter

import tkinter as tk                # python 3
from tkinter import *
from tkinter import font  as tkfont # python 3
from tkinter import messagebox
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import mysql.connector

exp = ""

def press(num, entered_code):
    global exp
    exp=exp + str(num)
    entered_code.set(exp)

def clear(entered_code):
    global exp
    exp = ""
    entered_code.set(exp)

def verify_code(test_label, code):
    code_func = code.get()
    try:
        mySQLConnection = mysql.connector.connect(host='buildingaccess.cuzrbhg1j8lc.us-east-1.rds.amazonaws.com',
                                                  database='building_access',
                                                  user='casciofil',
                                                  password='buildingaccessdbpass1')
        cursor = mySQLConnection.cursor(buffered=True)
        sql_select_query = "SELECT * FROM codes WHERE access_code = %s"
        cursor.execute(sql_select_query, (code_func,))
        result = cursor.fetchall()

        if result:
            if(result[0][7]=="active"):
                test_label.config(text="CODE RIGHT!")
                
                if(result[0][5]=="one"):
                    sql_update_query = "UPDATE codes SET status = 'expired' WHERE access_code = %s"
                    cursor.execute(sql_update_query, (code_func,))
                    mySQLConnection.commit()
            else:
                test_label.config(text="CODE EXPIRED!")
        else:
            test_label.config(text="CODE WRONG!")
        

    finally:
        if (mySQLConnection.is_connected()):
            cursor.close()
            mySQLConnection.close()



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        

        self.frames = {}
        for F in (StartPage, Visitor_class, Tenant_class):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

     


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = '#BBCEA8')
        self.controller = controller
        frame = Frame(self, bg="#BBCEA8")
        frame.pack()

        topframe = Frame(frame, bd=10, bg="#BBCEA8") 
        topframe.pack()  
        
        leftframe = Frame(frame, bd=50, bg="#BBCEA8")  
        leftframe.pack(side = LEFT)  
        
        rightframe = Frame(frame, bd=50, bg="#BBCEA8")  
        rightframe.pack(side = RIGHT)  
        
        address = Label(topframe, text="15 Broadway, Ultimo", font = "Verdana 40 bold", bg="#BBCEA8", fg="#0F0E0E")
        address.pack()

        tenant_btn = Button(leftframe, text="Tenant", width=14, height=4, highlightbackground="#272838", font=('Helvetica', '20'), command=lambda: controller.show_frame("Tenant_class"))
        tenant_btn.pack(side=RIGHT) 

        visitor_btn = Button(rightframe, text="Visitor", width=14, height=4, highlightbackground="#272838", font=('Helvetica', '20'), command=lambda: controller.show_frame("Visitor_class"))
        visitor_btn.pack(side=LEFT)


class Tenant_class(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()



class Visitor_class(tk.Frame):
   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = '#BBCEA8')
        self.controller = controller

        
        frame = Frame(self, bg="#BBCEA8")
        frame.pack()

        leftframe = Frame(frame, bg="#BBCEA8") 
        leftframe.pack(side=LEFT, padx=40)   
        
        rightframe = Frame(frame, bg="#BBCEA8", bd=10)  
        rightframe.pack(side=RIGHT)  

        entered_code = StringVar()

        code_label = Label(leftframe, text="Insert Code:", bg="#BBCEA8", font = "Verdana 20")
        code_label.grid(row=0, column=0)
        code_entry = Entry(leftframe, textvariable = entered_code)
        code_entry.grid(row=1, column=0)
        test_label = Label(leftframe, text="")
        enter_btn = Button(leftframe, text="Enter", width=13, height=4, command = lambda : verify_code(test_label, entered_code))
        enter_btn.grid(row=3, column=0, pady=15)
        test_label.grid(row=4, column=0)

        empty_btn = Button(rightframe, text=" ", width=4, height=4)
        empty_btn.grid(column=0, row = 3)
        zero_btn = Button(rightframe, text="0", width=4, height=4, command = lambda : press('0', entered_code))
        zero_btn.grid(column=1, row = 3)
        backspace_btn = Button(rightframe, text="<", width=4, height=4, command = lambda : clear(entered_code))
        backspace_btn.grid(column=2, row = 3)
        one_btn = Button(rightframe, text="1", width=4, height=4, command = lambda : press('1', entered_code))
        one_btn.grid(column=0, row = 2)
        two_btn = Button(rightframe, text="2", width=4, height=4, command = lambda : press('2', entered_code))
        two_btn.grid(column=1, row = 2)
        three_btn = Button(rightframe, text="3", width=4, height=4, command = lambda : press('3', entered_code))
        three_btn.grid(column=2, row = 2)
        four_btn = Button(rightframe, text="4", width=4, height=4, command = lambda : press('4', entered_code))
        four_btn.grid(column=0, row = 1)
        five_btn = Button(rightframe, text="5", width=4, height=4, command = lambda : press('5', entered_code))
        five_btn.grid(column=1, row = 1)
        six_btn = Button(rightframe, text="6", width=4, height=4, command = lambda : press('6', entered_code))
        six_btn.grid(column=2, row = 1)
        seven_btn = Button(rightframe, text="7", width=4, height=4, command = lambda : press('7', entered_code))
        seven_btn.grid(column=0, row = 0)
        eight_btn = Button(rightframe, text="8", width=4, height=4, command = lambda : press('8', entered_code))
        eight_btn.grid(column=1, row = 0)
        nine_btn = Button(rightframe, text="9", width=4, height=4, command = lambda : press('9', entered_code))
        nine_btn.grid(column=2, row = 0)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()