import random

def gen_password(length,choice):
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_symbol = '''!@#$%^&*()-=_+[]{}|;:'\",.<>?/'''
    if choice==1:
        all_characters = alphabets
    elif choice==2:
        all_characters = alphabets+digits
    else:
        all_characters = alphabets+digits+special_symbol

    password = ''.join([random.choice(all_characters) for x in range(length)])
    return password

def choice():
    print("Select the Complexity Level of the Password:")
    print("1.Weak")
    print("2.Medium")
    print("3.Hard")
    choice = int(input("\nEnter Your Choice:"))
    return choice

pass_length = int(input("Enter Length of Password:"))
ch = choice()
print("Generated Password:",gen_password(pass_length,ch))


