height_feet = int(input("Height in feet: "))
height_inches = float(input("Height in inches: "))
weight_pounds = float(input("Weight in pounds: "))

height = (height_feet * 12 + height_inches) * 0.0254  # Convert to meters
weight = weight_pounds * 0.453592  # Convert pounds to kilograms

bmi = weight / (height ** 2)

if bmi < 15:
    category = "very severely underweight"
if bmi >= 15 and bmi < 16:
    category = "severely underweight"
if bmi >= 16 and bmi < 18.5:
    category = "underweight"
if bmi >= 18.5 and bmi < 25:
    category = "normal (healthy weight)"
if bmi >= 25 and bmi < 30:
    category = "overweight"
if bmi >= 30 and bmi < 35:
    category = "obese class I (moderately obese)"
if bmi >= 35 and bmi < 40:
    category = "obese class II (severely obese)"
if bmi >= 40:
    category = "obese class III (very severely obese)"

print(f"Your BMI is {bmi:.2f}")
print(f"BMI Category: {category}")