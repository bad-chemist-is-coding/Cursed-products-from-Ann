print("\nProject 2:\n\t KIỂM TRA NĂM NHUẬN")

year = int(input("Enter the year\n"))

if year % 4 ==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP YEAR")
        else:
            print("NOT A LEAP YEAR")
    else:
        print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")