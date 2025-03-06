words = input("Enter a string: ")

stringToFind = input("Enter the substring to find: ")

newWord = words.find(stringToFind)

print(f"the substring \'{stringToFind}\' is found at index {newWord}")