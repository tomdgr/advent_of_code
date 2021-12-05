with open('luke3.txt', 'r') as f:
    luke3_in = [line.strip() for line in f]
def find_target(col_num, target_liste):
    sum=0
    for i in target_liste:
        sum+=int(i[col_num])
    if(sum >= (len(target_liste)/2)):
        return 1
    else:
        return 0
def remove_entries(target, col_num,list):
    tom_liste=[]
    for i in list:
        print('int i target num:', int(i[col_num]), target)
        if(int(i[col_num])==target):
            tom_liste.append(i)
        else:
            a=1
    return tom_liste
list=luke3_in
for i in range(12):
    target=find_target(i,list)
    list= remove_entries(target,i,list)
    print(list)
