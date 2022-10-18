# Find  the second Maximum Number in the list

mylist = [2,3,6,6,5]
# here we have duplicates so. with the help of set we eliminate duplicates in the list
mylist = sorted(set(mylist))
#sorted function help us to to arange the list of number in a Assending order
print(mylist)

print("second Maximum Number",mylist[-2])
#print("Fist Maximum",mylist[-1])

# Testcase :
#[2, 3, 5, 6]
#second Maximum Number 5