# Question 3- sum over 1+1/2 + 1/3 + ... till the sum does not change by more than 0.001

num = int(input("Enter the number of terms: "))

suma = 0
# for loop to get the summation upto num-1 term & store it in the suma 
for i in range(1, num):

    suma = suma+(1/i)
# making result as the final summation
result = suma+1/num
# using if and elif for conditioning the no. of terms used
if result-suma < 0.001:
    print("You can decrease the value of n as the summation is increasing by less than 0.001")
elif result-suma > 0.001:
    print("You should increase the number of term as the summation is increase by more tham 0.001")
print("The sum is", result)

