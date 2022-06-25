import requests

"""
Write To A File Exercise 4 in HillelExam.docx
"""

file_name = str(input('Please, input file name '))

url_text = 'https://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html'
response = requests.get(url_text).text
with open(f'{file_name}.txt', 'w') as file:
    file.write(response)
