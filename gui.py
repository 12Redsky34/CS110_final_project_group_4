# GUI for final group project
import tkinter as tk
from tkinter import messagebox

# Main Window
window = tk.Tk()
window.title("Final Group Project (WIP)")
#window.geometry("700x700") # ("width x height")

# Blank spaces for formatting
tk.Label(window, text="").grid(row=7, column=0) # Between name and address
tk.Label(window, text="").grid(row=13, column=0) # Between address and contact
tk.Label(window, text="").grid(row=18, column=0) # Between contact and info


# Heading/Title widget
header = tk.Label(window, text="Resume Reformatting", font=("Arial", 25)).grid(row=0, column=0, columnspan=3)


# Name header
tk.Label(window, text="Enter your name (leave blank if irrelevant)").grid(row=1, column=1)
# Entry widgets, Name category
tk.Label(window, text="Title:").grid(row=2, column=0)
tk.Label(window, text="First Name:").grid(row=3, column=0)
tk.Label(window, text="Middle Name:").grid(row=4, column=0)
tk.Label(window, text="Last Name:").grid(row=5, column=0)
tk.Label(window, text="Suffix:").grid(row=6, column=0)

title = tk.Entry(window).grid(row=2, column=1)
first = tk.Entry(window).grid(row=3, column=1)
middle = tk.Entry(window).grid(row=4, column=1)
last = tk.Entry(window).grid(row=5, column=1)
suffix = tk.Entry(window).grid(row=6, column=1)


# Address header
tk.Label(window, text="Enter your address details (leave blank if irrelevant)").grid(row=8, column=1)
# Entry widgets, Address category
tk.Label(window, text="Street:").grid(row=9, column=0)
tk.Label(window, text="City:").grid(row=10, column=0)
tk.Label(window, text="State:").grid(row=11, column=0)
tk.Label(window, text="Zip Code:").grid(row=12, column=0)

street = tk.Entry(window).grid(row=9, column=1)
city = tk.Entry(window).grid(row=10, column=1)
state = tk.Entry(window).grid(row=11, column=1)
zip_code = tk.Entry(window).grid(row=12, column=1)


# Contact header
tk.Label(window, text="Enter your contact details (leave blank if irrelevant)").grid(row=14, column=1)
# Entry widgets, Contact category
tk.Label(window, text="Primary Number:").grid(row=15, column=0)
tk.Label(window, text="Secondary Number:").grid(row=16, column=0)
tk.Label(window, text="Email:").grid(row=17, column=0)

primary = tk.Entry(window).grid(row=15, column=1)
secondary = tk.Entry(window).grid(row=16, column=1)
email = tk.Entry(window).grid(row=17, column=1)


# Experience, Education, Skills header
tk.Label(window, text="Experience, Education, and Skills (leave blank if irrelevant)").grid(row=19, column=1)
# Entry widgets, Additional info category
tk.Label(window, text="Enter your relevant experience:").grid(row=20, column=0)
tk.Label(window, text="Enter your relevant education:").grid(row=21, column=0)
tk.Label(window, text="Enter your relevant skills:").grid(row=22, column=0)

experience = tk.Text(window, height=3, width=15).grid(row=20, column=1)
education = tk.Text(window, height=3, width=15).grid(row=21, column=1)
skills = tk.Text(window, height=3, width=15).grid(row=22, column=1)


# Set up preview command (alert box version)
def preview_box():
    messagebox.showinfo("Preview", "This will contain a preview of the output.")

# Preview/Submit button
tk.Button(window, text="Preview", width=10, command=preview_box).grid(row=23, column=3)
tk.Button(window, text="Submit", width=10).grid(row=24, column=3)


# Establish event loop
window.mainloop()
