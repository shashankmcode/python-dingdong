# Take user input for the number
num = int(input("Enter a number: "))
check=num
# Initialize a variable to store the reversed number
reversed_num = 0

# Reverse the number using a loop
while num != 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Append the digit to the reversed number
    #temp=reversed_num
    num = num // 10  # Remove the last digit
if reversed_num == check:
    print('yes')
else:
    print('not a pl')
