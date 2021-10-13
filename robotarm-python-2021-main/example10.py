from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
move = 9

# Jouw python instructies zet je vanaf hier:

robotArm.grab()
for x in range(5):
    for x in range(move):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(move-1):
        robotArm.moveLeft()
    robotArm.grab()
    move = move-2
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()