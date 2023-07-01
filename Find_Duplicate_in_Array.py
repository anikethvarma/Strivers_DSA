def findDuplicate(arr:list, n:int):
    low = 1
    high = n-1
    while(low < high):
        mid = (low + high)//2
        
        count = 0
        for i in range(n):
            if arr[i] <= mid:
                count += 1
        
        if count > mid:
            high = mid
        else:
            low = mid + 1
    
    return low
