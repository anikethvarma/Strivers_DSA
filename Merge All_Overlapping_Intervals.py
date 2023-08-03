from typing import *

def mergeOverlappingIntervals(arr : List[List[int]]) -> List[List[int]]:
    # Write your code here.
    arr.sort()
    temp = []
    for i in range(len(arr)):
        if i == 0:
            temp.append(arr[i])
        elif temp[-1][-1] >= arr[i][0]:
            temp[-1][-1] = max(temp[-1][-1],arr[i][1])
        else:
            temp.append(arr[i])
    return temp   
