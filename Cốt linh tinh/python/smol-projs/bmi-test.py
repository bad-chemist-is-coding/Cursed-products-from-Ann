print("\nProject 1:\n\t KIỂM TRA BMI")

while True:
    weight = float(input("How fat are you (kg)?\n"))
    height = float(input("How short are you (m)?\n"))
    bmi = round( weight / height ** 2 )

    if bmi < 18.5:
        print(f"Your bmi is {bmi}, you are a skeleton! (underweight)")
    elif bmi < 25:
        print(f"Your bmi is {bmi}, you are a person! (normal weight)")
    elif bmi < 30:
        print(f"Your bmi is {bmi}, you better save your ass with diets! (overweight")
    elif bmi < 35:
        print(f"Your bmi is {bmi}, you need to save your ass with diets! (obese)")
    else:
        print(f"You bmi is {bmi}, you must save your ass with diets!!! (clinically obese\n")

    var = input('Wanna try again? (Y/N)\n')
    if var.lower().startswith('n'):
        print('Improve your health then come back to me!')
        break