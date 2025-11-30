# ---------------------------------------------
# Manufacturing Aid Program
# Get user input for material type, part length, width, and height
# Calculate and display Mfg Equipment and Picture
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

def getCategory(dim, material):
    """
    Determine the  based on value.
    """
    category = ""
    if dim <= 6400 and material == 'metal':
        category = "Mid-size VF-1 Vertical Mill" #Limit is 20" x 16" x 20"
    elif dim <= 61440 and material == 'metal':
        category = "Industrial VF-6/40 Vertical Mill" #Limit is 64" x 32" x 30"
    elif dim <= 738 and material == 'plastic':
        category = "Ender 3 Pro 3D Printer" #Limit is 8.7" x 8.7" x 9.8"
    elif dim <= 8000 and material == 'plastic':
        category = "Sovol SV08 Max 3D Printer" #Limit is 20" x 20" x 20"
    else:
        category = "Process cannot be defined"
    return category

# --- Main Program ---
print("Manufacturing Aid Program")

# Ask for user's name
name = input("Enter your name: ")

# Get material preference
material = input("Enter material, 'plastic' or 'metal'?: ")

# Get valid positive inputs for length, width, and height 
length = getPositiveNumber("Enter length (inches): ")
width = getPositiveNumber("Enter width (inches): ")
height = getPositiveNumber("Enter height (inches): ")

dimValue = calculatedim(length, width, height)
category = getCategory(dimValue, material) 

print(f"Name:{name},", f"the suggested Manufacturing Equipment that should be used is: {category}")
