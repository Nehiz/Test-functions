
"""A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. 

Write a Python program named boxes.py that asks the user for two integers:  
1) the number of manufactured items, and 
2) the number of items that the user will pack per box. 
Your program must compute and print the number of boxes necessary to hold the items. 

This must be a whole number. Note that the last box may be packed with fewer items 
than the other boxes. """

# A program that compute and print the number of boxes necessary to hold the items manufactured by a company.

# Import the math module so that we can call the math.ceil function.
import math

# Get two numbers of items from user
number_of_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the numbers of items per box: "))

# Compute the number of boxes by dividing and then calling the math.ceil function.
# call the math.ceil() function and immediately use its return value
num_of_boxes = (math.ceil(number_of_items/items_per_box))

#display blank space
print()

print(f"For { number_of_items} items, packing { items_per_box} items in each box, you will need {num_of_boxes} boxes.")

