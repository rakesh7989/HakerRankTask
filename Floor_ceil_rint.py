#### Floor-Ceil-rint

import numpy

numpy.set_printoptions(legacy='1.13')
A = numpy.array(input().split(),float)
print(numpy.floor(A),numpy.ceil(A),numpy.rint(A),sep='\n')

#Testcase:
# Input : 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

# Output: [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
#         [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
#         [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
