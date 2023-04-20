# n = float(input("Please enter a number: "))
# r = round(n)
# print(r)

# import math

# number = float(input("Enter a number: "))

# root = math.sqrt(number)

# print(f"The square root is{ root:.2f}")

miles = float(input("Please enter a distance in miles: "))
def kilometers_from_miles(miles):
    """Convert a value in miles to kilometers
    and return the kilometers value.
    """
    km = miles * 1.60934
    return km
