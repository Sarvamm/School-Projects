#make a basic tkinter gui with  some lables and buttons 
import tkinter as tk
#make a basic tkinter gui with  some lables and buttons 

    #creating the main window
window = tk.Tk()

#creating labels

label1 = tk.Label(window, text="Enter your name:")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Enter your age:")
label2.grid(row=1, column=0)

#creating entry boxes   

name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

age_entry = tk.Entry(window)
age_entry.grid(row=1, column=1)

#creating buttons

submit_button = tk.Button(window, text="Submit", command=lambda: submit_data())
submit_button.grid(row=2, column=0)

def submit_data():
    name = name_entry.get()
    age = age_entry.get()
    print(f"Name: {name}, Age: {age}")
    #clearing the entry boxes
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
def displayData():
    name = name_entry.get()
    age = age_entry.get()
    display_label = tk.Label(window, text=f"Name: {name}, Age: {age}")
    display_label.grid(row=3, column=0)

#creating buttons

display_button = tk.Button(window, text="Display Data", command=displayData)
display_button.grid(row=2, column=1)

#creating a quit button

quit_button = tk.Button(window, text="Quit", command=window.quit)
quit_button.grid(row=4, column=0)

#start the main loop

window.mainloop()
