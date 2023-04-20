"""
Write a program named tire_volume.py that computes the
approximate volume of air inside a tire. 

Add code near the end of that program that does the following:
    Gets the current date from the computer operating system.
    Opens a text file named volumes.txt for appending.
    Appends to the end of the volumes.txt file one line of text that 
    contains the following five values:
        current date
        width of the tire
        aspect ratio of the tire
        diameter of the wheel
        volume of the tire. """




# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Import the math module to use math.pi and math.sqrt.
import math

# Print a description of this program for the user to see.
print("This program reads from the keyboard the width, aspect ratio, ")
print("and diameter of a tire, and computes and outputs ")
print("the volume of space inside that tire. ")

# Display a blank space.
print()

# Get the three numbers of the tire from the keyboard.
width = float(input("Enter the width of the tire in mm (ex 205) : "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 50) : "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15) : "))

#computes the volume of the tire in litres.
x = (math.pi * width**2 * aspect_ratio)
y = (width * aspect_ratio + 2540 * diameter)
volume = x * y / 10000000000

# Display a balnk space
print()

# Print result for the user to see.
print(f"The approximate volume of this tire is {volume:.2f} litres")

#Add a set of if … elif … else statements that use the tire width,
# tire aspect ratio, and wheel diameter that the user enters to find a price and then print the price.
if volume >= 50:
    print(f"kindly note that tires with these dimensions are currently available for between {112} to {125} dollars.")

elif volume >= 40:
    print(f"kindly note that tires with these dimensions are currently available for approximately {99.5} dollars.")

else:
    print(f"kindly note that tires with these dimensions are currently available for less than {50.9} dollars.")

print()
# Ask the user if she wants to buy tires with the dimensions that she entered
text_1 = input("Do you want to proceed to buy a tire with the dimensions you entered above? ")

#If the user answers “yes”, your program should ask for her phone number and 
# also store her phone number in the volumes.txt file.
if text_1 == "yes":
    phone_number = int(input("Please enter your phone number: "))
    print("Your order has been noted. Thanks for using this program.")

elif text_1 == "no":
    print("Thanks for using this program.")
    

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print only the date
# part of the current date and time.
print(f"{current_date_and_time:%Y-%m-%d}")

# Opens a text file named volumes.txt for appending.
with open("volumes.txt", "at") as volumes_file:

    #Appends to the end of the file a line of text that contains the 
    # following five values: current date, width of the tire, 
    # aspect ratio of the tire, diameter of the wheel and volume of the tire.
    print(f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {phone_number}, {volume:.2f}", file=volumes_file)
print()

