inputNumber = input("Enter a number: ")

palindrome = inputNumber[::-1]

if palindrome == inputNumber:
    print(f"{inputNumber} is palindrome")
else:
    print(f"{inputNumber} is not a palindrome")