import sys


marker=[]
markerPos=0

with open(sys.argv[1], "r") as file:
    for myindex, mychar in enumerate(file.read()):
        while mychar in marker:
            marker.pop()
        
        marker.insert(0,mychar)
        if len(marker) == sys.argv[2]:
            markerPos = myindex +1
            break
        
            
print(markerPos)
