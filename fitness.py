""" (Week3 team activity)
Health professionals who are helping a client achieve 
a healthy body weight, sometimes use two computed measures 
named body mass index and basal metabolic rate. 

write a Python program named fitness.py that does the following:
    Asks the user to enter four values:
        gender
        birthdate in this format: YYYY-MM-DD
        weight in U.S. pounds
        height in U.S. inches
    Converts the weight from pounds to kilograms(1 lb=0.45359237 kg).
    Converts inches to centimeters (1 in= 2.54 cm).
    Calculates age, BMI, and BMR.
    Prints age, weight in kg, height in cm, BMI, and BMR."""



# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender: ")
    birthday = input("Enter your birthday (Y-M_D): ")
    weight = float(input("Enter your weight (lb): "))
    height = float(input("Enter your height (inches): "))
    

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthday)
    print(f"Age (Years): {age}")
    kg = kg_from_lb(weight)
    print(f"Weight (Kg): {kg:.2f}")
    cm = cm_from_in(height)
    print(f"Height (cm): {cm:.1f}")
    body = body_mass_index(kg, cm) #issue
    print(f"Body Mass Index : {body:.1f}")
    bmr = basal_metabolic_rate(gender, kg, cm, age) #issue
    print(f"Basal metabolic rate: {bmr:.0f}")
    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(weight):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg_from_lb = weight * 0.45359237
    return kg_from_lb


def cm_from_in(height):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm_from_in = height * 2.54
    return cm_from_in


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    w = 10000 * weight
    body_mass_index = w / (height ** 2)
    return body_mass_index


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    # gender
    if gender == "f":
        basal_metabolic_rate1 = 447.593 + \
        (9.247 * weight) + (3.098 * height) - (4.330 * age)

    elif gender == "m":
        basal_metabolic_rate1 = 88.362 + \
        (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return basal_metabolic_rate1


# Call the main function so that
# this program will start executing.
main()



