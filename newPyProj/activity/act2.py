numbers = int(input("Enter a number: "))
digits = str(numbers)
power = len(digits)

sum =0
for num in digits:
    sum += int(num)**power

if sum == numbers:
    print(f"{sum} is an armstrong number")
else:
    print(f"{sum} is not armstrong number")


