import os

Fname = input("Enter your first name: ")
Lname = input("Enter your last name: ")
Mname = input("Enter your middle name: ")
birthday = input("Enter your birthday: ")
gender = input("Enter your gender: ")
address = input("Enter your address: ")
course = input("Enter your course: ")
yearLevel = input("Enter your year level: ")

print("-----------------------------")
print(f"Name: ", Fname, Mname, Lname)
print(f"Birthday: ", birthday)
print(f"Gender: ", gender)
print(f"Address: ", address)
print(f"Course: ", course)
print(f"Year Level: ", yearLevel)
print("-----------------------------")
os.system("pause")