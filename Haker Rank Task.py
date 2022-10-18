
#############   Hacker Rank  Task ###############

# Find  the second Maximum Number in the list

mylist = [2,3,6,6,5]
# here we have duplicates so. with the help of set we eliminate duplicates in the list
mylist = sorted(set(mylist))
#sorted function help us to to arange the list of number in a Assending order
print(mylist)

print("second Maximum Number",mylist[-2])
#print("Fist Maximum",mylist[-1])

####################################################

###### Mutations
# Here we are trying to Replace the 6th char 'a' to 'k
s = "abracadabra"
position = 5
new_character = 'k'

s = s[:position] + new_character + s[position+1:]
print(s)



####  Time_Delta
# sun 10 May 2015 13:54:36 -700
from datetime import datetime


def time_delta(t1, t2):
  time_format = "%a %d %b %Y %H %M : %s %Z"
  time1 = datetime.strptime(t1, time_format)
  time2 = datetime.strptime(t2, time_format)
  return int(abs(time1 - time2).total_seconds())


for i in range(int(input())):
  t1 = input()
  t2 = input()
  print(time_delta(t1, t2))

