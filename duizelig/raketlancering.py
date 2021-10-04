import time

countdown = 30
while countdown >= 1:
    time.sleep(1)
    print('countdown ' + str(countdown))
    countdown = countdown - 1
time.sleep(1)
print('lift off!')