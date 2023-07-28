from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	# Write your code here.
	val1 = arr[0]
	val2 = arr[0]
	count1 = 0
	count2 = 0
	for i in range(n):
		if count1 == 0:
			val1 = arr[i]
			count1 = 1 
		elif count2 == 0:
			val2 = arr[i]
			count2 = 1
		if arr[i] == val1:
			count1 += 1 
		elif arr[i] == val2:
			count2 += 1
		else:
			count1 -= 1
			count2 -= 1
	if arr.count(val1) > floor(n/2):
		return val1 
	elif arr.count(val2) > floor(n/2):
		return val2
	else:
		return -1
