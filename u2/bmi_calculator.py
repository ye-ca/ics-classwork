height_feet = int(input("Height in feet: "))
height_inches = float(input("Height in inches: "))
weight_pounds = float(input("Weight in pounds: "))

height = (height_feet * 12 + height_inches) * 0.0254  # Convert to meters
weight = weight_pounds * 0.453592  # Convert pounds to kilograms

bmi = weight / (height ** 2)
print(f"The BMI is {bmi}")