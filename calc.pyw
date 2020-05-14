# importing tkinter
from tkinter import *
root = Tk()
root.title("Tkinter calculator")  # adding title

# getting input from user
num_input= Entry(root,width=45, borderwidth= 2)
num_input.grid(row =0 , column =0, columnspan=4,pady=10,ipady=8)
global input_operator
ip_op = '+'
global first_number
f_num=0


# displaying seleted numbers on the text box
def input_num(num):
    if num != 'clear_all':
        current = num_input.get()
        num_input.delete(0, END)
        num_input.insert(0, str(current)+str(num))
        # fnum = num_input.insert(0, str(current)+str(num))
        return
    else:
        num_input.delete(0, END)
        return


# defining function to perform basic mathematical operations
def add_function():
    global first_number
    first_num = num_input.get()
    first_number = first_num
    num_input.delete(0,END)
    global input_operator
    input_operator = '+'


def multiply_function():
    first_num = num_input.get()
    global first_number
    first_number = first_num
    num_input.delete(0,END)
    global input_operator
    input_operator = 'x'


def divide_function():
    first_num = num_input.get()
    global first_number
    first_number = first_num
    num_input.delete(0,END)
    global input_operator
    input_operator = '/'


def substract_function():
    first_num = num_input.get()
    global first_number
    first_number = first_num
    num_input.delete(0,END)
    global input_operator
    input_operator = '-'


# function for equal button
def equal(input_operator):
    if input_operator == '+':
        second_num = num_input.get()
        num_input.delete(0,END)
        num_input.insert(0, int(first_number)+int(second_num))
    if input_operator == 'x':
        second_num = num_input.get()
        num_input.delete(0,END)
        num_input.insert(0, int(first_number)*int(second_num))
    if input_operator == '/':
        second_num = num_input.get()
        num_input.delete(0,END)
        num_input.insert(0, int(first_number)/int(second_num))
    if input_operator == '-':    # if the
        second_num = num_input.get()
        num_input.delete(0,END)
        num_input.insert(0, int(first_number)-int(second_num))


# declaring buttons for numbers
button_1 = Button(root, text="1", padx=30, pady=15, command=lambda: input_num(1), bg='#add8e6').grid(row=1, column=0) # 1
button_2 = Button(root, text="2", padx=30, pady=15, command=lambda: input_num(2), bg='#add8e6').grid(row=1, column=1) # 2
button_3 = Button(root, text="3", padx=30, pady=15, command=lambda: input_num(3), bg='#add8e6').grid(row=1, column=2) # 3
button_4 = Button(root, text="4", padx=30, pady=15, command=lambda: input_num(4), bg='#add8e6').grid(row=2, column=0) # 4
button_5 = Button(root, text="5", padx=30, pady=15, command=lambda: input_num(5), bg='#add8e6').grid(row=2, column=1) # 5
button_6 = Button(root, text="6", padx=30, pady=15, command=lambda: input_num(6), bg='#add8e6').grid(row=2, column=2) # 6
button_7 = Button(root, text="7", padx=30, pady=15, command=lambda: input_num(7), bg='#add8e6').grid(row=3, column=0) # 7
button_8 = Button(root, text="8", padx=30, pady=15, command=lambda: input_num(8), bg='#add8e6').grid(row=3, column=1) # 8
button_9 = Button(root, text="9", padx=30, pady=15, command=lambda: input_num(9), bg='#add8e6').grid(row=3, column=2) # 9
button_0 = Button(root, text="0", padx=30, pady=15, command=lambda: input_num(0), bg='#add8e6').grid(row=4, column=0) # 0

# declaring buttons for operators
add_button = Button(root, text="+", padx=30,pady=42, command=add_function,bg='#ffffa1')
add_button.grid(row=2, column=3,rowspan=2)
divide_button = Button(root, text="/", padx=30,pady=15, command=divide_function,bg='#ffffa1')
divide_button.grid(row=4, column=1)
multiply_button = Button(root, text="x", padx=30,pady=15, command=multiply_function,bg='#ffffa1')
multiply_button.grid(row=4, column=2)
substract_button = Button(root, text="-", padx=31, pady=15, command=substract_function,bg='#ffffa1')
substract_button.grid(row=4, column=3)

# declaring equal button and clear all button
clear_button = Button(root, text="C", padx=30,pady=15, command=lambda: input_num('clear_all'),bg='#ff9a9a')
clear_button.grid(row=1, column=3)
equal_button= Button(root, text='=', padx=142, pady=15,command=lambda: equal(input_operator),bg='#9affcc')
equal_button.grid(row=5, column=0, columnspan=4)

root.mainloop()
