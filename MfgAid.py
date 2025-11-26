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

def calculatedim(length, width, height):
    dim = (length*width*height)
    return dim

def getCategory(dim):
    """
    Determine the BMI category based on value.
    """
    category = ""
    if dim < 20:
        category = "Small"
    elif dim < 50:
        category = "Normal"
    elif dim < 80:
        category = "Large"
    else:
        category = "Massive"
    return category

# --- Main Program ---
print("Manufacturing Aid Program")

# Ask for user's name
name = input("Enter your name: ")

# Get valid positive inputs for length, width, and height 
length = getPositiveNumber("Enter length (inches): ")
width = getPositiveNumber("Enter width (inches): ")
height = getPositiveNumber("Enter height (inches): ")

dimValue = calculatedim(length, width, height)
truebmi = round(dimValue)
category = getCategory(dimValue)

print(f"Name:{name}", f"your part is {truebmi} cubic inches,", f"Status:{category}")
