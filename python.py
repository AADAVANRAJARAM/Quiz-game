from tkinter import *
from tkinter import ttk
y= 0
a = ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root =ttk.Frame(a)

def quiz(y):
    a.add(frame1,text="Q1")
    a.add(frame2,text="Q2")
    a.add(frame3,text="Q3")
    a.add(frame4,text="Q4")
    a.add(frame5,text="Q5")

    Label(frame1,text="Encapsulation means?",font=("Segoe Script",50,)).grid(row=2,column=2)
    Button(frame1,text="Data hiding",font=("Segoe Script",30,"bold"),bg="light blue",command=a1_right).grid(row=3,column=1)
    Button(frame1,text="Data binding",font=("Segoe Script",30,"bold"),bg="light green",command=a1_wrong).grid(row=3,column=2)
    Button(frame1,text="Data abstraction",font=("Segoe Script",30,"bold"),bg="light pink",command=a1_wrong).grid(row=3,column=3)

    
    Label(frame2,text="s='HarryStyles'print(s[1:3])",font=("Segoe Script",50,"bold")).grid(row=2,column=2)
    Button(frame2,text="Har",font=("Segoe Script",30,"bold"),bg="light blue",command=a2_wrong).grid(row=3,column=1)
    Button(frame2,text="arr",font=("Segoe Script",30,"bold"),bg="light green",command=a2_right).grid(row=3,column=2)
    Button(frame2,text="rry",font=("Segoe Script",30,"bold"),bg="light pink",command=a2_wrong).grid(row=3,column=3)
    
    Label(frame3,text="Public,Private,Protected are?",font=("Segoe Script",50,"bold")).grid(row=2,column=2)
    Button(frame3,text="Members",font=("Segoe Script",30,"bold"),bg="light blue",command=a3_right).grid(row=3,column=1)
    Button(frame3,text="Objects",font=("Segoe Script",30,"bold"),bg="light green",command=a3_wrong).grid(row=3,column=2)
    Button(frame3,text="Function",font=("Segoe Script",30,"bold"),bg="light pink",command=a3_wrong).grid(row=3,column=3)
 
    Label(frame4,text="Keyword use to declare a function",font=("Segoe Script",50,"bold")).grid(row=2,column=2)
    Button(frame4,text="define",font=("Segoe Script",30,"bold"),bg="light blue",command=a4_wrong).grid(row=3,column=1)
    Button(frame4,text="def",font=("Segoe Script",30,"bold"),bg="light green",command=a4_right).grid(row=3,column=2)
    Button(frame4,text="None",font=("Segoe Script",30,"bold"),bg="light pink",command=a4_wrong).grid(row=3,column=3)

    Label(frame5,text="Output of 2*12 ?",font=("Segoe Script",50,"bold")).grid(row=2,column=2)
    Button(frame5,text="24",font=("Segoe Script",30,"bold"),bg="light blue",command=a5_right).grid(row=3,column=1)
    Button(frame5,text="28",font=("Segoe Script",30,"bold"),bg="light green",command=a5_wrong).grid(row=3,column=2)
    Button(frame5,text="32",font=("Segoe Script",30,"bold"),bg="light pink",command=a5_wrong).grid(row=3,column=3)


def a1_right():
    Label(frame1,text="Correct",font=("Segoe Script",40,"bold"),fg="green").grid(row=1,column=2)
    Label(frame1,text="Marks Obtained = 1",font=("Calibri",40,"bold")).grid(row=4,column=2)

def a1_wrong():
    Label(frame1,text="Incorrect",font=("Segoe Script",40,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="Marks Obtained = 0",font=("Calibri",40,"bold")).grid(row=4,column=2)

def a2_right():
    Label(frame2,text="Correct",font=("Segoe Script",40,"bold"),fg="green").grid(row=1,column=2)
    Label(frame2,text="Marks Obtained = 1",font=("Calibri",40,"bold")).grid(row=4,column=2)

def a2_wrong():
    Label(frame2,text="Incorrect",font=("Segoe Script",40,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="Marks Obtained = 0",font=("Calibri",40,"bold")).grid(row=4,column=2)

def a3_right():
    Label(frame3,text="Correct",font=("Segoe Script",40,"bold"),fg="green").grid(row=1,column=2)
    Label(frame3,text="Marks Obtained = 1",font=("Calibri",40,"bold")).grid(row=4,column=2)

def a3_wrong():
    Label(frame3,text="Incorrect",font=("Segoe Script",40,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame3,text="Marks Obtained = 0",font=("Calibri",40,"bold")).grid(row=4,column=2)

def a4_right():
    Label(frame4,text="Correct",font=("Segoe Script",40,"bold"),fg="green").grid(row=1,column=2)
    Label(frame4,text="Marks Obtained = 1",font=("Calibri",40,"bold")).grid(row=4,column=2)

def a4_wrong():
    Label(frame4,text="Incorrect",font=("Segoe Script",40,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame4,text="Marks Obtained = 0",font=("Calibri",40,"bold")).grid(row=4,column=2)    

def a5_right():
    Label(frame5,text="Correct",font=("Segoe Script",40,"bold"),fg="green").grid(row=1,column=2)
    Label(frame5,text="Marks Obtained = 1",font=("Calibri",40,"bold")).grid(row=4,column=2)

def a5_wrong():
    Label(frame5,text="Incorrect",font=("Segoe Script",40,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame5,text="Marks Obtained = 0",font=("Calibri",40,"bold")).grid(row=4,column=2)    


quiz(y)   
a.pack()
a.mainloop()
