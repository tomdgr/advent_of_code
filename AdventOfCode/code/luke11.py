"""
Luke 11: Dumbo Octopus Dynamics
"""
import numpy as np

def get_input():
    """
    :input: data_stream_from_task
    :return: numpy array
    """
    with open('../data/luke11.txt') as f:
        heightmap = []
        for line in f.read().splitlines():
            heightmap.append([int(i) for i in line])
    return np.array(heightmap)

def flash(octopus_map,flashed_map,d,x,y, NUM_FLASHED):
    """

    :param d:
    :param octopus_map:
    :param x:
    :param y:
    :return:
    """
    flashed_map[x][y]=1
    NUM_FLASHED+=1
    # increment adjecent Dumbo octopus energy levels:
    for dx,dy in d:
        octopus_map[x+dx][y+dy]+=1
    # search the adjacent Dumbo octopus for new energy bursts
    for dx,dy in d:
        if((octopus_map[x+dx][y+dy]>9) and (flashed_map[x+dx][y+dy] !=1) ):
            NUM_FLASHED,flashed_map=flash(octopus_map,flashed_map,d,x+dx,y+dy,NUM_FLASHED)
        else:
            NUM_FLASHED=NUM_FLASHED+0


    return NUM_FLASHED,flashed_map


def add_border(numpy_array,constant_value):
    array = np.pad(numpy_array, pad_width=1, mode='constant', constant_values=constant_value)
    return array


def model_energy_levels(octopus_map):
    """

    :param octopus_map:
    :return:
    """
    NUM_FLASHED = 0
    d = ((0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1) )
    rows,cols = len(octopus_map), len(octopus_map[0])
    SIMULATE_STEPS = 100
    flashed_map= np.zeros((rows,cols),dtype=int)
    # add borders to avoid index errors:
    octopus_map = add_border(octopus_map,-1000)
    flashed_map = add_border(flashed_map,1)
    rows,cols = len(octopus_map), len(octopus_map[0])
    for step in range(SIMULATE_STEPS):
        # Increment energy_levels
        octopus_map+=1

        # Flash dumbo Octopus with energy levels greater than 9
        for x in range(1, rows-1):
            for y in range(1,cols-1):
                if( (octopus_map[x][y]>9) and (flashed_map[x][y]!=1) ):
                    NUM_FLASHED,flashed_map = flash(octopus_map,flashed_map,d,x,y, NUM_FLASHED)
        # Set the bursted dumbo octopus to 0
        octopus_map[octopus_map > 9] = 0
        # set the flashed_map to 0 again
        flashed_map[flashed_map != 0] = 0
    return NUM_FLASHED



def main():
    octopus_map=get_input()
    NUM_FLASHED=model_energy_levels(octopus_map)
    print(NUM_FLASHED)
if __name__ == "__main__":
    main()