import requests
import pprint

pp = pprint.PrettyPrinter(depth=5)

url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''

respond = requests.get(url)

if respond.ok:
    respond_text = respond.text

# Task 1
p = []
array = respond_text.split('/&q;,&q;title&q;:&q;')
for item in array[1::]:
    item.replace('image_header_list&q;,&q;order&q', '')
    p.append(item.split('&q;,&q;order&q;:')[0])
print('\nTask 1\n')
pp.pprint(p)

# Task 2
array_link = respond_text.split('.jpg&q;,&q;link&q;:&q;')[1::]
link = []
for item in array_link:
    item.replace('image_header_list&q;,&q;order&q', '')
    link.append(item.split('&q;,&q;title&q;:&q;')[0])

dict_p_link = {}
for index in range(len(p)):
    dict_p_link[p[index]] = link[index]
print('\nTask 2\n')
pp.pprint(dict_p_link)

# Task 3
divide_for_par = []
number = 0
for index in range(len(p)):
    if index <= 14:
        divider_1 = '"' + link[index] + '"'
        divider_2 = '"' + link[index + 1] + '"'
        first_p = respond_text.split(divider_1)[2].split(divider_2)[0]
    else:
        divider = '"' + link[index] + '"'
        first_p = respond_text.split(divider)[2].split('widget-list')[0]
    divide_for_par.append(first_p)

result = []
for element in divide_for_par:
    prom_result = []
    for item in element.split(' title="')[2::]:
        prom_result.append(item.split('" class=""')[0])
    result.append(prom_result)

for index in range(len(dict_p_link)):
    dict_p_link[p[index]] = [link[index]] + result[index]

print('\nTask 3\n')
pp.pprint(dict_p_link)
