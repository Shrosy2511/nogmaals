x = 50
i = x + 1
c = x + i
while x <= 1000:
    c = i + x 
    print(str(x)+ ' + ' + str(i) + ' = ' + str(c))
    x = x + i
    i = i + 1