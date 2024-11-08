import random
#simulating temprature reading
for i in range(1,11): # 10 temprature reading
    temperature = random.randint(20, 100)
    print(f"Randint {i}: temperature = {temperature} C")
    
    if temperature > 70:
        print("Danger! High temperature detected. Stopping monitaring.")
        break #stop monitaring when temperature exceeds safe limits