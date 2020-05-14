from tkinter import *
root = Tk()
root.title("Ashwini")
num_input= Entry(root,width=45, borderwidth= 2)
num_input.grid(row =0 , column =0, columnspan=4,pady=10,ipady=8)
global ip_op
ip_op = '+'
global f_num
f_num=0



def ip_num(num):
    #num_input.delete(0,END)
    if num != 'red':
        current = num_input.get()
        num_input.delete(0, END)
        num_input.insert(0, str(current)+str(num))
        #fnum = num_input.insert(0, str(current)+str(num))
        return
    else:
        num_input.delete(0, END)
        return


def add_func():
    global f_num
    first_num = num_input.get()
    f_num = first_num
    num_input.delete(0,END)
    global ip_op
    ip_op = '+'


def mult_func():
    first_num = num_input.get()
    global f_num
    f_num = first_num
    num_input.delete(0,END)
    global ip_op
    ip_op = 'x'


def div_func():
    first_num = num_input.get()
    global f_num
    f_num = first_num
    num_input.delete(0,END)
    global ip_op
    ip_op = '/'


def sub_func():
    first_num = num_input.get()
    global f_num
    f_num = first_num
    num_input.delete(0,END)
    global ip_op
    ip_op = '-'


def equal(ip_op):
    if ip_op == '+':
        second_num = num_input.get()
        num_input.delete(0,END)
        num_input.insert(0, int(f_num)+int(second_num))
    if ip_op == 'x':
        second_num = num_input.get()
        num_input.delete(0,END)
        num_input.insert(0, int(f_num)*int(second_num))
    if ip_op == '/':
        second_num = num_input.get()
        num_input.delete(0,END)
        num_input.insert(0, int(f_num)/int(second_num))
    if ip_op == '-':
        second_num = num_input.get()
        num_input.delete(0,END)
        num_input.insert(0, int(f_num)-int(second_num))

butf1 = Button(root, text="1", padx=30,pady=15, command=lambda: ip_num(1),bg='#add8e6').grid(row=1, column=0)
butf2 = Button(root, text="2", padx=30,pady=15, command=lambda: ip_num(2),bg='#add8e6').grid(row=1, column=1)
butf3 = Button(root, text="3", padx=30,pady=15, command=lambda: ip_num(3),bg='#add8e6').grid(row=1, column=2)
butf4 = Button(root, text="4", padx=30,pady=15, command=lambda: ip_num(4),bg='#add8e6').grid(row=2, column=0)
butf5 = Button(root, text="5", padx=30,pady=15, command=lambda: ip_num(5),bg='#add8e6').grid(row=2, column=1)
butf6 = Button(root, text="6", padx=30,pady=15, command=lambda: ip_num(6),bg='#add8e6').grid(row=2, column=2)
butf7 = Button(root, text="7", padx=30,pady=15, command=lambda: ip_num(7),bg='#add8e6').grid(row=3, column=0)
butf8 = Button(root, text="8", padx=30,pady=15, command=lambda: ip_num(8),bg='#add8e6').grid(row=3, column=1)
butf9 = Button(root, text="9", padx=30,pady=15, command=lambda: ip_num(9),bg='#add8e6').grid(row=3, column=2)
butf0 = Button(root, text="0", padx=30,pady=15, command=lambda: ip_num(0),bg='#add8e6').grid(row=4, column=0)
clrbut = Button(root, text="C", padx=30,pady=15, command=lambda: ip_num('red'),bg='#ff9a9a').grid(row=1, column=3)
addbut = Button(root, text="+", padx=30,pady=42, command=add_func,bg='#ffffa1').grid(row=2, column=3,rowspan=2)
divbut = Button(root, text="/", padx=30,pady=15, command=div_func,bg='#ffffa1').grid(row=4, column=1)
mulbut = Button(root, text="x", padx=30,pady=15, command=mult_func,bg='#ffffa1').grid(row=4, column=2)
butsub = Button(root, text="-", padx=31, pady=15, command=sub_func,bg='#ffffa1').grid(row=4, column=3)
buteql= Button(root, text='=', padx=142, pady=15,command=lambda: equal(ip_op),bg='#9affcc').grid(row=5, column=0, columnspan=4)
bg='#fed8b1'
#declaring buttons


root.mainloop()