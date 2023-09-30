import tkinter as tk


# Function to add task to the list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)  # Clear the entry field after adding a task


#Function to remove task form the list
def remove_task():
    selected_task= listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)


#Function to mark task as complete

def complete_task():
    selected_task= listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task = listbox.get(task_index)
        completed_task = f"✓ {task}"
        listbox.delete(task_index)
        # listbox2.insert(tk.END, task)
        listbox2.insert(tk.END, completed_task)
        

#creating a main window
root = tk.Tk()
root.title("To-Do List")

#Width of input task bar
entry = tk.Entry(root, width=50)
entry.pack()

#creting button for addig task
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

#forming to a box containing all task in a list
listbox = tk.Listbox(root, width=50)
listbox.pack()

#creting button for removing task
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

complete_button = tk.Button(root, text="Completed Tasks", command=complete_task)
complete_button.pack()

listbox2 = tk.Listbox(root, width=50)
listbox2.pack()

#Starting the GUI event loop
root.mainloop()




# import tkinter as tk

# def add_task():
#     task = entry.get()
#     if task:
#         listbox.insert(tk.END, task)
#         entry.delete(0, tk.END)  # Clear the entry field after adding a task

# def remove_task():
#     selected_task_index = listbox.curselection()
#     if selected_task_index:
#         listbox.delete(selected_task_index)

# root = tk.Tk()
# root.title("To-Do List")

# entry = tk.Entry(root, width=50)
# entry.pack()

# add_button = tk.Button(root, text="Add Task", command=add_task)
# add_button.pack()

# listbox = tk.Listbox(root, width=50)
# listbox.pack()

# remove_button = tk.Button(root, text="Remove Task", command=remove_task)
# remove_button.pack()

# root.mainloop()



'''
This code is without GUI
'''

# tasks = []

# def add_task(task):
#     tasks.append(task)
#     print(f"Task {task} added.")
    
# def list_tasks():
#     if tasks:
#         print("To do list : ")
#         for i,task in enumerate(tasks, start=1):
#             print(f"{i}. {task}")
#     else:
#         print("No tasks are set")
        
# def complete_taks(task_number):
#     if 1<= task_number <= len(tasks):
#         completed_task = tasks.pop(task_number -1)
#         print(f"{task_number}. {completed_task} completed and removed from To-do List  ")
#     else:
#         print("invalid Task number, please re-check!")
           
    
# while True:
#     print("options\n")
#     print("1. Add a task.")
#     print("2. List all Tasks")
#     print("3. Marks task as Complete.")
#     print("4. Quit")
    
#     choice = int(input("Enter Your Choice number : "))
#     if choice==1:
#         task = input("Enter The Task: ")
#         add_task(task)
#     elif choice == 2:
#         list.tasks()
#     elif choice == 3:
#         task_number = int(input("Enter the task number that you completed"))
#         complete_task(task_number)
#     elif choice==4:
#         break;
#     else:
#         print("Wrong Input!!")
    
    
'''
Working with GUI
'''




















