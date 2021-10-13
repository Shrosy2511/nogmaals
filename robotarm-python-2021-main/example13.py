from RobotArm import RobotArm

robotArm = RobotArm('exercise 13')
robotArm.randomLevel(1,7)
move = 1

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
while robotArm.scan() != "":
    for x in range(move):
        robotArm.moveRight()
    robotArm.drop()
    move = move + 1
    for x in range(move):
        robotArm.moveLeft()
    robotArm.grab()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()