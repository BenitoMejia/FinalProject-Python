# ---------------------------------------------
# Manufacturing Aid Program
# Get user input for material type, part length, width, and height
# Calculate and display Mfg Process and Picture
# ---------------------------------------------

def getPositiveNumber(prompt):
    """
    Ask the user for a positive number using a while loop.
    Repeats until the user enters a value greater than 0.
    """
    value = 0
    while value <= 0:
        # Prompt the user for input
        value = float(input(prompt))
        # Check if input is positive
        if value <= 0:
            print("Please enter a positive number greater than zero.")
    return value

def calculatedim(weight, height):
    dim = (weight/(height*height))*703
    return dim

def getCategory(dim):
    """
    Determine the BMI category based on value.
    """
    category = ""
    if dim < 18.5:
        category = "Underweight"
    elif dim < 25:
        category = "Normal"
    elif dim < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return category

# --- Main Program ---
print("Manufacturing Aid Program (Python)")

# Ask for user's name
name = input("Enter your name: ")

# Get valid positive inputs for weight and height
weight = getPositiveNumber("Enter weight (lbs): ")
height = getPositiveNumber("Enter height (inches): ")

bmiValue = calculatedim(weight, height)
truebmi = round(bmiValue)
category = getCategory(bmiValue)

print(f"Name:{name}", f"Your BMI is:{truebmi}", f"Status:{category}")
