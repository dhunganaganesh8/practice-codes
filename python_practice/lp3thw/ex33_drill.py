def while_loop(var1, var2, increment):
    list = []
    while var1 <= var2:
        list.append(var1)
        var1 = var1 + increment
    return list

elements = []
elements = while_loop(int(input("Lower range: ")), int(input("Upper range: ")), int(input("increment? ")))
print(elements)
