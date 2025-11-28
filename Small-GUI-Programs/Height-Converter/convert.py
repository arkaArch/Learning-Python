def feet_inches_to_cm(feet, inches):
    if type(feet) == str:
        feet = float(feet)
    if type(inches) == str:
        inches = float(inches)
        
    return (feet * 30.48) + (inches * 2.54)