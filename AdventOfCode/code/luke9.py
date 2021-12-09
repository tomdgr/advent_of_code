import numpy as np
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


def main():
    numpyinput=get_input()
    numpyinput=add_border(numpyinput)
    print(numpyinput)
    print(len(numpyinput),len(numpyinput[0]))
    total_risk=findmin(numpyinput)
    print(total_risk)
if __name__ == "__main__":
    main()

