n = int(input())

pb = {}

for i in range(n):
    entry = str(input())
    pb[entry.split()[0]] = entry.split()[1]

while True:
    try:
        entry = str(input())
        if entry in pb.keys():
            print(entry + "=" + pb[entry])
        else:
            print("Not found")
            
    except EOFError:
        break
