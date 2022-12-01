import numpy as np
COUNT=0
def get_input():
    """
    :input: data_stream_from_task
    :return: numpy array
    """
    with open('../data/luke9.txt') as f:
        heightmap = []
        for line in f.read().splitlines():
            heightmap.append([int(i) for i in line])
    return np.array(heightmap)

def add_border(numpy_array):
    array = np.pad(numpy_array, pad_width=1, mode='constant', constant_values=9)
    return array

def findmin(heightmap):
    total_risk_level=0
    for i in range(1,len(heightmap)-1):

        for j in range(1,len(heightmap[0])-1):
            condition =((heightmap[i][j]<heightmap[i+1][j]) and (heightmap[i][j]<heightmap[i-1][j]) and (heightmap[i][j]<heightmap[i][j+1]) and (heightmap[i][j]<heightmap[i][j-1]))
            print(condition)
            if(condition):
                total_risk_level+=(heightmap[i][j]+1)


    return total_risk_level

def search(i,j,COUNT,heatmap,searched):

    if (heatmap[i][j]==9 or searched[i][j]==-1):
        #do nothing
        COUNT+=0
        searched[i][j]=-1
        print('did nothing count is now:',COUNT)
        return COUNT
    else:
        #Count the first
        COUNT+=1
        #Set it as counted
        searched[i][j]=-1
        if(i<=99 and (i>=0) and (j>=0) and(j<=99)):
            if((searched[i+1][j]!=-1) and (heatmap[i+1][j]!=9) ):

                COUNT=search(i+1,j,COUNT,heatmap,searched)
            if((searched[i-1][j]!=-1) and (heatmap[i-1][j]!=9)):

                COUNT=search(i-1,j,COUNT,heatmap,searched)
            if((searched[i][j+1]!=-1) and (heatmap[i][j+1]!=9)):

                COUNT=search(i,j+1,COUNT,heatmap,searched)
            if((searched[i][j-1]!=-1) and (heatmap[i+1][j]!=9)):

                COUNT=search(i,j-1,COUNT,heatmap,searched)

        return COUNT

    #check neighboor squares:




searched=np.zeros((101,101))

def calc_areas(heatmap,searched):
    """
    Search: 1. FOR all entries: is the entry searched?
                    if not add to searched.
                    Find number of adjacent non walls(9's),
                    are this already searched?
                    if not: add number of adjacent non walls to area.
                    recursivly call function in searchable directions

               add new entry to SEARCHED list,

    :return: list of areas found in search algo
    """

    list_of_areas=[]

    for i in range(1,len(heatmap)-1):
        for j in range(1,len(heatmap[0])-1):
            print('i,j: ',i,j)
            COUNT=0
            # check neighboor heights:
            if(searched[i][j]!=-1 or heatmap[i][j]==9):
                COUNT = search(i,j,COUNT,heatmap,searched)
                list_of_areas.append(COUNT)

    return list_of_areas


def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    print(final_list)

def main():
    COUNT=0
    #Task1
    #numpyinput=get_input()
    #numpyinput=add_border(numpyinput)
    #print(numpyinput)
    #print(len(numpyinput),len(numpyinput[0]))
    #total_risk=findmin(numpyinput)
    #print(total_risk)

    #Task2:
    numpyinput=get_input()
    numpyinput=add_border(numpyinput)
    list_of_areas=calc_areas(numpyinput,searched)
    Nmaxelements(list_of_areas,3)
if __name__ == "__main__":
    main()

