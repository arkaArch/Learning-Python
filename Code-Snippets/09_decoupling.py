#- Decoupling is the practice of reducing the interdependence between
#- components(like function, class) to make the code more adaptable,
#- maintainable, and scalable

feet_inches = input("Enter height in feet and inches: ")

def parse(height):
    parts = height.split(" ")
    l_feet = float(parts[0])
    l_inches = float(parts[1])
    return l_feet, l_inches    # This will return a tuple

def feet_inches_to_meter(l_feet, l_inches):
    meters = l_feet * 3048 + l_inches * 0.0254
    return meters

# feet_inches_tuple = parse(feet_inches)
# height_in_meters = feet_inches_to_meter(feet_inches_tuple[0], feet_inches_tuple[1])

# We can write the above two lines as:
feet, inches = parse(feet_inches)
height_in_meters = feet_inches_to_meter(feet, inches)

if height_in_meters < 1:
    print("Sorry! you can't go to the next level")
else:
    print("Congratulation! Go to next level")