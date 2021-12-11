def get_input():
    """
    :input: data_stream_from_task
    :return: numpy array
    """
    with open('../data/luke10.txt') as f:
        list = []
        for line in f.read().splitlines():
            list.append([i for i in line])
    return np.array(list)



def main():
if __name__ == "__main__":
    main()