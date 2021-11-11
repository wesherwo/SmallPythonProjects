from datetime import datetime

first, last = input("Enter you full name: ").split()
first = first.lower().capitalize()
last = last.lower().capitalize()

age = int(input("Enter your age: "))
year = datetime.now().year - age

email = first + "." + last + str(year % 100) + "@company.com"

print(first, last, age, year, email)