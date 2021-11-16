import re
import requests

sections_dict = {}
section_pattern = re.compile('>\s?(.+?)\s?</a>')
subsection_pattern = re.compile('a _ngcontent-sc.+?href="(.+?)".+?class="">\s?(.+?)\s?</a>')

with open('respond.txt', encoding='utf8') as f:
    for section_text in f.read().split('class="tile-cats__heading ng-star-inserted"'):
        section_found = section_pattern.search(section_text)
        if section_found:
            section_data = []
            for subsection in subsection_pattern.finditer(section_text):
                if subsection:
                    section_data.append(subsection.groups())
            if section_data:
                sections_dict.setdefault(section_found.groups()[0], tuple(section_data))
            section_data.clear()
