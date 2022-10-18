##### Merge Tools



def merge_the_tools(string, k):
    l=[]
    m=0
    for i in range(len(string)//k):
        l.append(string[m:m+k])
        m+=k
    for v in l:
        print(''.join(list(dict.fromkeys(list(v)).keys())))

string,k = input(),int(input())
merge_the_tools(string,k)


#Testcase :
# Input : AABCAAADA
#         3


# output: AB
#         CA
#         AD
#


