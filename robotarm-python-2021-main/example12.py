from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:

for x in range(10,1,-1):
    robotArm.grab()
    if robotArm.scan() == "red":
        for x in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(x-1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()

    
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()