from tkinter import*
def caseClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def caseClearTextDisplay():
    global operator
    operator=""
    text_Input.set("")
def caseEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
root=Tk()
root.title("Calulator")
operator=""
text_Input=StringVar()
txtDisplay=Entry(root,font=('arial',20,'bold'),textvariable=text_Input, bd=35, insertwidth=4,bg="light Grey", justify='right').grid(columnspan=4)
case7=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="7",command=lambda:caseClick(7),bg="Brown",bd=10).grid(row=1,column=0)
case8=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="8",command=lambda:caseClick(8),bg="Brown",bd=10).grid(row=1,column=1)
case9=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="9",command=lambda:caseClick(9),bg="Brown",bd=10).grid(row=1,column=2)
Addition=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="+",command=lambda:caseClick("+"),bg="Brown",bd=10).grid(row=1,column=3)
case4=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="4",command=lambda:caseClick(4),bg="Brown",bd=10).grid(row=2,column=0)
case5=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="5",command=lambda:caseClick(5),bg="Brown",bd=10).grid(row=2,column=1)
case6=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="6",command=lambda:caseClick(6),bg="Brown",bd=10).grid(row=2,column=2)
Substract=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="-",command=lambda:caseClick("-"),bg="Brown",bd=10).grid(row=2,column=3)
case1=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="1",command=lambda:caseClick(1),bg="Brown",bd=10).grid(row=3,column=0)
case2=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="2",command=lambda:caseClick(2),bg="Brown",bd=10).grid(row=3,column=1)
case3=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="3",command=lambda:caseClick(3),bg="Brown",bd=10).grid(row=3,column=2)
Multiply=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="*",command=lambda:caseClick("*"),bg="Brown",bd=10).grid(row=3,column=3)
case0=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="0",command=lambda:caseClick(0),bg="Brown",bd=10).grid(row=4,column=0)
caseClears=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="C",bd=10,bg="Brown",command=caseClearTextDisplay).grid(row=4,column=1)
Divide=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="/",bd=10,command=lambda:caseClick("/"),bg="Brown").grid(row=4,column=2)
caseEquals=Button(root,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text="=",bg="Brown",bd=10,command=caseEqualsInput,).grid(row=4,column=3)
root.mainloop()