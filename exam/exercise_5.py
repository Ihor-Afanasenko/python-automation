"""
Read From File Exercise 5 in HillelExam.docx
"""

with open('test.txt', 'r') as file:
    contents = file.readlines()

result = []
for line in contents:
    result.extend(line.split('/')[1:-1])

count_dict = {}
for element in set(result):
    count_dict.setdefault(element, result.count(element))
print(count_dict)
