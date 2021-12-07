import numpy as np
import re
import time

def get_input():
    """
    :input: data_stream_from_task
    :return: numpy array
    """
    with open('../data/luke6.txt', 'r') as f:
        ventmatrix = [line.strip() for line in f]

    for i in ventmatrix:
        ventmatrix=re.split(',',i)

    map_object = map(int, ventmatrix)
    list_of_integers = list(map_object)
    numpy_array=np.array(list_of_integers)
    return numpy_array

def test():
    f = open('../data/luke6.txt')
    F = [int(x) for x in f.readlines()[0].split(',')]
    agegroup = [0]*9 ## 0-8 days old
    for f in F:
        agegroup[f] += 1
    print('agegroup: ', agegroup)
    for d in range(256):
        print(agegroup)

        print('add the value in agegroup[',d%9,']','which is: ',agegroup[d%9], 'to agegroup[',(d+7)%9,']','Which was',agegroup[(d+7)%9],'for a total sum of: ',agegroup[(d+7)%9]+agegroup[d%9],'at day number: ',d)
        agegroup[(d+7)%9] += agegroup[d%9]
    print(sum(agegroup))

def model_fish(numpy_array,x):
    """
    :input: numpy array of input, days to simulate
    :return: number of fish at day x
    """

    for i in range(x):
        number_of_new_elements=len(numpy_array[numpy_array==0])
        if(number_of_new_elements>0):
            apppendable_array=np.ones(number_of_new_elements)*8
            numpy_array=np.concatenate((numpy_array, apppendable_array))

        #decrement all and add new

        numpy_array[numpy_array == -1] = 6
        print(numpy_array)
        numpy_array-=1

    return len(numpy_array),number_of_new_elements
#find all values that are zero.
def rec(numpy_array,prev,counter,days_to_simulate):
    #If limit is reached quit:
    length=len(numpy_array)
    if(counter>=days_to_simulate):

        print(length)
        return(length)

    else:
        print(length)
        #if element is -1 set it to 6
        t_0=time.time()
        numpy_array[numpy_array == -1] = 6
        t_1=time.time()
        print(numpy_array)
        numpy_array-=1
        t_2=time.time()
        counter+=1
        print(counter)

        if(prev>0):
            apppendable_array=np.ones(prev)*8
            numpy_array=np.concatenate((numpy_array, apppendable_array))
        prev=len(numpy_array[numpy_array==0])
        t_3=time.time()
        print('t_1-t_0 :',t_1-t_0,'t2-t_1: ',t_2-t_1,'t_3-t_2: ', t_3-t_2)
        return rec(numpy_array,prev,counter,days_to_simulate)



def main():
    test()



if __name__ == "__main__":
    main()