from __future__ import annotations

from datetime import datetime, date
from xml.etree import ElementTree


class Movie:
    def __init__(self,
                 category: str,
                 decade: str,
                 title: str,
                 format: str,
                 year: date,
                 rating: str,
                 description: str
                 ) -> None:
        self.__category = category
        self.__decade = decade
        self.__title = title
        self.__format = format
        self.__year = year
        self.__rating = rating
        self.__description = description

    def __str__(self) -> str:
        result = ''

        for key, value in self.__dict__.items():
            key_without_class = str(key).split('__')[1]
            if type(value) is datetime:
                result += f"\'{key_without_class}\': \'{datetime.strftime(value,'%Y')}\',\n"
            else:
                result += f'\'{key_without_class}\': \'{value}\',\n'
        return "{\n" + result[:-2] + "\n}"

    @classmethod
    def parse_xml_file_with_data_convert_to_movies_list(cls, path: str) -> list[Movie]:
        tree = ElementTree.parse(path)
        root = tree.getroot()
        movies = []
        for genre in root.findall("genre"):
            for decade in genre.findall("decade"):
                for movie in decade.findall("movie"):
                    movies.append(cls(genre.attrib["category"],
                                      decade.attrib["years"],
                                      movie.attrib["title"],
                                      movie.findtext("format"),
                                      datetime.strptime(movie.findtext("year"), '%Y'),
                                      movie.findtext("rating"),
                                      movie.findtext("description").strip()
                                      ))
        return movies

    @classmethod
    def parse_xml_file_with_data_convert_to_movies_list_v_2(cls, path: str) -> list[Movie]:
        tree = ElementTree.parse(path)
        root = tree.getroot()
        movies = []
        movies_title = []
        for child in root.iter('movie'):
            movies_title.append(child.attrib['title'])
        for title in movies_title:
            movies.append(cls(root.find(f".//movie[@title=\"{title}\"]../..").attrib["category"],
                              root.find(f".//movie[@title=\"{title}\"]..").attrib["years"],
                              title,
                              root.findtext(f".//movie[@title=\"{title}\"]/format"),
                              datetime.strptime(root.findtext(f".//movie[@title=\"{title}\"]/year"), '%Y'),
                              root.findtext(f".//movie[@title=\"{title}\"]/rating"),
                              root.findtext(f".//movie[@title=\"{title}\"]/description").strip()
                              ))
        return movies


if __name__ == '__main__':
    # E.g.
    movie = Movie('Test', 'test', 'Test', 'HD', datetime.strptime("2005", '%Y'), 'PG', 'test')
    path = "movies.xml"
    movies = movie.parse_xml_file_with_data_convert_to_movies_list(path)
    for movie in movies:
        print(movie)

    movies_v2 = movie.parse_xml_file_with_data_convert_to_movies_list_v_2(path)
    for movie in movies_v2:
        print(movie)
