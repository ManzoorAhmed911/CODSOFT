def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return  x * y

def division(x,y):
    if y ==0:
        print("denominator is Zero, Error")        
    return  x / y
def calculator():
    print("CALCULATOR")
    print("Operations That You can perform: ")
    print("1. Addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4.division")
    
    
    choices = int(input("Enter the Operation number you want to perform: "))
    if choices not in [1, 2, 3, 4]:
        print("Wrong input")
    number1 = float(input("Enter the first Number: "))
    number2 = float(input("Enter the second Number: "))
    
    if choices == 1:
        result = addition(number1,number2)
        operator ="+"
    elif choices == 2:
        result = subtraction(number1,number2)
        operator = "-"
    elif choices == 3:
        result = multiplication(number1,number2)
        operator="*"
    elif choices == 4:
        result = division(number1,number2)
        operator="/"
    print(f"{number1} {operator} {number2} = {result}")
    
    
calculator()         
    
    
    
    
    
    
    
    
    
    
    
    






















































# import tkinter as tk

# # def adding_integers():
# #     NumbersAndOperator = NumbersAndOperator.entry.get()
# #     if NumbersAndOperator:
# #         listbox.insert(tk.END, NumbersAndOperator)
# #         NumbersAndOperator.delete(0,tk.END)

# def button_click(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(0,current+str(number))

# def clear():
#     entry.delete(0,tk.END)
# def calculation():
#     current = entry.get()
#     if current:
#         result = eval(current)
#         entry.delete(0,tk.END)
#         entry.insert(0, str(result))
#     else:
#         print("Error")

# window = tk.Tk()
# window.title("CALCULATOR")

# entry = tk.Entry(window, width=20, font=('NewTimeRoman',22))
# entry.grid(row=0,column=0,columnspan=4)

# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+'
# ]



# row_val = 1
# col_val = 0
# for button_text in buttons:
#     tk.Button(window, text=button_text, padx=20, pady=20, font=('Arial', 20), command=lambda t=button_text: button_click(t) if t != '=' else calculation()).grid(row=row_val, column=col_val)
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# # Clear button
# tk.Button(window, text="Clear", padx=20, pady=20, font=('Arial', 20), command=clear).grid(row=5, column=0, columnspan=4)

# # Run the Tkinter main loop
# window.mainloop()



# text = clear ,

# text = button_text,





