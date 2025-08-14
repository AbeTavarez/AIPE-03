# This is my first program

# String (Text)
print("Hello...")

print('world!')

print("33" + "2")

# Integers (numbers)
print("Addition: ", 33 + 2)
print("Subtraction: ", 33 - 2)
print("Multiplication: ", 33 * 2)
print("Division: ", 33 / 2)
print("Modulus: ", 31 % 2)
print("Float division: ", 33.5 / 2)

# Variables
my_name = "Abraham"
age = 12

# boolean (True, False)
is_student = False
is_verified = False
print("is_verified: ", is_verified)

# 100 lines later...

# Conditionals
if is_verified:
    print(f"Hello, my name is {my_name} and I am {age} years old.")
else: 
    print("You are not verified.")
    
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
    
message = "Practice Programming    "
print(message.upper())
print(message.lower())
print(message.rstrip())
print(len(message))
