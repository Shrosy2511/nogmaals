from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
color = robotArm.scan()

# Jouw python instructies zet je vanaf hier:
for c in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

while color == '':
    for c in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    if robotArm.scan() == 'red' or robotArm.scan() == 'green' or robotArm.scan() == 'white' or robotArm.scan() == 'blue':
        robotArm.moveRight()
        robotArm.drop()
    elif robotArm.scan() == '':
        break

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()