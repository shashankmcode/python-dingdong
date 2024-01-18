# Take user input for the number
num = int(input("Enter a number: "))

# Initialize a variable to store the reversed number
reversed_num = 0

# Reverse the number using a loop
while num != 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Append the digit to the reversed number
    num = num // 10  # Remove the last digit
# Print the reversed number
print("Reversed number:", reversed_num)
