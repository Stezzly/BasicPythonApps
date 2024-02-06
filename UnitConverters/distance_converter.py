def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def meters_to_miles(meters):
    return meters * 0.000621371

def miles_to_meters(miles):
    return miles / 0.000621371

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def feet_to_inches(feet):
    return feet * 12

def inches_to_feet(inches):
    return inches / 12

# Test the functions
meters_input = 1000
kilometers_output = meters_to_kilometers(meters_input)
print(f"{meters_input} meters is equal to {kilometers_output:.2f} kilometers.")

kilometers_input = 5
meters_output = kilometers_to_meters(kilometers_input)
print(f"{kilometers_input} kilometers is equal to {meters_output:.2f} meters.")

miles_input = 10
meters_output = miles_to_meters(miles_input)
print(f"{miles_input} miles is equal to {meters_output:.2f} meters.")

meters_input = 5000
miles_output = meters_to_miles(meters_input)
print(f"{meters_input} meters is equal to {miles_output:.2f} miles.")

kilometers_input = 10
miles_output = kilometers_to_miles(kilometers_input)
print(f"{kilometers_input} kilometers is equal to {miles_output:.2f} miles.")

miles_input = 20
kilometers_output = miles_to_kilometers(miles_input)
print(f"{miles_input} miles is equal to {kilometers_output:.2f} kilometers.")

meters_input = 100
feet_output = meters_to_feet(meters_input)
print(f"{meters_input} meters is equal to {feet_output:.2f} feet.")

feet_input = 200
meters_output = feet_to_meters(feet_input)
print(f"{feet_input} feet is equal to {meters_output:.2f} meters.")

feet_input = 15
inches_output = feet_to_inches(feet_input)
print(f"{feet_input} feet is equal to {inches_output:.2f} inches.")

inches_input = 36
feet_output = inches_to_feet(inches_input)
print(f"{inches_input} inches is equal to {feet_output:.2f} feet.")
