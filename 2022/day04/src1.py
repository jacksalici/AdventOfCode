import sys

nAssignmentsFullyContained = 0
nAssignmentsOverlapping = 0
with open(sys.argv[1], "r") as file:
    for line in file:
        assignmentsPair = line.strip().split(",")
        a= [{i for i in range(100) if (i>=int((assignmentsPair[j].split("-"))[0]) and i<=int((assignmentsPair[j].split("-"))[1]))} for j in range(len(assignmentsPair))]
        if a[0].issubset(a[1]) or a[1].issubset(a[0]):
            nAssignmentsFullyContained+=1
        if len(a[0].intersection(a[1]))!=0:
            nAssignmentsOverlapping+=1

print(nAssignmentsOverlapping)

       


