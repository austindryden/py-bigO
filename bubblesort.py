import math

listy = [2, 5, 76, -4, 200, 0, 9, 2, -3, 5]


def bubbleSort(list):
    swap = False
    for n in range(len(list)-1):
        if (list[n]>list[n+1]):
            store = list[n+1]
            list[n+1]=list[n]
            list[n]=store
            swap = True
        
    if swap:
        return(bubbleSort(list))
    return list


def targetNum(list, num):
    
    if len(list) <= 1:
        return("NOPE!!")

    if(list[0] + list[-1] == num):
        return([list[0],list[-1]])
    
    if (list[0] + list[-1] > num):
        return targetNum(list[:len(list) - 1], num)
    
    if (list[0] + list[-1] < num):
        return targetNum(list[1:], num)
    
        
print(targetNum([0,1,5,8,11], 9))