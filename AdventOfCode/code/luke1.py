with open('../test.txt', 'r') as f:
    results = [line.strip() for line in f]
results = list(map(int, results))
decreased=0
increased=0
for i in range(len(results)-3):
    sum1 = results[i] + results[i+1] + results[i+2]
    sum2 = results[i+1] + results[i+2] + results[i+3]
    if((sum1-sum2)>0):
        decreased+=1
    elif((sum1-sum2)==0):
        decreased+=0
        increased+=0
    else:
        increased+=1
print(increased,decreased)