from tkinter import *
import tkinter.messagebox


#create the window.
root = Tk()
root.configure(background='black')
root.title("My calculator")

#create the output line.

e =  Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0, columnspan=3, padx=10,pady=20)

def click(number):
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current) + str(number))

        return

def clear():
        e.delete(0,END)
        return


def add():
        num=e.get()
        global first
        global math
        math="+"
        first=int(num)
        e.delete(0,END)

def equal():

        secondNum=e.get()
        e.delete(0,END)
        if math=="+":
                e.insert(0,first + int(secondNum))
        if math=="x":
                e.insert(0,first * int(secondNum))
        if math=="/":
                e.insert(0,first / int(secondNum))
        if math=="-":
                e.insert(0,first - int(secondNum))
        if math=='sqrt':
                e.insert(0,first**0.5)
        if math=='factorial':
                e.insert(0,fct)

        return

def subtract():
        num=e.get()
        global first
        global math
        math="-"
        first=int(num)
        e.delete(0,END)
        return




def multiply():
        num=e.get()
        global first
        global math
        math="x"
        first=int(num)
        e.delete(0,END)

        return


def divide():
        num=e.get()
        global first
        global math
        math="/"
        first=int(num)
        e.delete(0,END)

        return
def sqrt():
        num=e.get()
        global first
        global math
        math='sqrt'
        first=int(num)
        e.delete(0, END)
        return


def factorial():
        num=e.get()
        global first
        global math
        global fct
        math='factorial'
        first = int(num)
        fct=1
        for i in range(1,first+1):
                fct=fct*i
        e.delete(0,END)


        return



def backspace():
        num=e.get()
        l=len(num)
        e.delete(l-1,END)
        return






#Define number buttons.
button_1 = Button(root, text='1',bg='darkblue',fg='white', padx=50, pady=20, command=lambda:click(1))
button_2 = Button(root, text='2',bg='darkblue',fg='white', padx=55, pady=20, command=lambda:click(2))
button_3 = Button(root, text='3',bg='darkblue',fg='white', padx=50, pady=20, command=lambda:click(3))
button_4 = Button(root, text='4',bg='darkblue',fg='white', padx=50, pady=20, command=lambda:click(4))
button_5 = Button(root, text='5',bg='darkblue',fg='white', padx=55, pady=20, command=lambda:click(5))
button_6 = Button(root, text='6',bg='darkblue',fg='white', padx=50, pady=20, command=lambda:click(6))
button_7 = Button(root, text='7',bg='darkblue',fg='white', padx=50, pady=20, command=lambda:click(7))
button_8 = Button(root, text='8',bg='darkblue',fg='white', padx=55, pady=20, command=lambda:click(8))
button_9 = Button(root, text='9',bg='darkblue',fg='white', padx=50, pady=20, command=lambda:click(9))
button_0 = Button(root, text='0',bg='darkblue',fg='white', padx=50, pady=23, command=lambda:click(0))

#Define symbols buttons.
button_add = Button(root, text='+',bg='darkslategray', fg='white',font='sans 12 bold', padx=50, pady=25, command=add)
button_equal = Button(root, text='=',bg='darkslategray', fg='white',font='sans 14 bold', padx=45, pady=20, command=equal)
button_clear = Button(root, text='clear',bg='darkslategray', fg='white',font='sans 12 bold', padx=35, pady=20, command=clear)
button_sub = Button(root, text='-',bg='darkslategray', fg='white',font='sans 12 bold', padx=55, pady=25, command=subtract)
button_mult = Button(root, text='x',bg='darkslategray', fg='white',font='sans 12 bold', padx=50, pady=25, command=multiply)
button_div = Button(root, text='/',bg='darkslategray', fg='white',font='sans 12 bold', padx=45, pady=20, command=divide)
button_sqrt = Button(root, text='sqrt',bg='darkslategray', fg='white', font='sans 12 bold',padx=35, pady=20, command=sqrt)
button_fact =  Button(root, text='n!',bg='darkslategray', fg='white', font='sans 12 bold' , padx=50,pady=20, command=factorial)
button_backSpace = Button(root, text='<<',bg='darkslategray', fg='white', font='sans 12 bold', padx=45, pady=20, command=backspace)


#Put buttons on the screen

button_1.grid(row=3 , column=0 )
button_2.grid(row=3 , column=1 )
button_3.grid(row=3, column=2 )

button_4.grid(row=2 , column=0 )
button_5.grid(row= 2, column=1 )
button_6.grid(row=2 , column=2 )

button_7.grid(row=1 , column=0 )
button_8.grid(row=1 , column=1 )
button_9.grid(row=1 , column=2 )

button_0.grid(row=4 , column=0 )
button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)


button_sub.grid(row=5, column=1)
button_mult.grid(row=5,column=2)
button_div.grid(row=6,column=0)

button_sqrt.grid(row=6,column=0)
button_fact.grid(row=6, column=1)
button_backSpace.grid(row=6, column=2)




root.mainloop()

