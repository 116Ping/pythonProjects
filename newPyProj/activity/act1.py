lowerBound = int(input("Enter the lower bound:"))
upperBound = int(input("Enter the upper bound:"))

for num in range(lowerBound, upperBound):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")

