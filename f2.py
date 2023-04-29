import re
import copy

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

with open('input.txt','r') as f:
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
       
while(countRounds < 20):
    count = 0
    for monk in monkeys:
        monkeys_copy[count].inspected += len(monk.items) 
        for i in monk.items:
            if monk.operation == '*old':
                monk.operation = '*' + str(i)
                
            elif monk.operation =='+old':
                monk.operation = '+' + str(i)
            temp = int(eval(f"{i}{monk.operation}"))
            temp = int(temp / 3)
            if temp % int(monk.divisible[0]) == 0:
                monkeys_copy[int(monk.a[0])].items.append(temp)
                monkeys_copy[count].items.remove(i)
            else:
                monkeys_copy[int(monk.b[0])].items.append(temp)
                monkeys_copy[count].items.remove(i)
           
        count += 1
    monkeys = copy.deepcopy(monkeys_copy)
    countRounds += 1
totalInspected = []
for i in monkeys_copy:

    totalInspected.append(i.inspected)
    
totalInspected.sort()
print(totalInspected)
print("answer to part 1 is : " , (totalInspected[-1] * totalInspected[-2]))