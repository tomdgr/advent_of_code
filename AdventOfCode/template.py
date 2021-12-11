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


struct = {
')': 3,
']': 57,
'}': 1197,
'>': 25137
}

def isincomplete(list_of_chunks):
    for chunk in range(len(list_of_chunks):
        for char in range(len(chunk)):
            if
    return

def main():
    print(get_input())
    list_of_cunks=get_input()
if __name__ == "__main__":
    main()