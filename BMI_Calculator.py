from math import pow
def calculate_bmi(height, weight):
    # Formula : weight / (height**2)
    bmi = weight / pow(height, 2)
    return bmi

def Category_bmi(bmi):
    # Categories based on BMI value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def userinput():
    while True:
        try:
            weight = float(input("Enter Your Weight in Kgs: "))
            height = float(input("Enter Your Height in m: "))
            if weight > 0 and height > 0:
                return weight, height
            else:
                print("Please enter valid positive values for weight and height.")
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

weight, height = userinput()
bmi_value = calculate_bmi(height, weight)
bmi_category = Category_bmi(bmi_value)

# Print the results
print("Your BMI value:{:.2f}".format(bmi_value))
print("BMI Category: ", bmi_category)
