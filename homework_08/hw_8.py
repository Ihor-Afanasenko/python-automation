import requests, re

url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''
section_tag = 'class="tile-cats__heading ng-star-inserted'
respond = requests.get(url)

if respond.ok:
    respond_text = respond.text

sections_dict = {}
section_pattern = re.compile('>\s?(.+?)\s?</a>')
subsection_pattern = re.compile('a _ngcontent-sc.+?href="(.+?)".+?class="">\s?(.+?)\s?</a>')

for section_text in respond_text.split('class="tile-cats__heading ng-star-inserted"'):
    section_found = section_pattern.search(section_text)
    if section_found:
        section_data = []
        for subsection in subsection_pattern.finditer(section_text):
            if subsection:
                section_data.append(subsection.groups())
        if section_data:
            sections_dict.setdefault(section_found.groups()[0], tuple(section_data))
        section_data.clear()

with open('results.txt', 'w', encoding='utf8') as f:
    for section, subsections in sections_dict.items():
        f.write(f'\t{section}\t'.center(120, "-") + "\n")
        for items in subsections:
            f.write("{1:.<50}\t{0:>}\n".format(*items))
            f.flush()
        f.write("\n" * 2)
