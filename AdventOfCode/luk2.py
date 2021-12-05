
list=[]
with open('luke2.txt', 'r') as f:
    for lines in f:
        a = [s for s in lines.split() ]
        list = list+a



hor=0
dep=0
aim=0
for a in range(0, len(list), 2):
    print(list[a])
    if list[a]=='forward':
        hor+=int(list[a+1])
        dep+=aim*int(list[a+1])
    elif list[a]=='down':
        aim+=int(list[a+1])
    else:
        aim-=int(list[a+1])
result=dep*hor
print(result)
