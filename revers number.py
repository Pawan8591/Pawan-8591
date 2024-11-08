# Prompt the user to enter a number
n = int(input("Enter any number: "))

# Initialize the variable to store the reversed number
rev = 0

# Loop to extract and reverse each digit of the number
while n > 0:
    rem = n % 10         # Get the last digit of the number
    rev = rev * 10 + rem # Append the digit to the reversed number
    n = n // 10          # Remove the last digit from the original number

# Print the reversed number
print("Reversed number:", rev)