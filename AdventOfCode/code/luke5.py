import numpy as np
import re
with open('../luke5.txt', 'r') as f:
    ventmatrix = [line.strip() for line in f]


#make matrix 4xlen(inputlist)  [[x1,y1,x2,y2],[...]]
ventmatrixcounter=0
ventnumpy= np.zeros((len(ventmatrix),4))
for lines in ventmatrix:
    res=re.split(',| ', lines)
    #remove arrow
    for line in res:
        if (line=='->'):
            res.remove(line)
    #map to ints and append to numpy
    map_object = map(int, res)
    list_of_integers = list(map_object)
    ventnumpy[ventmatrixcounter]=list_of_integers
    ventmatrixcounter+=1


print(ventnumpy)
largest_value=np.amax(ventnumpy)
largest_value=int(largest_value)
print('largest value:',largest_value)
ventmap=np.zeros((largest_value+1,largest_value+1))
#-----------------Functions: -------------------------
def increment_ventmap(m, ventmap, isroworcolumn):
    #print('x_0',m[0], 'y_0',m[1],'x_2',m[2],'y_2',m[3])
    #print(m[0]-m[2],': isdiffx')
    #print(m[1]-m[3],': isdiffy')
    if (isroworcolumn=='row'):
        diff=abs(m[1]-m[3])+1
        if m[1]>m[3]:
            y_0=m[3]
            y_0=int(y_0)
        else:
            y_0=m[1]
            y_0=int(y_0)
        for i in range(int(diff)):
            ventmap[int(m[0]),y_0+i]+=1

    elif(isroworcolumn=='col'):
        diff=abs(m[0]-m[2])+1
        if m[0]>m[2]:
            x_0=m[2]
            x_0=int(x_0)
        else:
            x_0=m[0]
            x_0=int(x_0)
        for i in range(int(diff)):
            ventmap[x_0+i,int(m[1])]+=1
    elif(isroworcolumn=='diag'):

        diff=abs(m[1]-m[3])+1
        if ((m[1]<m[3]) and (m[0]<m[2]) ):
            x_0=int(m[0])
            y_0=int(m[1])
            for i in range(int(diff)):
                ventmap[x_0+i,y_0+i]+=1
        elif ((m[1]<m[3]) and (m[0]>m[2])):
            x_0=int(m[0])
            y_0=int(m[1])
            for i in range(int(diff)):
                ventmap[x_0-i,y_0+i]+=1

        elif ((m[1]>m[3]) and (m[0]<m[2])):
            x_0=int(m[0])
            y_0=int(m[1])
            for i in range(int(diff)):
                ventmap[x_0+i,y_0-i]+=1

        else:
            x_0=int(m[0])
            y_0=int(m[1])
            for i in range(int(diff)):
                ventmap[x_0-i,y_0-i]+=1
        #print('for x_0',m[0], 'y_0',m[1],'x_2',m[2],'y_2',m[3])
        #print(x_0+i,y_0+i)
    else:
        print('WTF IS GOING ON?')

    return ventmap

def isverticalorhorizontal(ventnumpy, ventmap):
    dummy=0
    for m in ventnumpy:
        if((m[0]==m[2])):#x1==x2
            isroworcolumn='row'
            ventmap=increment_ventmap(m, ventmap, isroworcolumn)
        elif(m[1]==m[3]): # || y1==y2
            isroworcolumn='col'
            ventmap=increment_ventmap(m, ventmap, isroworcolumn)
        elif(abs((m[1]-m[3]))==abs((m[0]-m[2]))):
            isroworcolumn='diag'
            ventmap=increment_ventmap(m,ventmap,isroworcolumn)
            #do nothing
        else:
            print('WTF IS GOING ON?')
    print('largest sum: ',np.amax(ventmap))
    p31 = np.asarray(ventmap)
    za = (p31 >= 2).sum()
    print('sum larger than 2:',za)

#-----PSEUDOCODE:
#for a line:
# check if isverticalishorisontal: returns True,'row'||'column' /False,'False'

#increment ventmap: takes in map(nparray) (x,y). and increments all places a lines hits
#find how many places in map >2 returns number





isverticalorhorizontal(ventnumpy,ventmap)