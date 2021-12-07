import numpy as np
with open('../luke4.txt', 'r') as f:
    bingomatrix = [line.strip() for line in f]

bingo_input= [69,88,67,56,53,97,46,29,37,51,3,93,92,78,41,22,45,66,13,82,2,7,52,40,18,70,32,95,89,64,84,68,83,26,43,0,61,36,57,34,80,39,6,63,72,98,21,54,23,28,65,16,76,11,20,33,96,4,10,25,30,19,90,24,55,91,15,8,71,99,58,14,60,48,44,17,47,85,74,87,86,27,42,38,81,79,94,73,12,5,77,35,9,62,50,31,49,59,75,1]

bingolist= np.zeros((5,5))
bingolist_counter = 0
isfirst=True
testlist=[]
for i in bingomatrix:

    if (i != ' -> '):
        a_list = i.split()                      #split list
        map_object = map(int, a_list)           #make map object
        list_of_integers = list(map_object)     #make list
        #Make numpy array:

        bingolist[bingolist_counter]=list_of_integers

        bingolist_counter+=1
    else:
        if(isfirst==True):
            isfirst=False
            final_list=bingolist
        else:
            final_list=np.concatenate((final_list,bingolist),axis=0)
        bingolist = np.zeros((5,5))
        bingolist_counter=0
        testlist.append(bingolist)

##---------------------------BINGO functions:------------------
testlist2=testlist
def setnumber(number,testlist):
    for i in range(len(testlist)):
        testlist[i] = np.where(testlist[i] == number, -1, testlist[i])
    return testlist


def checkbingo(testlist):
    counter=0

    for i in testlist:
        sum_rows=i.sum(axis=1)
        sum_columns=i.sum(axis=0)
        counter_row=0
        coutner_column=0
        for i in sum_rows:
            if(i == -5):

               return counter,counter_row,'row'
            counter_row+=1
        for i in sum_columns:
            if(i == -5):
                return counter,coutner_column,'column'
            coutner_column+=1
        counter+=1
    return -1,-1,''

def checknotbingo(testlist):
    counter=0
    value=False

    for i in testlist:
        col_list=[3.0,2.0,3.0,5.0,2.0]
        row_list=[3.0,2.0,3.0,5.0,2.0]
        sum_rows=i.sum(axis=1)
        sum_columns=i.sum(axis=0)
        counter_row=0
        coutner_column=0
        for j in sum_rows:
            if(j != -5):
                row_list[counter_row]=1.0
            counter_row+=1
        for k in sum_columns:
            if(k != -5):
                col_list[coutner_column]=1.0
            coutner_column+=1


        sum1=sum(row_list)
        sum2=sum(col_list)
        if (sum1==5.0 and sum2==5.0):
            value=True
        counter+=1
    return value,counter





teller=0
for i in bingo_input:
    testlist=setnumber(i,testlist)

    a,b,c=checkbingo(testlist)

    print(teller)
    if(c=='row'):
        print(testlist[a])
        print(i)
        break
    elif(c=='column'):
        print(testlist[a])
        print(i)
        break
    teller+=1

num=82
for i in range(num):
    number=bingo_input[i]
    testlist=setnumber(number,testlist)

counter=0
for i in testlist:
    value=False
    sum1=0
    sum2=0
    col_list=[-200.123,-200.123,-200.123,-100.123,-1.12]
    row_list=[-200.123,-200.123,-200.123,-100.123,-1.12]
    sum_rows=i.sum(axis=1)
    sum_columns=i.sum(axis=0)
    counter_row=0
    coutner_column=0
    #HVIS èn rad/kolonne mangler ett tall for å bli utfyllt:
    # sett den til sann

    for j in sum_rows:
        if(j != -5.0):
            row_list[counter_row]=1.0
        counter_row+=1
    for k in sum_columns:
        if(k != -5.0):
            col_list[coutner_column]=1.0
        coutner_column+=1
    counter+=1
    #Hvis alle rader og alle kolonner mangler ett tall
    sum1=sum(row_list)
    sum2=sum(col_list)
    if (sum1==5.0 and sum2==5.0):
        value=True
        print(testlist[counter-1])

    value=False
print(bingo_input[num])

