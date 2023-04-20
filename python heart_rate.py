# #project 1

# #A Python program named heart_rate.py that asks for a person’s age 
# #and computes and outputs the slowest and fastest rates for an athlete that 
# 21is necessary to strengthen his heart.

print()
a = int(input("Please enter your age: "))
print()

# Maximum heart rate per minute = b
b = int(220 - a)

# Fastest beneficial range = c
c = float(b * (85/100))

# Slowest benefical range = d
d = float(b * (65/100))

print("When you exercise to strengthen your heart, ")
print(f"you should keep your heart rate between: {d:.2f} and {c:.2f} beats per minute")
print()

