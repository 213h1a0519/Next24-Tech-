import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    
    # Validate the input fields
    if not (name and email and age):
        messagebox.showwarning("Incomplete Form", "Please fill in all fields")
    else:
        messagebox.showinfo("Registration Successful", f"Name: {name}\nEmail: {email}\nAge: {age}")
        # Here you can add code to save the data to a file or database
        
        # Clear the entry fields after submission
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_age.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entry boxes for the form
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_name = tk.Entry(root, width=50)
entry_name.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_email = tk.Entry(root, width=50)
entry_email.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_age = tk.Entry(root, width=50)
entry_age.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=1, pady=15)

# Run the main event loop
root.mainloop()
