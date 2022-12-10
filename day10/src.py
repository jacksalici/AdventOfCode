import sys

cycle = 1
registerX = 1
signalStrengths = 0



def checkSignalStrengths(n):
    global cycle, signalStrengths
    for i in range (0, n):
        if ((cycle-20)%40==0):
            signalStrengths+=cycle*registerX
            print(cycle, registerX, signalStrengths)
        
        cycle+=1




with open(sys.argv[1], "r") as file:
    for line in file:
        command = line.strip().split(" ")

        if command[0] == "noop":
            checkSignalStrengths(1)

        if command[0] == "addx":
            checkSignalStrengths(2)
            registerX+=int(command[1])

print(signalStrengths)





