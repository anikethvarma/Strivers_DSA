def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    row_index = 0
    for i in range(len(mat)):
        if mat[i][-1] <= target:
            row_index = i
        
    low = 0
    high = len(mat[0]) - 1
    while(low<=high):
        mid = (low+high)//2
        if mat[row_index][mid] == target:
            return True
        elif mat[row_index][mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

         

