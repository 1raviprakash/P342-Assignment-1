# Question 2- Factorial n! say for n=10 or 15, check and trap negative integers, say for -5!


num = int(input("Enter the number of which you want to have the Factorial"))

# Result is the Factorial
result = 1
# hold is used here to store the initial value in num
hold = num
# if is used here so that negative inputs can be avoided
if num < 0:
    print("Enter a positive Integer number")
elif num == 0:
    print("The factorial of 0 is", result)
else:
    # While loop for the factorial calculation
    while num > 0:
        result = result*num
        num = num-1
    print("The factorial of ", hold, " is:", result)
