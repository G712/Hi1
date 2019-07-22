var = "NOTHING"
while var != "stop":
    var = input("Type a word:")
    for i in range(0,len(var)):
        print(var[i])
