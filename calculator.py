import os
def menu():
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.Exit")
    choice = int(input("Enter Your Choice:"))
    return choice


while True:
    try:
        os.system("cls")
        a = float(input("Enter 1st Value:"))
        b = float(input("Enter 2nd Value:"))
        match menu():
            case 1:
                print("Addition is:",a+b)
            case 2:
                print("Subtraction is:",a-b)
            case 3:
                print("Multiplication is:",a*b)
            case 4:
                print("Division is:",a/b)
            case 5:
                print("Remainder is:",a%b)
            case 6:
                print(f"{a} power {b} is {a**b}")
            case 7:
                exit(0)
            case _:
                print("Invalid Choice")
        input("Press Enter Key to Continue")
    except:
        print("Something Went Wrong")
        break
    
        







