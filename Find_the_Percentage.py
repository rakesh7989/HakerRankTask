if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # query_name is the Key
    # student_Marks is the dict
    # query_name it will return the corresponding  values which is stored in variable Marks
    Marks = student_marks[query_name]

    # To print the 2 decimal place use format function

    # Format(value,'.nf')

    print(format(sum(Marks) / 3, '.2f'))

#Testcase:
# Input :
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Output : 56.00