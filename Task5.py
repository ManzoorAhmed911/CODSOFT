import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}


# Adding contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact_list.insert(tk.END, f"{name} - {phone}")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        clear_fields()
        messagebox.showinfo("Contact Saved Successfully")
    else:
        messagebox.showerror("Error", "Name and phone information are required")


# View all contacts
def view_contact():
    view_list.delete(0, tk.END)
    for name, info in contacts.items():
        view_list.insert(tk.END, f"{name} - {info['Phone']}")


# Search for a contact
def search_contact():
    search_term = search_entry.get().lower()
    search_list.delete(0, tk.END)
    for name, info in contacts.items():
        if search_term in name.lower() or search_term in info['Phone'].lower():  # Corrected 'Phone' key
            search_list.insert(tk.END, f"{name} - {info['Phone']}")



# Clear all input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)


# Update contact information
def update_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact:
        selected_name = selected_contact.split('-')[0].strip()
        if selected_name in contacts:
            name_entry.delete(0, tk.END)
            name_entry.insert(tk.END, selected_name)
            phone_entry.delete(0, tk.END)
            phone_entry.insert(tk.END, contacts[selected_name]['Phone'])
            email_entry.delete(0, tk.END)
            email_entry.insert(tk.END, contacts[selected_name]['Email'])
            address_entry.delete(0, tk.END)
            address_entry.insert(tk.END, contacts[selected_name]["Address"])
        else:
            messagebox.showerror("Error", "Contact not found")
    else:
        messagebox.showerror("Error", "Select a contact to update")


# Delete a contact
def delete_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact:
        selected_name = selected_contact.split("-")[0].strip()
        if selected_name in contacts:
            del contacts[selected_name]
            contact_list.delete(contact_list.curselection())
            clear_fields()
            messagebox.showinfo("Contact Deleted Successfully")
        else:
            messagebox.showerror("Error", "Contact not found")
    else:
        messagebox.showerror("Error", "Select a contact to delete")


# Create GUI window
contact = tk.Tk()
contact.title("CONTACT BOOK")
# Set the initial width to 800 pixels and height to 600 pixels
contact.geometry("1100x1100")

# Create input fields and labels
name_label = tk.Label(contact, text="Name:")
name_label.pack()
name_entry = tk.Entry(contact, width=50)
name_entry.pack(pady=5)

phone_label = tk.Label(contact, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(contact, width=50)
phone_entry.pack(pady=5)

email_label = tk.Label(contact, text="Email:")
email_label.pack()
email_entry = tk.Entry(contact, width=50)
email_entry.pack(pady=5)

address_label = tk.Label(contact, text="Address:")
address_label.pack()
address_entry = tk.Entry(contact, width=50)
address_entry.pack(pady=5)

# Create Buttons
add_button = tk.Button(contact, text="Add Contact", command=add_contact)
add_button.pack(pady=8)
# Label for the list of contacts
contacts_label = tk.Label(contact, text="Contacts can be deleted, updated from this section")
contacts_label.pack()
# List where all contacts are displayed
contact_list = tk.Listbox(contact, width=45)
contact_list.pack()


view_button = tk.Button(contact, text="View Contacts", command=view_contact)
view_button.pack(pady=8)
#lableing view section
contacts_label = tk.Label(contact, text="to View all contacts click view button")
contacts_label.pack()
view_list = tk.Listbox(contact, width=45)
view_list.pack()

delete_button = tk.Button(contact, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=8)

update_button = tk.Button(contact, text="Update Contact", command=update_contact)
update_button.pack(pady=8)

# Input field and label for search
search_label = tk.Label(contact, text="Search")
search_label.pack()
search_entry = tk.Entry(contact, width=40)
search_entry.pack(pady=8)

# Search Button
search_button = tk.Button(contact, text="Search Contact", command=search_contact)
search_button.pack(pady=8)
#lableing view section
contacts_label = tk.Label(contact, text="contact that has been searched for")
contacts_label.pack()
search_list = tk.Listbox(contact, width=45)
search_list.pack()


contact.mainloop()
