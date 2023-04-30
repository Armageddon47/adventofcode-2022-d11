import re
import copy
from decimal import Decimal, getcontext,ROUND_DOWN



getcontext().prec = 50  # set precision to 50 decimal places

files = []
monkeys = []
monkeyCount = -1
countRounds = 0
numberofmonkeys = 0
class Monkey():
    def __init__(self):
        self.items = []
        self.operation = 0
        self.divisible = 0
        self.a = 0
        self.b = 0
        self.inspected = 0

with open('input2.txt','r') as f:
    for l in f:
        
        files.append(l.strip())
        
for i in files:
    if i[0:6] == "Monkey":
        numberofmonkeys += 1
        
for i in range(numberofmonkeys):
    monkey = Monkey()
    monkeys.append(monkey)
    
for command in files:
    if command == '':
        continue
    if command[0] == "M":
        monkeyCount += 1
                
    elif command[0] == "S":

        numbers = re.findall(r'\d+', command)
        numbers = [int(num) for num in numbers]
        monkeys[monkeyCount].items = numbers

    elif command[0] == "O":
        monkeys[monkeyCount].operation = command[21:]
        monkeys[monkeyCount].operation = monkeys[monkeyCount].operation.replace(' ', '')

    elif command[0] == "T":
        numbers = re.findall(r'\d+', command)
        monkeys[monkeyCount].divisible = numbers
        
    elif command[3] == "t":
        numbers = re.findall(r'\d+', command)
        monkeys[monkeyCount].a = numbers
    elif command[3] == "f":
        numbers = re.findall(r'\d+', command)
        monkeys[monkeyCount].b = numbers
 
monkeys_copy = copy.deepcopy(monkeys)
monkeys_original = copy.deepcopy(monkeys)
       
while(countRounds < 20):
    f = 0
    while True:
        monkeys = copy.deepcopy(monkeys_copy)
        if f >= len(monkeys): break
        
        tem = monkeys[f]
        monkeys_copy[f].inspected += len(tem.items)
        while len(tem.items) > 0:
            d = tem.items[0]
            if tem.operation == '*old':
                compare = int((d * d) / 3)
            elif tem.operation == '+old':
                compare = int((d + d) / 3)
            else:
                compare = int(eval(f"{d}{tem.operation}"))   
                compare = int( compare / 3)
            if compare % int(tem.divisible[0]) == 0:
                monkeys_copy[int(tem.a[0])].items.append(compare)
                monkeys_copy[f].items.remove(d)
            else:
                monkeys_copy[int(tem.b[0])].items.append(compare)
                monkeys_copy[f].items.remove(d)
            tem.items.pop(0)
            
        f += 1

    countRounds += 1
totalInspected = []
for i in monkeys:
    totalInspected.append(i.inspected)
    
totalInspected.sort()
print(totalInspected)
print("answer to part 1 is : " , (totalInspected[-1] * totalInspected[-2]))

############# end fo part 1
## IMPORTANT NOTE,##
## Part two is gonna take a couple of minutes to calculate, 
## give it time after you start to run the code
monkeys_copy = copy.deepcopy(monkeys_original)
monkeys = copy.deepcopy(monkeys_original)
primes_sum = 1
for mk in monkeys_original:
    primes_sum *= int(mk.divisible[0])

countRounds = 0
while countRounds < 10000:
    f = 0
    while True:
        monkeys = copy.deepcopy(monkeys_copy)
        if f >= len(monkeys): break
        
        tem = monkeys[f]
        monkeys_copy[f].inspected += len(tem.items)
        while len(tem.items) > 0:
            d = tem.items[0]
            if tem.operation == '*old':
                compare = int((d * d) )
            elif tem.operation == '+old':
                compare = int((d + d) )
            else:
                compare = int(eval(f"{d}{tem.operation}"))   

            compare %= primes_sum
                
            if compare % int(tem.divisible[0]) == 0:
                monkeys_copy[int(tem.a[0])].items.append(compare)
                monkeys_copy[f].items.remove(d)
            else:
                monkeys_copy[int(tem.b[0])].items.append(compare)
                monkeys_copy[f].items.remove(d)
            tem.items.pop(0)
            
        f += 1
    if countRounds % 1000 == 0:
        pass
    countRounds += 1
        
print ( countRounds)


totalInspected = []
for i in monkeys:
    totalInspected.append(i.inspected)
    
totalInspected.sort()

output = Decimal((totalInspected[-1] * totalInspected[-2]))
print("answer to part 2 is : " , output)