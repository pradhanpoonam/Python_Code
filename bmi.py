#Adding comments
print("Let us calculate your BMI")
height = float(input("Enter your height in metres\n"))
weight = float(input("Enter your weight in KG\n"))

BMI = round(weight/(height**2))

print("bmi is:" + str(BMI))

if BMI <= 18.5:
    print("You are nderweight")
elif BMI <= 25:
    print("You are Normal")
elif BMI <= 30:
    print("You are Overweight")
elif BMI <= 35:
    print("You are Obese")
else:
    print("You are Clinically Obese")
