#Rock-paper-scirss
import random

count = 0
while True:
    con_ch = random.randint(1,3)
    print(con_ch)

    count += 1

    if (count == 1):
        print("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
        print("Now Your turn: ", end="")
        pl_ch = int(input())
    else:
        print("Now Your turn: ", end="")
        pl_ch = int(input())

    if (pl_ch == 1 and con_ch == 3):
        print("You Win!")
        print("it takes %i times!" %count)
        break
    elif (pl_ch == 3 and con_ch == 1):
        print("You Lose!")
    elif (pl_ch > con_ch):
        print("You Win!")
        print("it takes %i times!" %count)
        break
    elif (pl_ch == con_ch):
        print("Rock-paper-scissor...")
    else:
        print("You Lose!")
