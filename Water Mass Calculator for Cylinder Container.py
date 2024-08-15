from Formula import formula

#Set the initial values
n = 0
maximum_load = 360
total_mass = 0
radius = 0
height = 0

#function of menu
def main_menu():
    title()
    print("A: Input Radius and Height")#Show the function behind each letter
    print("B: Calculate the Volume and Mass")
    print("C: Display Result")
    print("D: Compare the result to maximum load")
    print("E: Total Result")
    print("F: Exit")

#Title and greeting
def title():
    print('''
         << Water Mass Calculator for Cylinder Container >>
                       Welcome to the menu!
        ''')

def input_data():
    global radius, height
    radius = float(input("Enter the radius:"))
    height = float(input("Enter the height:"))
    if 0.2 <= radius <= 0.4 and 0.5 <= height <= 0.7:
        print("\nEntered values are valid. Please enter B for further calculation.")
    else:
        print("\nInvalid value of sizes. Please enter A to enter inputs again.")
        radius, height = 0, 0

def calculate():
        global radius, height
        f=formula(radius, height)
        water_mass = f.mass_of_water()
        if total_mass+water_mass <= 360:#Ensure the calculation won't continue if the current total mass exceed the maximum load
            max_vol = f.maximum_volume()
            print('\nCalculation completed. Please enter C to check the result.')
            return max_vol, water_mass
        else:
            print('\nThe current water mass has exceeded the maximum load.\nPlease enter E to check total result.')
        return None, None

def display(max_vol, water_mass):
    global n, total_mass
    if max_vol is not None:  # Check if max_vol is not None
        print(f"\nThe maximum volume of this cylinder container is {max_vol:,.2f} m^3.")
        print(f"{water_mass:,.2f} kg of water is contained in the cylinder container.")
        n += 1
        total_mass += water_mass
        print(f'\n==================================================================================')
        print(f'Number of Container    |Volume of Container   |Water Mass      |Total Water Mass')
        print(f'{n}\t\t\t\t\t   ', f'{max_vol:,.2f}\t\t\t\t  ', f'{water_mass:,.2f}\t\t   ', f'{total_mass:,.2f}')
        print(f'==================================================================================')
        print(f'Please enter A to continue adding new cylinder container,\nor enter D to compare the result with maximum load.')
    else:
        print("\nThe current water mass has exceeded the maximum load.\nPlease enter E to check the total result.")


def compare(max_vol, water_mass):
    if total_mass <= maximum_load:
        print('''\nThe current water mass hasn't exceeded the maximum load yet.\nPlease enter A to continue adding new cylinder container.''')
    else:
        print('''\nThe current water mass has exceeded the maximum load.\nPlease enter E to check the total result.''')

def total():
    print(f'==================================================================================')
    print(f"The total water mass that the truck will contain is {total_mass:,.2f} kg.")
    print(f"It will take {n} cylinder containers to transfer this amount of water.")
    print(f'==================================================================================')

def exit_program():
    print('\nThank you for using Water Mass Calculator. See you next time!')
    quit()

while True:
    main_menu()
    letter = input("\nPlease enter A, B, C, D, E, or F to proceed: ").upper()
    #Ensure the program work properly when user enters the relative letter
    if letter == 'A':
        input_data()
    elif letter == 'B':
        max_vol, water_mass = calculate()
    elif letter == 'C':
        display(max_vol, water_mass)
    elif letter == 'D':
        compare(max_vol, water_mass)
    elif letter == 'E':
        total()
    elif letter == 'F':
        exit_program()
        break
    else:
        print("Invalid letter. Please enter A, B, C, D, E, or F.")
