i = input('type hier een woord ')
x = 0
while i != 'quit':
    i = input('type hier een woord ')
    x = x + 1
    if i == 'quit':
        print('goed geraden' + 'je hebt ' + str(x) + ' keer geprobeerd te raden')
