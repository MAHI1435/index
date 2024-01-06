from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total= str(eval(expression))

        equation.set(total)
        expression = ""

    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


pro= Tk()
pro.geometry("410x350")
pro.title("Python Calculator")


equation= StringVar()
p1= Entry(pro,textvariable= equation, bd=12, bg= "gray", font= "arial 26", justify= "right")
p1.grid(row=0, columnspan= 4)



btn7=Button(pro, text="7", font="arial 14 bold", bd= 15, command=lambda: press(7), height=1, width=5)
btn7.grid(row=1, column=0)

btn8=Button(pro, text="8", font="arial 14 bold",   bd= 15, command=lambda: press(8), height=1, width=5)
btn8.grid(row=1, column=1)

btn9=Button(pro, text="9", font="arial 14 bold", bd= 15, command=lambda: press(9), height=1, width=5)
btn9.grid(row=1, column=2)

btnadd=Button(pro, text="+", font="arial 14 bold", bd= 15, command=lambda: press("+"), height=1, width=5)
btnadd.grid(row=1, column=3)



btn4=Button(pro, text="4", font="arial 14 bold", bd= 15, command=lambda: press(4), height=1, width=5)
btn4.grid(row=2, column=0)

btn5=Button(pro, text="5", font="arial 14 bold", bd= 15, command=lambda: press(5), height=1, width=5)
btn5.grid(row=2, column=1)

btn6=Button(pro, text="6", font="arial 14 bold", bd= 15, command=lambda: press(6), height=1, width=5)
btn6.grid(row=2, column=2)

btnsub=Button(pro, text="-", font="arial 14 bold", bd= 15, command=lambda: press("-"),  height=1, width=5)
btnsub.grid(row=2, column=3)



btn1=Button(pro, text="1", font="arial 14 bold", bd= 15, command=lambda: press(1), height=1, width=5)
btn1.grid(row=3, column=0)

btn2=Button(pro, text="2", font="arial 14 bold", bd= 15, command=lambda: press(2), height=1, width=5)
btn2.grid(row=3, column=1)

btn3=Button(pro, text="3", font="arial 14 bold", bd= 15, command=lambda: press(3), height=1, width=5)
btn3.grid(row=3, column=2)

btnmul=Button(pro, text="*", font="arial 14 bold", bd= 15, command=lambda: press("*"),  height=1, width=5)
btnmul.grid(row=3, column=3)



btncancel=Button(pro, text="C", font="arial 14 bold", bd= 15, command=clear, height=1, width=5)
btncancel.grid(row=4, column=0)

btnzero=Button(pro, text="0", font="arial 14 bold", bd= 15, command=lambda: press(0), height=1, width=5)
btnzero.grid(row=4, column=1)

btndiv=Button(pro, text="/", font="arial 14 bold", bd= 15, command=lambda: press("/"), height=1, width=5)
btndiv.grid(row=4, column=2)

btnequal=Button(pro, text="=", font="arial 14 bold", bd= 15, command=equalpress, height=1, width=5)
btnequal.grid(row=4, column=3)

pro.mainloop()
