from tkinter import *
# Create the main window
root = Tk()
root.title("email validation")
root.geometry("400x400")
# Disable window resizing
root.resizable(0, 0)
# Set background color to black
root.config(bg="black")

def check():
    # Import the regular expression module
    import re
    email_id = email_entry.get().lower()
    if(email_id ==""):
        validate_label.config(text="Please enter your email.", fg="yellow")

    elif re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email_id): # Check if email matches Gmail format
        validate_label.config(text=f"{email_id} is valid.", fg="green")

    else:
        validate_label.config(text=f"{email_id} is invalid.", fg="red")

# Create and place the title label
title = Label(root, text="Email Validation", font="Arial 20 bold", bg="black", fg="white")
title.place(x=90, y=50)

# Create and place the email entry field
email_entry = Entry(root)
email_entry.place(x=100, y=140, width=200)

# Create and place the check button
check_button = Button(root, text="Check",width=10, fg="white", bg="blue", cursor="hand2", command=check)
check_button.place(x=160, y=200)

#Create and place the validation message label
validate_label = Label(root, text=f"", font="Arial 10 bold",bg="black")
validate_label.place(x=110, y=270)

root.mainloop()