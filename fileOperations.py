handle = open('Softwares.txt')

count = 0
for line in handle:
    spos = line.find(" ")
    print(line [:spos])
    count=count+1

print(count)