x,y=int(input().split())
infos = []
forbids = []

for i in range(x+1):
    info = list[input().split()]
    infos.append(info)

for i in range(y+1):
    forbid = list[input().split()]
    forbids.append(forbid)

for i in range(x+1):
    if infos[i][0] in forbids:
        forbid_package = forbids.index()
        #print(forbid_package)
        if infos[i][1] == forbid_package[0]:
            if infos[i][2] == forbid_package[1]:
                package = infos[i][0]
    else:
        print("none")

print(package)

