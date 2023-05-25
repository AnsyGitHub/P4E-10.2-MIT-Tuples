name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
data = dict()
for line in handle:
    if line.startswith("From "):
        first = line.split()
        second = first[5]
        second = second.split(":")
        hour = second[0]
        data[hour] = data.get(hour,0) + 1
        
li = list()        
for k,v in data.items():
    new = (k,v)
    li.append(new)
    
li = sorted(li)
for k,v in li:
    print(k,v)