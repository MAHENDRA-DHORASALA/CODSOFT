print("~~~~~~~~~~~SIMPLE CALCULATOR~~~~~~~~~~~~~~")
l=["ADDITION","SUBTRACTION","MULTIPLICATION","DIVISION"]
while True:
    print("\nPRESS 1 FOR ADDITION\nPRESS 2 FOR SUBTRACTION\nPRESS 3 FOR MULTIPLICATION\nPRESS 4 FOR DIVISION\nPRESS 5 FOR EXIT")
    choice=int(input("ENTER YOUR CHOICE : "))
    if choice<=5 and choice>=1:
        if choice==5:
            print("YOU ARE EXITED")
            break
        else:
            print("YOU CHOOSEN",l[choice-1])
            NUMBER1=int(input("ENTER THE VALUE OF FIRST NUMBER :"))
            NUMBER2=int(input("ENTER THE VALUE OF SECOND NUMBER :"))
            if choice==1:
                print(f"ADDITION OF {NUMBER1} and {NUMBER2}  IS :",NUMBER1+NUMBER2)
            elif choice==2:
                print(f"SUBTRACTION OF {NUMBER1} and {NUMBER2} IS :",NUMBER1-NUMBER2)
            elif choice==3:
                print(f"MULTIPLICATION OF {NUMBER1} and {NUMBER2} IS :",NUMBER1*NUMBER2)
            elif choice==4:
                print(f"DIVISION OF {NUMBER1} and {NUMBER2} IS :",NUMBER1/NUMBER2)
    else:   
        print("INVALID CHOICE ...PLEASE TRY AGAIN")