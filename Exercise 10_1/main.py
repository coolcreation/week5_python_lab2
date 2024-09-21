#!/usr/bin/env python3
# Jeff Bohn
# 9/19/2024
# main.py
# SWDV210 - Week_5-Lab_2
# Chapter 10 - Working with Strings

################# Exercise 10-1 : Create Account Program #################


def main():
    print("\nCreate an account\n")

    full_name = get_full_name()
    password = get_password()
    email = get_email()
    phone_number = get_phone_number()
    print()
    # print("Phone Number: ".ljust(25), phone_number)
    
    first_name = get_first_name(full_name)  
    # print(f"Hi {first_name}, thanks for creating {email} account. Your password is: {password}" ) 
    print(f"Hi {first_name}, thanks for creating an account. We'll text you your confirmation code to this number: {phone_number}" )             
    
def get_full_name():
    while True:
        name = input("Enter full name: ".ljust(26)).strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password: ".ljust(26)).strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password
        
def get_email():
    while True:
        my_email = input("Enter email address: ".ljust(26)).strip().lower()
        length = len(my_email)
        com_location = my_email.find(".com")
        at_checker = my_email.find("@")
        # print(length, com_location, at_checker)

        if length - com_location == 4 and at_checker > -1 and at_checker < (len(my_email) -6):
            return my_email
        else:
            print("Please enter a valid email address")
            continue


def get_phone_number():
    while True:
        p_n = input("Enter phone number: ".ljust(26))
        problem_chars = [" ", "(", ")", "-", "."]
        for i in problem_chars:
            if i in p_n:
                p_n = p_n.replace(i, "")

        print(isinstance(p_n, int), p_n)           #  p_n = phone number
        if len(p_n) == 10:                         #  is the string 10 characters?
            p_n = int(p_n)
            if isinstance(p_n, int):               #  is the string able to be converted to int?
                p_n = str(p_n)                     #  convert back to string to add periods between number sets
                new_string = ''                    
                                                   
                for i in range(len(p_n)):
                    new_string += p_n[i]
                    # print(i, p_n[i], new_string)
                    if i == 2 or i == 5:
                       new_string += "."

                return new_string
            else:
                print("Please enter a 10 digit phone number")
                continue
        else:
             print("Please enter a 10 digit phone number")


        
if __name__ == "__main__":
    main()