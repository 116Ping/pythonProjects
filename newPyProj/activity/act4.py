fibonacciNumber = int(input("Enter the number of terms: "))

a,b=0,1

print("Fibonacci sequence: ", end=" ")

for num in range(fibonacciNumber):
    print(a, end=" ")
    a, b = b, a+b



