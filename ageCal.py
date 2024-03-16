from tkinter import *
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.geometry("500x300")


def age():
	if my_entry.get():
		current_year = datetime.now().year
		your_age = current_year - int(my_entry.get())
		if your_age < 0 :
			messagebox.showerror("Error", "You entered the wrong date of birth.")
		else:
			messagebox.showinfo("Your Age", f"Your Age Is: {your_age}")

	else:
		messagebox.showerror("Error", "You forgot to enter your age!")

my_label = Label(root, text="Enter Year Born", font=("Helvetica", 24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="Calculate Age!", font=("Helvetica", 18), command=age)
my_button.pack(pady=20)



root.mainloop()