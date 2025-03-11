string = input("Enter words separated by spaces: ")
list = string.split()

joinedString = "-".join(list)

print(f"Joined string {joinedString}")