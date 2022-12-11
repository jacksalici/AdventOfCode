from pprint import pprint
import sys
import re

regex = r"Monkey (\d+):(?:\s+)Starting items: (.+)(?:\s+)Operation: new = old (.) (\d+|\D+)(?:\s+)Test: divisible by (\d+)(?:\s+)If true: throw to monkey (\d+)(?:\s+)If false: throw to monkey (\d+)(?:\s+)"
monkeys = []
round = 0




with open(sys.argv[1]) as file:
    matches = re.finditer(regex, file.read(), re.MULTILINE)

    for match in matches:
        dict = {
            'monkey': match.groups()[0],
            'items': match.groups()[1].split(', '),
            'operation': match.groups()[2],
            'operator': match.groups()[3],
            'test': match.groups()[4],
            'true': match.groups()[5],
            'false': match.groups()[6],
            'counter': 0
        }
        monkeys.append(dict)
    
    prodDiv = 1
    for m in monkeys:
        prodDiv *= int(m["test"])
    
    for round in range(10000):
        for m in monkeys:
            for i in m["items"][:]:
                n = 0

                if m["operation"] == "*":
                    n = int(i) * int(m["operator"] if m["operator"] !='old\n ' else i)
                elif m["operation"] == "+":
                    n = int(i) + int(m["operator"] if m["operator"] !='old\n ' else i)
                
                #n = int(float(n)/3)
                n =  int(n)%prodDiv

                if (n%int(m["test"])==0):
                    monkeys[int(m["true"])]["items"].append(str(n))
                else:
                    monkeys[int(m["false"])]["items"].append(str(n))
                
                m["counter"]+=1

                m["items"].remove(i)
        print(round)

    pprint ([m["counter"] for m in monkeys])


