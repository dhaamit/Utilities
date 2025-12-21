name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hoursCount = dict()
for line in handle:
    lst = line.split()
    if not (line.startswith('From') and len(lst) > 4):
        continue
    hour = lst[5].split(':')[0]
    hoursCount[hour] = hoursCount.get(hour,0) + 1

# newList = list()
# for key, value in hoursCount.items():
#     newList.append((key, value))

# for item in sorted(newList):
#     print (item[0], item[1])

for x, y in sorted(hoursCount.items()):
    print (x,y)

