#open file, name given as input. Parse through file, look for text X-DSPAM-Confidence:. 
# Get float value and calculate average of all occurances.

fh = input ("Enter file name: ")

try:
    fContent = open(fh)
except:
    print("File not found.")

count = 0
total = 0
for line in fContent:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    getPos = line.find(":")
    getVal = line[getPos+1:].strip()
    fVal = float(getVal)
    count = count + 1
    total = total + fVal

average = total / count
print ("Average spam confidence:", average)