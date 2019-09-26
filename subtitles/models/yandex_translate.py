from yandex_translate import YandexTranslate


class YandexTranslateModel(object):
    def __init__(self):
        self._translator = YandexTranslate(
            'trnsl.1.1.20190923T142916Z.e5bcea9267318d2d.1b812152591630d0d5a19f2e4c6dd07398a8bb9e')

    def translate_word_en_ru(self, word):
        translated_word_dict = self._translator.translate(word, 'en-ru')
        if translated_word_dict['code'] == 200:
            return translated_word_dict['text'][0]
        else:
            return

    def translate_words_en_ru(self, words):
        translated_words_dict = self._translator.translate(words, 'en-ru')

        if translated_words_dict['code'] != 200:
            return
        translated_words = translated_words_dict['text']

        word_translations_pairs = list()
        for index in range(len(words)):
            word_translations_pairs.append(list({words[index], translated_words[index]}))

        return word_translations_pairs
