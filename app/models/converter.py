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

        for word_pair in words:
            word_tags = set()
            for word_synsets in wordnet.synsets(word_pair[0]):
                if word_synsets.name().split('.')[0] == word_pair[0]:
                    word_tags.add(word_synsets.pos())
            if len(word_tags) > 0:
                parsed_words.append(word_pair[0])

        return parsed_words
