def singleNonDuplicate(arr):
    # Write your code here
    low = 0
    high = len(arr) - 1
    while(low < high):
        mid = (low + high)//2
        if mid!=0 and arr[mid-1] == arr[mid] and (mid - low)%2 == 1:
            low = mid + 1
        elif mid < len(arr) - 1 and arr[mid] == arr[mid+1] and (mid - low)%2 == 0:
            low = mid 
        else:
            high = mid
    return arr[low]
