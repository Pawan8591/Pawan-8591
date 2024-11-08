# Prompt the user to enter a number
n = int(input("Enter any number: "))

# Initialize a counter to count the digits
digit_count = 0

# Loop to count the digits in the number
while n > 0:
    rem = n % 10          # Get the last digit of the number (not used here but can be useful)
    n = n // 10           # Remove the last digit from the number
    digit_count += 1      # Increment the digit counter

# Print the total number of digits
print("Number of digits:", digit_count)
