# Task 2: BMI Calculator Program
def calculate_bmi(name: str, weight_kg: float, height_cm: float):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Healthy"
    elif 25.0 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    with open("bmi.csv", "a") as file:
        file.write(f"{name}, {height_cm}, {weight_kg}, {bmi:.2f}, {category}\n")
    print(f"{name}'s BMI is {bmi:.2f}, Category: {category}")

# Running the function
if __name__ == "__main__":
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    calculate_bmi(name, weight, height)
