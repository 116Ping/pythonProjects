number = int(input("Enter a number: "))

result = 1

for i in range(2, number +1):
    result *= i
print(f"the factorial of {number} is: {result}")

