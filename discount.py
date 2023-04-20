"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.

write a Python program named discount.py that gets a customer 
subtotal as input and gets the current day of the week from your 
computer operating system. 

Your program must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from your computer operating system.

    If the subtotal is $50 or greater and today is Tuesday or Wednesday,
    your program must subtract 10 % from the subtotal.   
    
    Your program must then compute the total amount due by adding sales tax of 6 % to the subtotal. 
   
    Your program must print the discount amount if applicable, the sales tax amount, 
    and the total amount due.

    import the datetime module so it can be used.

Core Requirements
    Your program asks the user for the subtotal but does not ask the user for the day of the week. 
    Your program gets the day of the week from your computer operating system.
    Your program correctly computes and prints the discount amount if applicable.
    Your program correctly computes and prints the sales tax amount and the total amount due ."""

from datetime import datetime

# Discount rate is 10% and tax rate is 6%.
discount_rate = 0.10
tax_rate = 0.06

# Get the subtotal from user
subtotal = float(input("Please enter your subtotal: "))

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()
day_of_week = 1
# If the subtotal is greater than 50 and today is
# Tuesday or Wednesday, compute the discount amount.
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = round(subtotal * discount_rate, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount

# Compute the sales tax. Notice that we compute the sales tax
# after computing the discount because the customer does not
# pay sales tax on the full price but on the discounted price.
sales_tax = round(subtotal * tax_rate, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

# Compute the total by adding the subtotal and the sales tax.
total = subtotal + sales_tax

# Display the total for the user to see.
print(f"Total: {total:.2f}")

