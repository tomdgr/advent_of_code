import numpy as np
def get_input():
    """
    :input: data_stream_from_task
    :return: numpy array
    """
    itxt = open("../data/luke7.txt", mode='r').read().strip().splitlines()
    itxt = list(map(int, itxt[0].split(',')))
    array=np.array(itxt)
    return array



def preproceccing_input_data(text_input):
    max=np.amax(text_input)
    min=np.amin(text_input)

    return max, min

def nth_triangular_number(n):


    return int(n*(n+1)/2)

def optimize(max,min,vertical_pos_list):
    min_fuel=1000000000000000

    #complexity 0(n^2) solution:
    for i in range(max-min+1):
        fuel=0
        for j in vertical_pos_list:
            #
            fuel+=nth_triangular_number(abs(j-i))
        print(fuel)
        if(fuel<min_fuel):
            min_fuel=fuel
    return min_fuel


def main():
    vertical_pos_list=array=get_input()
    max, min = preproceccing_input_data(vertical_pos_list)
    min_fuel=optimize(max,min,vertical_pos_list)
    print('minimum calculated fuel is: ', min_fuel)
if __name__ == "__main__":
    main()