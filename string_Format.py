####### String Format

n = int(input())
w = len(bin(n)[2:1])
for i in range(1,n + 1):
    print(str(i).rjust(w," "), end=" ")
    print(str(oct(i)[2:]).rjust(w," "),end=" ")
    print(str(hex(i)[2:].upper()).rjust(w," "),end=" ")
    print(str(bin(i)[2:]).rjust(w," "))



# Testcase :
# Input : 17


# Output:
#      1 1 1 1
#      2 2 2 10
#      3 3 3 11
#      4 4 4 100
#      5 5 5 101
#      6 6 6 110
#      7 7 7 111
#      8 10 8 1000
#      9 11 9 1001
#      10 12 A 1010
#      11 13 B 1011
#      12 14 C 1100
#      13 15 D 1101
#      14 16 E 1110
#      15 17 F 1111
#      16 20 10 10000
#      17 21 11 10001


