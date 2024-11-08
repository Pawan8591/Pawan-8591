# Prompt the user to enter a number
num = int(input("Enter any number: "))

# Initialize the factorial variable
factorial = 1

# Loop to calculate the factorial of the number
while num >= 1:
    factorial *= num  # Multiply the current factorial by the current number
    num -= 1          # Decrease the number by 1 for the next iteration

# Print the resulting factorial
print("Factorial of the given number is:", factorial)    
'''
51-5-4*3*2*1-120

iteration 1:num-5 factorial-factorial num-5-1-4 5>1 P num-1-5-5

iteration 2: num-4 4>1 T factorial-factorial num=5*4-20 num-4-1-3

iteration 3:3>1 T

factorial-20*3-60 num-2

iteration 5: 1>1 f

Iteration 4:2>1 t fact-60-2-120
'''