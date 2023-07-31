from os import *
from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    # Write your code here.
    first_row = 0
    first_col = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i!=0 and j != 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                if i == 0:
                    first_row = 1
                if j == 0:
                    first_col = 1

    for i in range(1,n):
        if matrix[i][0] == 0:
            matrix[i] = [0]*m     

    for i in range(1,m):
        if matrix[0][i] == 0:
            for j in range(n):
                matrix[j][i] = 0
    
    if first_row:
        for j in range(m):
            matrix[0][j] = 0
        
    if first_col:
        for i in range(n):
            matrix[i][0] = 0
    
    
    return matrix


    
