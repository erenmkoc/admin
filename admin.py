import time
username = input("Enter username:")
password = input("Enter password:")
print("Registration successful!")
enter = input("Do you want to login?(Yes/No):")
if((enter == "Yes")or(enter == "yes")): 
    while (True):
        username1 = input("Username:")
        password1 = input("Password:")
        if((username1 == username) and (password1 == password)):
            print("Welcome!", username1)
            break
        elif ((username1 != username) and (password1 == password)):
            print("You entered wrong username!")
        elif ((username1 == username) and (password1 != password)):
            print("Forgot your password?")
            print("Do you want to change your password? (Yes/No):")
            cevap = input()
            if ((cevap == "Yes") or (cevap == "yes")):
                new_password = input("New password:")
                print("Please wait...")
                time.sleep(2)
                password = new_password
                print("**************************")
                print("Password changed!")


            else:
                print("Try again...")

else:
    ((enter == "No") or (enter == "no"))
    
