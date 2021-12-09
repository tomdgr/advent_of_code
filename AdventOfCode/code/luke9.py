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

def search(i,j,COUNT,heatmap,Searched):
    a=0
    if (heatmap[i][j]==9 or Searched[i][j]==-1):
        a=1

    else:
        COUNT+=1
        Searched[i][j]=-1
        search(i,j,COUNT,heatmap,Searched)




def calc_areas(heatmap):
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

    list_of_Areas=[]
    Searched=np.zeros((101,101))
    for i in range(1,len(heatmap)-1):
        for j in range(1,len(heatmap[0])-1):
            COUNT=0

            search(i,j,COUNT,heatmap,Searched)
        list_of_Areas.append(COUNT)
    return list_of_Areas

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
    numpyinput=get_input()
    numpyinput=add_border(numpyinput)
    print(numpyinput)
    print(len(numpyinput),len(numpyinput[0]))
    total_risk=findmin(numpyinput)
    print(total_risk)

    #Task2:
    numpyinput=get_input()
    numpyinput=add_border(numpyinput)
    list_of_areas=calc_areas(numpyinput)
    Nmaxelements(list_of_areas,3)
if __name__ == "__main__":
    main()

