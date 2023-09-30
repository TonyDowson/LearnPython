file = open('LGEN.L.csv','r')
print(file.readline())

myDict = {}

for line in file:
    record = line.split(',')
    myDict[record[0]] = float(record[5])
    
print(myDict)
