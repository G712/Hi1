list = [1, 2, 3]
number = int(input("Please type in a number: "))
var = 0
if number > list[0]:
    var = var + 1
if number > list[1]:
    var = var + 1
if number > list[2]:
    var = var + 1
var = str(var)
print("Your number is greater than " + var + "(no) number(s) in our list.")