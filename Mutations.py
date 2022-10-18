###### Mutations
# Here we are trying to Replace the 6th char 'a' to 'k
s = "abracadabra"
position = 5
new_character = 'k'

s = s[:position] + new_character + s[position+1:]
print(s)


# Test case :
# Input : abracadabra
# Output: abrackdabra