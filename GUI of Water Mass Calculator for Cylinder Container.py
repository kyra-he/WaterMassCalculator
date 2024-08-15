from tkinter import *
from Formula import formula
import tkinter as tk

#Set the initial values
n = 0
maximum_load = 360
total_mass = 0
radius = 0
height = 0
max_vol = 0.0
water_mass = 0.0

def main():
    title_text.set("<< Water Mass Calculator for Cylinder Container >>\nWelcome to the menu!")
    menu_list.delete(0, END)
    menu_options = [
        "A: Input Radius and Height",
        "B: Calculate the Volume and Mass",
        "C: Display Result",
        "D: Compare the result to maximum load",
        "E: Total Result",
    ]
    for text in menu_options:
        menu_list.insert(END, text)

def handle_menu_selection(event):
    selected_index = menu_list.curselection()[0]
    menu_options[selected_index][1]()

def input_data():
    global radius, height
    try:
        radius = float(radius_entry.get()) #Prompt the user to input data
        height = float(height_entry.get())
    except ValueError:
        result_text.set("Please enter valid numeric values for radius and height.")
        return
    if 0.2 <= radius <= 0.4 and 0.5 <= height <= 0.7:
        result_text.set("Entered values are valid. Please enter B for further calculation.")
    else:
        result_text.set("Invalid value of sizes. Please enter A to enter inputs again.")
        radius_entry.delete(0, END)
        height_entry.delete(0, END)

def calculate():
    global radius, height, max_vol, water_mass
    try:
        radius = float(radius_entry.get())
        height = float(height_entry.get())
    except ValueError:
        result_text.set("Please enter valid numeric values for radius and height.")
        return
    f = formula(radius, height)
    water_mass = f.mass_of_water()
    if total_mass + water_mass <= 360:
        max_vol = f.maximum_volume()
        result_text.set(f"Calculation completed.\nMaximum volume: {max_vol:.2f} m^3\nWater mass: {water_mass:.2f} kg")
    else:
        result_text.set("The current water mass has exceeded the maximum load.\nPlease enter E to check total result.")

def display():
    global n, total_mass
    if max_vol and water_mass:
        n += 1
        total_mass += water_mass
        total_text.set(f"Total water mass: {total_mass:.2f} kg\nCylinder containers needed: {n}")
    else:
        result_text.set("Please calculate the result first.")

def compare():
    if total_mass<= maximum_load: #Ensure current total mass doesn't exceed the maximum load
        result_text.set("The current water mass hasn't exceeded the maximum load yet."
                        "\nPlease enter A to continue adding new cylinder container.")
    else:
        result_text.set("The current water mass has exceeded the maximum load."
                        "\nPlease enter E to check the total result.")

def total():
    total_text.set(f"==================================================\n"
                   f"The total water mass that the truck will contain is {total_mass:,.2f} kg.\n"
                   f"It will take {n} cylinder containers to transfer this amount of water.\n"
                   f"==================================================")

def exit_program():#Function which allows user to exit the program
    quit()

def open_file(lstNE):
    file_path = "Sizes_of_Cylinder_Containers.txt"
    content = show_file(file_path, lstNE)
    return content

def show_file(file_path, lstNE):
    with open(file_path, 'r') as infile:
        content = infile.readlines()
    for line in content:
        modified_line = add_space_to_data(line)
        lstNE.insert(END, modified_line.strip())
    modified_lines = [add_space_to_data(line) for line in content]
    return modified_lines

#Seperate the data with a blank space
def add_space_to_data(line):
    data_list = line.split()
    modified_line = " ".join(data_list[i] + " " for i in range(len(data_list)))
    return modified_line.strip()

def handle_letter_entry():
    letter = letter_entry.get().upper()

    if letter == 'A':
        input_data()
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", result_text.get())
    elif letter == 'B':
        calculate()
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", result_text.get())
    elif letter == 'C':
        display()
        total_text_box.delete("1.0", "end")
        total_text_box.insert("end", total_text.get())
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", result_text.get())
    elif letter == 'D':
        compare()
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", result_text.get())
    elif letter == 'E':
        total()
        total_text_box.delete("1.0", "end")
        total_text_box.insert("end", total_text.get())

    letter_entry.delete(0, 'end')

main_window = tk.Tk()
main_window.title("Water Mass Calculator for Cylinder Container")
main_window.geometry('900x500')
main_window.configure(pady=30)
main_window.configure(bg="lightblue")#Set the background color to lightblue

title_text = StringVar()
result_text = StringVar()
total_text = StringVar()

yscroll = Scrollbar(main_window, orient=VERTICAL)
yscroll.grid(row=1, column=1, rowspan=2, padx=(0, 100), pady=5, sticky=NS)
conOFlstNE = StringVar()
lstNE = Listbox(main_window, width=20, height=7, yscrollcommand=yscroll.set,bg="lightgrey")
lstNE.grid(row=1, column=0, rowspan=2, columnspan=1, padx=(50, 0), pady=5, sticky=E)
yscroll["command"] = lstNE.yview

open_file(lstNE)

instruction_label = Label(main_window, text="Radius(m)   Height(m)",bg="lightblue")
instruction_label.grid(row=0, column=0, columnspan=1)

welcome_label = Label(main_window, textvariable=title_text,bg="lightblue")
welcome_label.grid(row=0, column=3, columnspan=3)

menu_list = Listbox(main_window, height=6, width=40,bg="lightgrey")
menu_list.grid(row=1, column=3, columnspan=3, padx=10, pady=10)
menu_options = [
    ("Input Radius and Height", input_data),
    ("Calculate the Volume and Mass", calculate),
    ("Display Result", display),
    ("Compare the result to maximum load", compare),
    ("Total Result", total)
]
for text, _ in menu_options:
    menu_list.insert(END, text)
menu_list.bind("<ButtonRelease-1>", handle_menu_selection)

radius_label = Label(main_window, text='Enter the radius (m):',bg="lightblue")
radius_label.grid(row=0, column=7, sticky=W + E + N + S)

radius_entry = Entry(main_window, width=5)
radius_entry.grid(row=0, column=8)

height_label = Label(main_window, text='Enter the height (m):',bg="lightblue")
height_label.grid(row=1, column=7)

height_entry = Entry(main_window, width=5)
height_entry.grid(row=1, column=8)

result_text_box = tk.Text(main_window, height=10, width=50,bg="lightgrey")
result_text_box.grid(row=7, column=0, columnspan=4, padx=10, pady=10)#Set the layout

total_text_box = tk.Text(main_window, height=10, width=50,bg="lightgrey")
total_text_box.grid(row=7, column=5, columnspan=4, padx=10, pady=10)#Set the layout

result_text.set("This is the result text.")
total_text.set("This is the total text.")

result_text_box.insert(tk.END, result_text.get())
total_text_box.insert(tk.END, total_text.get())

exit_button = Button(main_window, text="Exit", command=exit_program)
exit_button.grid(row=9, column=0)

letter_label = Label(main_window, text='Enter a letter:',bg="lightblue")
letter_label.grid(row=5, column=3, sticky=W + E + N + S)

letter_entry = Entry(main_window, width=5)
letter_entry.grid(row=5, column=4,padx=30)

submit_and_calculate_button= Button(main_window, text="Submit", command=handle_letter_entry)
submit_and_calculate_button.grid(row=5, column=7)

calculate_button= Button(main_window, text="Calculate", command=handle_letter_entry)
calculate_button.grid(row=5, column=8)

main()

main_window.mainloop()
