import sys

cycle = 1
registerX = 1
signalStrengths = 0
crt = ['.' for i in range(240)]

def printCRT():
    for index, px in enumerate(crt):
        if (index+1)%40==0:
            endline = '\n'
        else:
            endline = ''
        print(px,end=endline)


def checkDrawingCRT():
    #registerX controls the sprite (3 px wide), cycle-1 controls the actual pixel drawn
    global crt,cycle,registerX
    position = (cycle-1)%40
    sprite = registerX
    if position == sprite or position == sprite -1 or position == sprite +1:
        crt[cycle-1]='#'
    


def checkSignalStrengths(n):
    global cycle, signalStrengths
    for i in range (0, n):
        if ((cycle-20)%40==0):
            signalStrengths+=cycle*registerX

        checkDrawingCRT()
        
        cycle+=1




with open(sys.argv[1], "r") as file:
    for line in file:
        command = line.strip().split(" ")

        if command[0] == "noop":
            checkSignalStrengths(1)

        if command[0] == "addx":
            checkSignalStrengths(2)
            registerX+=int(command[1])

print("signalStrengths = ", signalStrengths)
printCRT()




