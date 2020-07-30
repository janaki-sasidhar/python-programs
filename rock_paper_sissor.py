import os,random,sys
tie_score=0
user_score=0
comp_score=0
flag=0
option=input("Do you want to play the game? (yes/no) ").lower()
if option=="yes":
    num=int(input("How many games do you wanna play ? "))
    print('''The instructions are
    1.Rock vs Paper --> Paper wins
    2.Rock vs sissor --> Rock wins
    3.Paper vs sissor --> sissor wins''')

    print('''The choice must be
    1.Rock
    2.Paper
    3.Sissor''')
    while flag<num:
        comp_choice=random.randint(1,3)
        user_choice=int(input("Enter the choice "))
        if user_choice<1 or user_choice>3:
            print("You must choose the value between 1 and 3. You will lose a game if you choose out of bounds")
            continue
        else:
            flag=flag+1
            if comp_choice==1 and user_choice==1:
                tie_score+=1
            elif comp_choice==1 and user_choice==2:
                user_score+=1
            elif comp_choice==1 and user_choice==3:
                comp_score+=1
            elif comp_choice==2 and user_choice==1:
                comp_score+=1
            elif comp_choice==2 and user_choice==2:
                tie_score+=1
            elif comp_choice==2 and user_choice==3:
                user_score+=1
            elif comp_choice==3 and user_choice==1:
                user_score+=1
            elif comp_choice==3 and user_choice==2:
                comp_score+=1
            elif comp_choice==3 and user_choice==3:
                tie_score+=1
    print("The user_score is ",user_score)
    print("The computer score is ",comp_score)
    print("The tie score is ",tie_score)
    again=input("Do you want to play again ? (yes/no)").lower()
    if again=="yes":
        os.system('clear')
        os.system("python rock_paper_sissor.py")


else:
    print("Ok, you can play next time" )
