usernum = int(input("Enter an integer: "))
mylist = []
fizz = 0
buzz = 0
fizzbuzz = 0
total = 0
for x in range(usernum + 1):
    total += x
    if x % 3 == 0 and x % 5 == 0:
        mylist.append('Fizzbuzz')
        fizzbuzz += 1
    elif x % 3 == 0:
        mylist.append('Fizz')
        fizz += 1
    elif x % 5 == 0:
        mylist.append('Buzz')
        buzz += 1
    else:
        mylist.append(x)
print(mylist)
print('Fizz = ' + str(fizz))
print('Buzz = ' + str(buzz))
print('Fizzbuzz = ' + str(fizzbuzz))
print('Total = ' + str(total))