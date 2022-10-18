# Enter your code here. Read input from STDIN. Print output to STDOUT
# import package Namedtuple from the collections Library

from collections import namedtuple
n = int(input())
data = namedtuple("data",input())
marks_lst = [] # Create a empty list
for i in range(n):
    marks = int(data(*input().split()).MARKS)  # we are spliting the data
    marks_lst.append(marks)  # here are appending the marks to the new variable marks_lst
print(sum(marks_lst)/n)

#Testcase : 1
# Input : 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6

# output: 78.0

# Test case 2 :
# Input : 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5

# output : 81.0