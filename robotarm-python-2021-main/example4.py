from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for i in range(3,0,-1):
    robotArm.grab()
    for c in range(i):
        robotArm.moveRight()
    robotArm.drop()
    for c in range(i):
        robotArm.moveLeft()

for c in range(2):
    robotArm.moveRight()
robotArm.grab()

for c in range(1):
    robotArm.moveLeft()
robotArm.drop()

for c in range(2):
    robotArm.moveRight()
robotArm.grab()
    
for c in range(2):
    robotArm.moveLeft()
robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()