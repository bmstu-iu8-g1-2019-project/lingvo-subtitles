from app.models import yandex_translate, converter, opensubtitles, registration, learning_mode


def register(email, username, hashed_password):
    return registration.register_user(email, username, hashed_password)


class Controller(object):
    def __init__(self, yandex_translate_api_key):
        self._opensubtitles_mdl = opensubtitles.OpenSubtitlesModel()
        self._yandextranslate_mdl = yandex_translate.YandexTranslateModel(yandex_translate_api_key)

    def search_by_name_get_first_n(self, name, n=2):
        return self._opensubtitles_mdl.search_by_name_get_first_n(name, n)

    def get_learning_mode_data(self, name, username):
        path_to_subtitle_file = self._opensubtitles_mdl.download_by_file_id(self._opensubtitles_mdl.search_by_name_get_most_fit(name).get('IDSubtitleFile'))
        converter_mdl = converter.Converter(path_to_subtitle_file)

        words = converter_mdl.to_list()

        translated_words = self._yandextranslate_mdl.translate_words_en_ru(words)

        return learning_mode.build_learning_mode_data(words, translated_words, username)
