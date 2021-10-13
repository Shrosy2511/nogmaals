from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:

for x in range(7):
    while robotArm.scan() == "":
        robotArm.grab()
        if robotArm.scan() == "white":
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveRight()
            break
        else:
            robotArm.drop()
            robotArm.moveRight()
        break


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()