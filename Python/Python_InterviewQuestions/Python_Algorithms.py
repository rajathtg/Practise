Question1:
Sample Input:
a = 2
b = 3

Sample Output:
5

def solveMeFirst(a,b):
    res = a+b
    return res

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Question2:

Sample Input
6
1 2 3 4 10 11

Sample Output
31

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    result = sum(ar)
    return result
    # Write your code here

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip()) ##Strip removes unwanted spaces.
    print(ar_count)
    ar = list(map(int, input().rstrip().split())) ##Split is used split the data as per requirement.
    print(ar)
    result = simpleArraySum(ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Question3:

Sample Input:
17 28 30
99 16 8

Sample Output:
2 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice=0
    bob=0
    n = [0,1,2]
    for i in n:
      if a[i] > b[i]:
          alice+=1
      elif a[i] < b[i]:
          bob+=1
      else:
          alice+=0
          bob+=0
    return alice,bob

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Question4:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Sample Input:
3
11 2 4
4 5 6
10 8 -12

Sample Output:
15

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    d1=0
    d2=0
    for i in range(0, n):
        d1 = d1+arr[i][i]
        d2 = d2+arr[i][n-i-1]
    return abs(d1-d2)
    #print(abs(d1-d2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Question5:

