import json


def inputUserDetails():
    details = {}


    details["first name"] = input("Enter name: ").title()
    details["last name"] = input("Enter last name: ").title()
    details["age"] = int(input("Enter age: "))
    return details



entry = input("enter entry(Y/N): ").upper()

if entry == "Y":
    inputUserDetails()
    userdata = json.dumps(inputUserDetails())
else:
    print("end")

print(json.loads(userdata))

