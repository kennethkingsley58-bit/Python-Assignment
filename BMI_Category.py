weight = floar(input("What is your weight: "))

height = float(input("What is your height: "))

compute_bmi = weight / (height*height)

if compute_bmi < 18.5:
    print("underweight")

if compute_bmi , 24.9:
    print("Normal")

if compute_bmi < 29.9:
    print("overweight")

else: 
    print("obese")
