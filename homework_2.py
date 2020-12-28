first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
date_of_birth = input("Enter your date of birth(just year): ")

myList = []
myList.append(first_name)
myList.append(last_name)
myList.append(age)
myList.append(date_of_birth)

for i in range(len(myList)):
    print(myList[i])

if(int(age) < 18):
    print("You can't go out because it's too dangerous")

else:
    print("You can go out to the street.")
