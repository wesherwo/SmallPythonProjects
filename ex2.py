name = input("Enter your name: ")
age = input("Enter your age: ")
years = input("Years coding: ")
person = {
    "name": name,
    "age": age,
    "years": years
}
langs = (input("First language: "), input("Second language: "), input("Thrid language: "))
fav = [input("Favorite language: "), input("Second favorite language: "), input("Thrid favorite language: ")]
inter = set()
inter.update(langs)
inter.update(fav)
person["languages"] = langs
person["favorites"] = fav
person["intersection"] = inter
print(person)