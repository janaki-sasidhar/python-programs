import random,string

isCapital=False

isSpecialCharacter=False

bigalpha_list=[chr(i) for i in range(65,65+26)]

smallalpha_list=[chr(i) for i in range(97,97+26)]

specialCharList=[i for i in list(string.punctuation)]
def password_generator():
    li=[]
    whole=num//4
    if isCapital==True:
        for i in range(whole):
           li.append(random.choice(bigalpha_list))
    if isSpecialCharacter==True:
        for i in range(whole):
            li.append(random.choice(specialCharList))
    for i in range(whole):
        li.append(random.choice(smallalpha_list))
    for i in range(whole):
        li.append(str(random.randint(0,9)))
    for i in range(num-len(li)):
        li.append(random.choice(smallalpha_list))
    random.shuffle(li)
    print(''.join(li))
   

def main():
    global num ,isSpecialCharacter,isCapital
    while True:
        try:
            num=int(input("How many digit password you wanna generate? ")) 
        except ValueError:
            print("Enter only integers")
            continue
        cap=input("Do you want to include capital letters in the alphabet ?(yes/y/no/n) ").lower()
        if cap=="yes" or cap=="y":
            isCapital=True
        spchar=input("Do you want to include special characters in the alphabet ? (yes/y/no/n").lower()
        if spchar=="yes" or spchar=="y":
            isSpecialCharacter=True
        password_generator()
        break
if __name__ == "__main__":
    main()
