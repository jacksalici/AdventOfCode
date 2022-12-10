import sys

nAssignmentsFullyContained = 0
with open("./2022/day04/input.txt", "r") as file:
    for line in file:
        assignmentsPair = line.strip().split(",")
        a= [{i for i in range(100) if (i>=int((assignmentsPair[j].split("-"))[0]) and i<=int((assignmentsPair[j].split("-"))[1]))} for j in range(len(assignmentsPair))]
        if a[0].issubset(a[1]) or a[1].issubset(a[0]):
            nAssignmentsFullyContained+=1

print(nAssignmentsFullyContained)

       


