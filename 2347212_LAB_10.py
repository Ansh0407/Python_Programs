import tkinter as tk
from tkinter import ttk
import re

app = tk.Tk()
app.geometry("600x600")
app.title("University Management System")
app.configure(bg="lightblue")

unique_names = set()
unique_ids = set()

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_phone(phone):
    pattern = r'^\d{10}$'
    return re.match(pattern, phone)

def validate_name(name):
    pattern = r'^[a-zA-Z\s]+$'
    return re.match(pattern, name)

def validate_form():
    university_name = domain_entry.get()
    student_name = student_name_entry.get()
    gender = gender_var.get()
    department = department_var.get()
    student_id = student_id_entry.get()
    address = Address_checkbox_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    dob = dob_spinbox.get()
    
    if not validate_name(student_name):
        print("Error: Invalid Name")
        return

    if student_name in unique_names:
        print("Error: Student name already exists.")
        return

    if not validate_email(email):
        print("Error: Invalid Email ID")
        return

    if not validate_phone(phone):
        print("Error: Invalid Phone Number")
        return

    if student_id in unique_ids:
        print("Error: Student ID already exists.")
        return
    
    unique_names.add(student_name)
    unique_ids.add(student_id)
    
    print("University Name:", university_name)
    print("Student Name:", student_name)
    print("Gender:", gender)
    print("Department:", department)
    print("Student ID:", student_id)
    print("Address:", address)
    print("Email:", email)
    print("Phone:", phone)
    print("Year/DoB:", dob)
 
    domain_entry.delete(0, "end")
    student_name_entry.delete(0, "end")
    email_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    gender_var.set("")
    department_var.set("")
    student_id_entry.delete(0, "end")
    Address_checkbox_entry.delete(0, "end")
    dob_spinbox.delete(0, "end")
    
domain_label = tk.Label(app, text="University Name:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")
student_name_label = tk.Label(app, text="Student Name:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")
email_label = tk.Label(app, text="Email ID:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")
phone_label = tk.Label(app, text="Phone Number:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")
gender_label = tk.Label(app, text="Gender:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")
department_label = tk.Label(app, text="Department:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")
student_id_label = tk.Label(app, text="Student ID:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")
Address_checkbox_label = tk.Label(app, text="Address:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")
dob_label = tk.Label(app, text="Year/DoB:", font=("ariel", 12, 'bold'), bd=3, fg='white', bg="dark blue")

domain_entry = tk.Entry(app)
student_name_entry = tk.Entry(app)
email_entry = tk.Entry(app)
phone_entry = tk.Entry(app)
dob_spinbox = tk.Spinbox(app, from_=1900, to=2023, width=5)  # Adjust the range as needed

gender_var = tk.StringVar()
male_radio = tk.Radiobutton(app, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(app, text="Female", variable=gender_var, value="Female")

department_var = tk.StringVar()
department_choices = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Physics", "Mathematics"]
department_dropdown = ttk.Combobox(app, textvariable=department_var, values=department_choices)

student_id_entry = tk.Entry(app)
Address_checkbox_entry = tk.Entry(app)

submit_button = tk.Button(app, text="Submit", command=validate_form)

domain_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
domain_entry.grid(row=0, column=1, padx=10, pady=5)
student_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
student_name_entry.grid(row=1, column=1, padx=10, pady=5)
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry.grid(row=2, column=1, padx=10, pady=5)
phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
phone_entry.grid(row=3, column=1, padx=10, pady=5)
gender_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
male_radio.grid(row=4, column=1, padx=10, pady=5)
female_radio.grid(row=4, column=2, padx=10, pady=5)
department_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
department_dropdown.grid(row=5, column=1, padx=10, pady=5)
student_id_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
student_id_entry.grid(row=6, column=1, padx=10, pady=5)
Address_checkbox_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
Address_checkbox_entry.grid(row=7, column=1, padx=10, pady=5)
dob_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
dob_spinbox.grid(row=8, column=1, padx=10, pady=5)
submit_button.grid(row=9, column=0, columnspan=2, pady=10)

app.mainloop()
