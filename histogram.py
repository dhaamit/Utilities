txt = input ("Enter the text:")
counts = dict()

slist = txt.split()

for word in slist:
    counts[word] = counts.get(word,0)+1

bigWord = None
bigCount = None

for word,count in counts.items():
    if bigCount is None or bigCount < count:
        bigWord = word
        bigCount = count

print (bigWord)
print (bigCount)