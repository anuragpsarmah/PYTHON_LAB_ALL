import tkinter as tk
from tkinter import ttk
import re

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    dob = dob_spinbox.get()
    tracker = tracker_var.get()
    bmi = bmi_entry.get()

    name_pattern = r"^[A-Za-z\s]+$"
    email_pattern = r"^\w+@\w+\.\w+$"
    phone_pattern = r"^\d{10}$"
    dob_pattern = r"^\d{4}$"

    if not re.match(name_pattern, name):
        error_label.config(text="Invalid name. Please use only letters and spaces.")
        return
    if not re.match(email_pattern, email):
        error_label.config(text="Invalid email format. Please use name@example.com.")
        return
    if not re.match(phone_pattern, phone):
        error_label.config(text="Invalid phone number. Please use 10 digits.")
        return
    if gender not in ["Male", "Female", "Other"]:
        error_label.config(text="Invalid gender selection.")
        return
    if not re.match(dob_pattern, dob):
        error_label.config(text="Invalid year of birth. Please use a 4-digit year.")
        return

    error_label.config(text="")

    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Gender: {gender}")
    print(f"Year of Birth: {dob}")
    print(f"Fitness Tracker: {tracker}")
    print(f"BMI: {bmi}")

root = tk.Tk()
root.geometry("400x400")
root.title("Fitness Tracking System")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

email_label = tk.Label(root, text="Email ID:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

phone_label = tk.Label(root, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

gender_label = tk.Label(root, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_dropdown.pack()

dob_label = tk.Label(root, text="Year of Birth:")
dob_label.pack()
dob_spinbox = ttk.Spinbox(root, from_=1900, to=2023)
dob_spinbox.pack()

tracker_label = tk.Label(root, text="Fitness Tracker:")
tracker_label.pack()
tracker_var = tk.StringVar()
tracker_dropdown = ttk.Combobox(root, textvariable=tracker_var, values=["Fitbit", "Apple Watch", "Garmin", "Other"])
tracker_dropdown.pack()

bmi_label = tk.Label(root, text="BMI:")
bmi_label.pack()
bmi_entry = tk.Entry(root)
bmi_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

error_label = tk.Label(root, text="", foreground="red")
error_label.pack()

root.mainloop()
