from datetime import datetime

id_team = str(input(""))
n = int(input(""))

for i in range(n):
    prompt = str(input(""))
    data = prompt.split(",")

    if (len(data) != 6):
        print("NO")
        continue

    skip = False
    for d in data:
        if (d.strip() == ""):
            skip = True
            break
    if (skip):
        print("NO")
        continue

    if (data[-1][-1] != ';'):
        print("NO")
        continue

    if (data[0] != id_team):
        print("NO")
        continue
    
    try:
        datetime.strptime(data[1], "%H:%M:%S")
    except:
        print("NO")
        continue

    print("YES")