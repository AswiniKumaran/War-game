import random
digits=[str(numbers) for numbers in range(10)]
random.shuffle(digits)
number=(digits[:3])
print(number)
c=""
while(c!="Close"):
    guess=input("Guess the number")
    l=guess
    if(l[0]==number[0] and l[1]==number[1] and l[2]==number[2]):
        print("Correct Guess")
        c="Close"
    elif(l[0]==number[0] or l[1]==number[1] or l[2]==number[2]):
        print("Match")
    else:
        print("Nope")
