# GUI for final group project
import tkinter as tk

# Main Window
window = tk.Tk()
window.title("Final Group Project (WIP)")

# Heading/Title widget
tk.Label(window, text="Resume Reformatting", font=("Arial", 25)).grid(row=0, column=0)

form_pane = tk.Frame(window)
form_pane.grid(row=1, column=0)

# Blank spaces for formatting
tk.Label(form_pane, text="").grid(row=7, column=0) # Between name and address
tk.Label(form_pane, text="").grid(row=13, column=0) # Between address and contact
tk.Label(form_pane, text="").grid(row=18, column=0) # Between contact and info


# Name header
tk.Label(form_pane, text="Enter your name (leave blank if irrelevant)").grid(row=1, column=1)
# Entry widgets, Name category
tk.Label(form_pane, text="Title:").grid(row=2, column=0)
tk.Label(form_pane, text="First Name:").grid(row=3, column=0)
tk.Label(form_pane, text="Middle Name:").grid(row=4, column=0)
tk.Label(form_pane, text="Last Name:").grid(row=5, column=0)
tk.Label(form_pane, text="Suffix:").grid(row=6, column=0)

title = tk.Entry(form_pane)
title.grid(row=2, column=1)

first = tk.Entry(form_pane)
first.grid(row=3, column=1)

middle = tk.Entry(form_pane)
middle.grid(row=4, column=1)

last = tk.Entry(form_pane)
last.grid(row=5, column=1)

suffix = tk.Entry(form_pane)
suffix.grid(row=6, column=1)


# Address header
tk.Label(form_pane, text="Enter your address details (leave blank if irrelevant)").grid(row=8, column=1)
# Entry widgets, Address category
tk.Label(form_pane, text="Street:").grid(row=9, column=0)
tk.Label(form_pane, text="City:").grid(row=10, column=0)
tk.Label(form_pane, text="State:").grid(row=11, column=0)
tk.Label(form_pane, text="Zip Code:").grid(row=12, column=0)

street = tk.Entry(form_pane)
street.grid(row=9, column=1)

city = tk.Entry(form_pane)
city.grid(row=10, column=1)

state = tk.Entry(form_pane)
state.grid(row=11, column=1)

zip_code = tk.Entry(form_pane)
zip_code.grid(row=12, column=1)


# Contact header
tk.Label(form_pane, text="Enter your contact details (leave blank if irrelevant)").grid(row=14, column=1)
# Entry widgets, Contact category
tk.Label(form_pane, text="Primary Number:").grid(row=15, column=0)
tk.Label(form_pane, text="Secondary Number:").grid(row=16, column=0)
tk.Label(form_pane, text="Email:").grid(row=17, column=0)

primary = tk.Entry(form_pane)
primary.grid(row=15, column=1)

secondary = tk.Entry(form_pane)
secondary.grid(row=16, column=1)

email = tk.Entry(form_pane)
email.grid(row=17, column=1)


# Experience, Education, Skills header
tk.Label(form_pane, text="Experience, Education, and Skills (leave blank if irrelevant)").grid(row=19, column=1)
# Entry widgets, Additional info category
tk.Label(form_pane, text="Enter your relevant experience:").grid(row=20, column=0)
tk.Label(form_pane, text="Enter your relevant education:").grid(row=21, column=0)
tk.Label(form_pane, text="Enter your relevant skills:").grid(row=22, column=0)

experience = tk.Text(form_pane, height=3, width=15)
experience.grid(row=20, column=1)

education = tk.Text(form_pane, height=3, width=15)
education.grid(row=21, column=1)

skills = tk.Text(form_pane, height=3, width=15)
skills.grid(row=22, column=1)


from tkinter import messagebox
from classes import Applicant

# The core object storing all the information from the input fields
applicant = Applicant()

# Populates the applicant object properties from the input fields
def update_applicant():
    applicant.clear()

    title_text = title.get()
    if title_text != "":
        applicant.set_name_title(title_text)
    
    first_text = first.get()
    if first_text != "":
        applicant.set_name_first(first_text)
    
    middle_text = middle.get()
    if middle_text != "":
        applicant.set_name_middle(middle_text)
    
    last_text = last.get()
    if last_text != "":
        applicant.set_name_last(last_text)
    
    suffix_text = suffix.get()
    if suffix_text != "":
        applicant.set_name_suffix(suffix_text)
    

    street_text = street.get()
    if street_text != "":
        applicant.set_addr_street(street_text)

    city_text = city.get()
    if city_text != "":
        applicant.set_addr_city(city_text)
    
    state_text = state.get()
    if state_text != "":
        applicant.set_addr_state(state_text)
    
    zip_text = zip_code.get()
    if zip_text != "":
        applicant.set_addr_zip(zip_text)

    
    primary_text = primary.get()
    if primary_text != "":
        applicant.set_contact_phone(primary_text)
    
    secondary_text = secondary.get()
    if secondary_text != "":
        applicant.set_contact_phone_alt(secondary_text)
    
    email_text = email.get()
    if email_text != "":
        applicant.set_contact_email(email_text)
    
    exp_text = experience.get('1.0', 'end').splitlines()
    for text in exp_text:
        applicant.add_experience(text)
    
    edu_text = education.get('1.0', 'end').splitlines()
    for text in edu_text:
        applicant.add_education(text)
    
    skills_text = skills.get('1.0', 'end').splitlines()
    for text in skills_text:
        applicant.add_skill(text)


# Generates the preview of the applicant's information
def preview():
    update_applicant()
    preview_text.configure(text=applicant.to_string())

import os

# Saves the applicant's information to a text file
def save_applicant(data):
    target_dir = 'submissions'

    # Make the target directory if it does not exist
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    
    applicant_number = len(os.listdir(target_dir)) + 1
    file_name = f"{target_dir}/applicant-{applicant_number}.txt"

    new_file = open(file_name, "w")
    new_file.write(data)
    new_file.close()

# Submits the applicant's information
def submit():
    update_applicant()
    save_applicant(applicant.to_string())
    messagebox.showinfo("Submission received", "Submitted")

# Preview/Submit button
tk.Button(form_pane, text="Preview", width=10, command=preview).grid(row=23, column=3)
tk.Button(form_pane, text="Submit", width=10, command=submit).grid(row=24, column=3)


preview_pane = tk.Frame(window)
preview_pane.grid(row=1, column=2)

tk.Label(preview_pane, text="Preview").grid(row=0, column=0)
preview_text = tk.Label(preview_pane, text="")
preview_text.grid(row=1, column=0)


# Establish event loop
window.mainloop()
