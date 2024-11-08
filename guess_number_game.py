import random
for i in range(1,4): 
    n = random.randint(1, 10)
    # print(f"guess {i}:  = {n} ")
    g=int(input("enter your guess number"))
    print(f"guess {i}:  = {n} ")
    if n== g:
        print("your wing the game ")
        
        break
    else:
        print("plse try agein ")

print("you lost game, better luck next time")
        