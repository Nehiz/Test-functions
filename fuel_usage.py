
""" (week 3 checkpoint)
Many vehicle owners record the fuel efficiency of
their vehicles as a way to track the health of the vehicle. 
If the fuel efficiency of a vehicle suddenly drops, 
there is probably something wrong with the engine 
or drive train of the vehicle. 

Write a Python program that asks the user for three numbers:
    A starting odometer value in miles
    An ending odometer value in miles
    An amount of fuel in gallons
Your program must calculate and print fuel efficiency in both 
miles per gallon and liters per 100 kilometers. 

Your program must have three functions named as follows:
    main
    miles_per_gallon
    lp100k_from_mpg
All user input and printing must be in the main function. 
In other words, the miles_per_gallon and lp100k_from_mpg functions must 
not call the the input or print functions. """

#import math


def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles =  float(input("Enter first odometer value: "))
    
    # Get another odometer value in U.S. miles from the user.
    end_miles = float(input("Enter last odometer value: "))
   
    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons = float(input("Enter fuel amount: "))
    
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    
    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.1f} litres per {100} kilometer")
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    miles_per_gallon = (end_miles - start_miles) / amount_gallons
    return miles_per_gallon


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k_from_mpg = 235.215/mpg
    return lp100k_from_mpg


# Call the main function so that
# this program will start executing.
main()
