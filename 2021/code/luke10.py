import os

def get_input():
    """
    :input: data_stream_from_task
    :return: numpy array
    """
    with open('../data/luke10.txt') as f:
        results = [line.strip() for line in f]
    return results

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])
def isincomplete(list_of_chunks):
    total_sum=0
    search_list=['()','[]','{}','<>']
    search_list2=[')',']','}','>']
    search_list3=['(','[','{','<']
    incomplete_list=[]
    incomplete_list2=[]
    prev_char='0'
    telleantall=0
    for i in list_of_chunks:
        telleantall+=1
        condition=True
        while condition:
            inc=0
            for closed in search_list:
                if (closed in i):
                    i=i.replace(closed,'')
                    condition=True
                    inc+=1

            if(inc==0):
                condition=False
            else:
                condition=True
        for char in i:
            if (char in search_list2): #if its a rightclosed

                if char==search_list2[0]:
                    print('found',char,'expected: ',search_list2[0],'added 3')
                    prev_char=char
                    incomplete_list.append(i)
                    total_sum+=3
                    break
                elif char==search_list2[1]:
                    print('found',char,'expected: ',search_list2[1],'added 57')
                    prev_char=char
                    incomplete_list.append(i)
                    total_sum+=57
                    break
                elif char==search_list2[2]:
                    print('found',char,'expected: ',search_list2[2],'added 1197')
                    prev_char=char
                    incomplete_list.append(i)
                    total_sum+=1197
                    break
                elif char==search_list2[3]:
                    print('found',char,'expected: ',search_list2[3],'added 25137')
                    prev_char=char
                    incomplete_list.append(i)
                    total_sum+=25137
                    break
                else:
                    print('ERROR')



            prev_char=char
        incomplete_list2.append(i)
    return incomplete_list2,total_sum






    return new_list


def calc_new_score(incomplete_list):
    list_of_sums=[]
    search_list3=['(','[','{','<']
    sum=0
    for i in incomplete_list:
        flipped = i[::-1]
        sum=0
        for i in flipped:

            sum=sum*5
            if i==search_list3[0]:
                sum+=1
            elif i==search_list3[1]:
                sum+=2
            elif i==search_list3[2]:
                sum+=3
            elif i==search_list3[3]:
                sum+=4

        list_of_sums.append(sum)
    return list_of_sums

def main():
    list_of_cunks=get_input()
    incomplete_list,total_sum=isincomplete(list_of_cunks)
    print(incomplete_list)
    search_list2=[')',']','}','>']
    new_list=[]
    for i in incomplete_list:
        condition2=False
        for j in i:
            for k in search_list2:
                if(j==k):
                    condition2=True


        if (condition2==True):
            incomplete_list.remove(i)
        else:
            new_list.append(i)
    print('total_sum: ', total_sum)

    print('new_list: ', new_list)
    #part2:
    total_score_list=calc_new_score(new_list)

    total_score_list=sorted(total_score_list)
    print(total_score_list)
    print(len(total_score_list))
    mid=findMiddle(total_score_list)
    print(mid)
if __name__ == "__main__":
    main()