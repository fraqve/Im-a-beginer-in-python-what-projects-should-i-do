import random

max = 5

def GenerateList(max:int):
    l = []
    for i in range(max+1):
        l.append(random.randint(0 , 10))
    return l
        

list = GenerateList(max)

print(list)




def SelectSort(list):
    for unsorted_index in range(0 , len(list)):
        min = list[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index,len(list)):
            if list[i] < min:
                min = list[i]
                min_index = i
                list[min_index] = list[unsorted_index]
                list[unsorted_index] = min
                

            

SelectSort(list)

print(list)