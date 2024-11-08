# Prompt the user to enter a number
n = int(input("Enter any number: "))

# Initialize a variable to store the sum of the digits
digit_sum = 0

# Loop to calculate the sum of the digits
while n > 0:
    rem = n % 10          # Get the last digit of the number
    digit_sum += rem      # Add the last digit to the sum
    n = n // 10           # Remove the last digit from the number

# Print the sum of the digits
print("Sum of the digits:", digit_sum)