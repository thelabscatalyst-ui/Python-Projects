# we are setting a password:
password = input("Enter your password: ")
upper = 0 
digit = 0

if(len(password)>= 6 and len(password)<= 12):
    print("Password length is correct")
    for ch in password:
        if(ch.isupper()): #checks for uppercase character
            upper = 1
        if(ch.isdigit()): #checks for digit 
            digit = 1

    if(upper == 1 and digit == 1):
        print("Password has an uppercase character")
        print("Password has a digit")
        print("Password is valid")      

    elif(upper == 1):
        print("Uppercase criteria is passed")
        print("Password dosent conatin any digit")  
        print("Password is invalid")    

    elif(digit == 1):
        print("Digit criteria is passed")
        print("Password dosent conatin any uppercase character") 
        print("Password is invalid")       
else:
    print("Not within the correct range") 

# reffered as white box testing    
