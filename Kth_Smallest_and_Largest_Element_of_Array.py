def kthSmallLarge(arr, n, k):
    # Write your code here
    arr.sort()
    return [arr[k-1],arr[-k]]
