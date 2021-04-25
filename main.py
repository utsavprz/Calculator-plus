#Building a simple calculator (Utsav Prajapati - 200261(29A))

# from tkinter module, imports *(everything)
from tkinter import *

#back-end of calculator
# global declaration the entered_num variable 
entered_num = ""

# function to update the expression in the entry field (number_entry)
def button_click(number):
    global entered_num
    # string concatination
    entered_num = entered_num + str(number)
    number_entry.set(entered_num) # 'set' updates the 'expression(numbers)' in the entry field (number_entry)

# function to clear the entry field (number_entry)
def button_clear():
    global entered_num
    entered_num = ""
    number_entry.set(entered_num)

# function to calculate the expression and display in the entry field (number_entry)
def equal_button():
  # 'try' and 'except' used here to avoid zero division error, and other error
  try: 
      global entered_num

      # example for eval function
      # eval("2 ** 8")
      # 256 gets displayed (though the numbers are as string, 'eval'evaluates the string expression and does the calculation') 

      result = str(eval(entered_num))  # 'eval' is used to evaluate the string expression and do the calculation and 'str converts the result into string'
      number_entry.set(result)

      # initialzes the expression variable by empty string afte the result is displayed on the entry field (number_entry)
      entered_num = ""

  # if zero division is done, 'except' updates the entry box to show "ERROR"
  except:
    number_entry.set("ERROR")
    entered_num = ""


# front-end of calculator
# creates the tkinter GUI window
root = Tk()

# sets the tile for GUI window 
root.title(' Calc +')

# sets the dimension of GUI window 
root.geometry("300x450")

# setting the bitmap icon for the GUI window
root.iconbitmap('D:\\calculator python\\icons\\Wineass-Ios7-Redesign-Calculator.ico')

