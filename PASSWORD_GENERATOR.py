import string 
import random
upper_case=[i for i in string.ascii_uppercase]
lower_case=[i for i in string.ascii_lowercase]
numbers=[i for i in string.digits]
special_char=[i for i in string.punctuation]
randomPassword=[]
choice="NO"
print("~~~~~~~~~~ PASSWORD GENERATOR ~~~~~~~~~~")
while(True):
    if choice=="NO" or choice=="NO".lower():
        length=int(input("ENTER THE LENGTH OF THE PASSWORD :"))
        upperCaseLength=int(input("HOW MANY UPPERCASE LETTERS WOULD YOU LIKE TO REQUIRE IN YOUR PASSWORD :"))
        if upperCaseLength>length:
            print("ERROR!..(PASSWORD LENGTH EXCEEDED) PLEASE TRY AGAIN")
        else:
            lowerCaseLength=int(input("HOW MANY LOWERCASE LETTERS WOULD YOU LIKE TO REQUIRE IN YOUR PASSWORD :"))
            if lowerCaseLength>length or (upperCaseLength+lowerCaseLength)>length:
                print("ERROR!..(PASSWORD LENGTH EXCEEDED) PLEASE TRY AGAIN")
            else:
                specialCharLength=int(input("HOW MANY SPECIAL CHARACTERS WOULD YOU LIKE TO REQUIRE IN YOUR PASSWORD :"))
                if specialCharLength>length or (upperCaseLength+lowerCaseLength+specialCharLength)>length:
                    print("ERROR!..(PASSWORD LENGTH EXCEEDED) PLEASE TRY AGAIN")
                else:
                    numberLength=int(input("HOW MANY NUMBERS WOULD YOU LIKE TO REQUIRE IN YOUR PASSWORD :"))
                    if numberLength>length or (upperCaseLength+lowerCaseLength+specialCharLength+numberLength)>length:
                        print("ERROR!..(PASSWORD LENGTH EXCEEDED) PLEASE TRY AGAIN")
                    else:
                        if (upperCaseLength+lowerCaseLength+specialCharLength+numberLength)<length:
                            print("ERROR!..(PASSWORD LENGTH IS LESS THAN THE DESIRED LENGTH) PLEASE TRY AGAIN")
                        else:
                        
                            for i in range(upperCaseLength):
                                randomPassword.append(random.choice(upper_case))
                            for i in range(lowerCaseLength):
                                randomPassword.append(random.choice(lower_case))
                            for i in range(specialCharLength):
                                randomPassword.append(random.choice(special_char))
                            for i in range(numberLength):
                                randomPassword.append(random.choice(numbers))
                            random.shuffle(randomPassword)
                            for i in range(length):
                                password="".join(randomPassword)
                            print("YOUR PASSWORD IS:",password)
                            choice=input("IS THIS PASSWORD OK FOR YOU (YES/NO): ")
    else:
        print("YOUR PASSWORD GENERATED SUCCESSFULLY")
        break
