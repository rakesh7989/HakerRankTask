########### Max-Min

import numpy

n,m=map(int,input().split())

lst=[list(map(int,input().split())) for i in range(n)]

ar=numpy.array(lst)

print(max(numpy.min(ar,axis=1)))


#Testcase:

# Input :  4 2
#          2 5
#          3 7
#          1 3
#          4 0


# Output : 3

