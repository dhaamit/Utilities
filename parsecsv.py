fh = open('Aug13_Aug14.csv')

counts = dict()

for line in fh:
    lst = line.split(',')
    if len(lst) < 3:
        continue
    print(lst)