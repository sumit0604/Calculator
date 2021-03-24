from tkinter import *
import parser
import math


root = Tk()
root.title("Calculator")
root.geometry("225x360")
#getting input and put it into text field
i=0
def get_var(num):
    global i
    display.insert(i,num)
    i+=1
#deleten everthing from input area
def clear_all():
    display.delete(0,END)

#calculation
def calculation():
    entire_string = display.get()
    try:
        num = parser.expr(entire_string).compile()
        result = eval(num)
        clear_all()
        display.insert(0,result)
    except Exception as e:
        display.insert(0,"something went wrong")

#deleting an single element from input field
def undo():
    entire_string = display.get()

    if len(entire_string)> 0:
        new_String=entire_string[:-1]
        clear_all()
        display.insert(0,new_String)
    else:
        display.insert(0,"Error xxxxx")

#performing operator
def perf_operator(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
#square root
def square():
    num = display.get()
    root =math.sqrt(int(num))
    clear_all()
    display.insert(0,root)


#adding the input
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

#adding button in the calculator

Button(root,text="1",height=5,width=5,command =lambda :get_var(1)).grid(row=2,column=0)
Button(root,text="2",height=5,width=5,command =lambda :get_var(2)).grid(row=2,column=1)
Button(root,text="3",height=5,width=5,command =lambda :get_var(3)).grid(row=2,column=2)
Button(root,text="4",height=5,width=5,command =lambda :get_var(4)).grid(row=3,column=0)
Button(root,text="5",height=5,width=5,command =lambda :get_var(5)).grid(row=3,column=1)
Button(root,text="6",height=5,width=5,command =lambda :get_var(6)).grid(row=3,column=2)
Button(root,text="7",height=5,width=5,command =lambda :get_var(7)).grid(row=4,column=0)
Button(root,text="8",height=5,width=5,command =lambda :get_var(8)).grid(row=4,column=1)
Button(root,text="9",height=5,width=5,command =lambda :get_var(9)).grid(row=4,column=2)
Button(root,text="0",height=5,width=5,command =lambda :get_var(0)).grid(row=5,column=1)

Button(root,text="+",height=5,width=5,command =lambda :perf_operator("+")).grid(row=5,column=3)
Button(root,text="-",height=5,width=5,command =lambda :perf_operator("-")).grid(row=2,column=3)
Button(root,text="/",height=5,width=5,command =lambda :perf_operator("/")).grid(row=3,column=3)
Button(root,text="%",height=5,width=5,command =lambda :perf_operator("%")).grid(row=4,column=3)
Button(root,text="=",height=5,width=5,command =calculation).grid(row=5,column=2)

Button(root,text="*",height=5,width=5,command =lambda :perf_operator("*")).grid(row=2,column=4)
Button(root,text="**",height=5,width=5,command =lambda :perf_operator("**")).grid(row=3,column=4)
Button(root,text="sqrt",height=5,width=5,command = square).grid(row=4,column=4)
Button(root,text="del",height=5,width=5,command =undo).grid(row=5,column=4)
Button(root,text="AC",height=5,width=5,command =clear_all).grid(row=5,column=0)


root.mainloop()