# back-end of calculator
# function of frame for default mode
def default_mode_frame():
    default_frame = Frame(root, bg="#F4F7F8")
    default_frame.place(x=0, y=0, width=300, height=450)

    # global declaration of number_entry
    global number_entry

    # StringVar() is a variable class
    number_entry = StringVar()

    # entry box where the numbers are displayed
    eq_entry = Entry(root, fg="#BBBABA", textvariable=number_entry, font=("Calibre", 35, "bold"), justify=RIGHT, bd=0,
                     state=DISABLED, disabledbackground='#F4F7F8')
    eq_entry.place(x=0, y=0, width=300, height=90, )

    # number buttons
    button_1 = Button(default_frame, text="1", padx=20, pady=15, fg="#202020", command=lambda: button_click(1), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_2 = Button(default_frame, text="2", padx=20, pady=15, fg="#202020", command=lambda: button_click(2), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_3 = Button(default_frame, text="3", padx=20, pady=15, fg="#202020", command=lambda: button_click(3), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_4 = Button(default_frame, text="4", padx=20, pady=15, fg="#202020", command=lambda: button_click(4), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_5 = Button(default_frame, text="5", padx=20, pady=15, fg="#202020", command=lambda: button_click(5), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_6 = Button(default_frame, text="6", padx=20, pady=15, fg="#202020", command=lambda: button_click(6), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_7 = Button(default_frame, text="7", padx=20, pady=15, fg="#202020", command=lambda: button_click(7), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_8 = Button(default_frame, text="8", padx=20, pady=15, fg="#202020", command=lambda: button_click(8), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_9 = Button(default_frame, text="9", padx=20, pady=15, fg="#202020", command=lambda: button_click(9), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_0 = Button(default_frame, text="0", padx=20, pady=15, fg="#202020", command=lambda: button_click(0), bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_point = Button(default_frame, text=".", padx=23, pady=15, fg="#202020", command=lambda: button_click("."),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    # operator buttons
    add_btn = Button(default_frame, text="+", padx=25, pady=15, fg="#FB6E12", command=lambda: button_click("+"), bd=0,
                     font=("Helvetica", 12, 'bold'), cursor="hand2")

    button_minus = Button(default_frame, text="−", padx=25, pady=15, fg="#FB6E12", command=lambda: button_click("-"),
                          bd=0,
                          font=("Helvetica", 12, 'bold'), cursor="hand2")

    button_multiply = Button(default_frame, text="x", padx=25, pady=15, fg="#FB6E12", command=lambda: button_click("*"),
                             bd=0,
                             font=("Helvetica", 12, 'bold'), cursor="hand2", )

    button_divide = Button(default_frame, text="/", padx=28, pady=15, fg="#FB6E12", command=lambda: button_click("/"),
                           bd=0,
                           font=("Helvetica", 12, 'bold'), cursor="hand2")

    button_to_clear = Button(default_frame, text="C", padx=19, pady=15, fg="#FB6E12", command=lambda: button_clear(),
                             bd=0,
                             font=("Helvetica", 12, 'bold'), cursor="hand2")

    equal_btn = Button(default_frame, text="=", padx=60, pady=15, fg="#FFFFFF", bg="#FB6E12",
                       command=lambda: equal_button(),
                       bd=0,
                       font=("Helvetica", 12, 'bold'), cursor="hand2")

    percent_btn = Button(default_frame, text="%", padx=17, pady=15, fg="#FB6E12", command=lambda: button_click("%"),
                         bd=0,
                         font=("Helvetica", 12, 'bold'), cursor="hand2")

    dark_mode_btn = Button(default_frame, text="M", padx=17, pady=15, fg="#FB6E12", bg='#202020', bd=0,
                           command=dark_mode_frame,
                           font=("Helvetica", 12, 'bold'), cursor="hand2")

    # Placement of Buttons on GUI

    # First row buttons
    button_to_clear.place(x=80, y=100)
    button_divide.place(x=220, y=100)
    percent_btn.place(x=150, y=100)
    dark_mode_btn.place(x=10, y=100)

    # Second row buttons
    button_7.place(x=10, y=170)
    button_8.place(x=80, y=170)
    button_9.place(x=150, y=170)
    button_multiply.place(x=220, y=170)

    # Third row buttons
    button_4.place(x=10, y=240)
    button_5.place(x=80, y=240)
    button_6.place(x=150, y=240)
    button_minus.place(x=220, y=240)

    # Forth row buttons
    button_1.place(x=10, y=310)
    button_2.place(x=80, y=310)
    button_3.place(x=150, y=310)
    add_btn.place(x=220, y=310)

    # Fifth row buttons
    button_0.place(x=10, y=380)
    equal_btn.place(x=150, y=380)
    button_point.place(x=80, y=380)

# function of frame for dark mode
def dark_mode_frame():
    dark_frame = Frame(root, bg="black")
    dark_frame.place(x=0, y=0, width=300, height=450)

    global number_entry
    number_entry = StringVar()

    eq_entry = Entry(root, fg="#BBBABA", textvariable=number_entry, font=("Calibre", 35, "bold"), justify=RIGHT, bd=0,
                     state=DISABLED, disabledbackground='#000000')
    eq_entry.place(x=0, y=0, width=300, height=90, )

    # number buttons
    button_1 = Button(dark_frame, text="1", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(1),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_2 = Button(dark_frame, text="2", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(2),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_3 = Button(dark_frame, text="3", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(3),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_4 = Button(dark_frame, text="4", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(4),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_5 = Button(dark_frame, text="5", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(5),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_6 = Button(dark_frame, text="6", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(6),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_7 = Button(dark_frame, text="7", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(7),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_8 = Button(dark_frame, text="8", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(8),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_9 = Button(dark_frame, text="9", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(9),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_0 = Button(dark_frame, text="0", bg="#111111", fg="#F4F7F8", padx=20, pady=15,
                      command=lambda: button_click(0),
                      bd=0,
                      font=("Helvetica", 12, 'bold'),
                      cursor="hand2")

    button_point = Button(dark_frame, text=".", bg="#111111", fg="#F4F7F8", padx=23, pady=15,
                          command=lambda: button_click("."), bd=0,
                          font=("Helvetica", 12, 'bold'),
                          cursor="hand2")

    # operator buttons
    add_btn = Button(dark_frame, text="+", bg="#202020", padx=25, pady=15, fg="#FB6E12",
                     command=lambda: button_click("+"),
                     bd=0,
                     font=("Helvetica", 12, 'bold'), cursor="hand2")

    button_minus = Button(dark_frame, text="−", bg="#202020", padx=25, pady=15, fg="#FB6E12",
                          command=lambda: button_click("-"), bd=0,
                          font=("Helvetica", 12, 'bold'), cursor="hand2")

    button_multiply = Button(dark_frame, text="x", bg="#202020", padx=25, pady=15, fg="#FB6E12",
                             command=lambda: button_click("*"), bd=0,
                             font=("Helvetica", 12, 'bold'), cursor="hand2", )

    button_divide = Button(dark_frame, text="/", bg="#202020", padx=28, pady=15, fg="#FB6E12",
                           command=lambda: button_click("/"), bd=0,
                           font=("Helvetica", 12, 'bold'), cursor="hand2")

    button_to_clear = Button(dark_frame, text="C", bg="#202020", padx=19, pady=15, fg="#FB6E12",
                             command=lambda: button_clear(), bd=0,
                             font=("Helvetica", 12, 'bold'), cursor="hand2")

    equal_btn = Button(dark_frame, text="=", padx=60, pady=15, fg="#FFFFFF", bg="#FB6E12",
                       command=lambda: equal_button(),
                       bd=0,
                       font=("Helvetica", 12, 'bold'), cursor="hand2")

    percent_btn = Button(dark_frame, text="%", bg="#202020", padx=17, pady=15, fg="#FB6E12",
                         command=lambda: button_click("%"), bd=0,
                         font=("Helvetica", 12, 'bold'), cursor="hand2")

    # Enables darkmode on button click
    dark_mode_btn = Button(dark_frame, text="M", padx=17, pady=15, fg="#FB6E12", bd=0, command=default_mode_frame,
                           font=("Helvetica", 12, 'bold'), cursor="hand2")

    # Placement of Buttons on GUI

    # First row buttons
    button_to_clear.place(x=80, y=100)
    button_divide.place(x=220, y=100)
    percent_btn.place(x=150, y=100)
    dark_mode_btn.place(x=10, y=100)

    # Second row buttons
    button_7.place(x=10, y=170)
    button_8.place(x=80, y=170)
    button_9.place(x=150, y=170)
    button_multiply.place(x=220, y=170)

    # Third row buttons
    button_4.place(x=10, y=240)
    button_5.place(x=80, y=240)
    button_6.place(x=150, y=240)
    button_minus.place(x=220, y=240)

    # Forth row buttons
    button_1.place(x=10, y=310)
    button_2.place(x=80, y=310)
    button_3.place(x=150, y=310)
    add_btn.place(x=220, y=310)

    # Fifth row buttons
    button_0.place(x=10, y=380)
    equal_btn.place(x=150, y=380)
    button_point.place(x=80, y=380)


# calls and opens the default_mode_frame
default_mode_frame()

# 'resizable' disable resizing of the tkinter window
root.resizable(False, False)

# start the root GUI 
root.mainloop()




