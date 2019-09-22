from pysubparser import parser
from collections import Counter
from nltk.corpus import wordnet

import nltk
nltk.download('wordnet')


class Converter(object):
    def __init__(self, path_to_subtitle_file):
        self._subtitles = parser.parse(path_to_subtitle_file)

    def to_list(self):
        words_counter = Counter()
        for subtitle in self._subtitles:
            words_counter += Counter(
                (subtitle.clean_up(to_lowercase=True, remove_brackets=True, remove_formatting=True)).split())

        words = words_counter.most_common()
        parsed_words = list()

        for word in words:
            pos_l = set()
            for tmp in wordnet.synsets(word[0]):
                if tmp.name().split('.')[0] == word[0]:
                    pos_l.add(tmp.pos())
            if len(pos_l) > 0:
                parsed_words.append(word[0])

        return parsed_words
