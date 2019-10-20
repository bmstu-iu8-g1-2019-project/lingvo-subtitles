from app.models import yandex_translate, converter, opensubtitles, registration


def register(email, username, hashed_password):
    return registration.register_user(email, username, hashed_password)


class Controller(object):
    def __init__(self, yandex_translate_api_key):
        self._os_mdl = opensubtitles.OpenSubtitlesModel()
        self._yt_mdl = yandex_translate.YandexTranslateModel(yandex_translate_api_key)

    def search_by_name_get_first_n(self, name, n=2):
        return self._os_mdl.search_by_name_get_first_n(name, n)

    def get_learning_mode_data(self, name):
        path_to_subtitle_file = self._os_mdl.download_by_file_id(self._os_mdl.search_by_name_get_most_fit(name).get('IDSubtitleFile'))
        ct_mdl = converter.Converter(path_to_subtitle_file)

        words = ct_mdl.to_list()

        return self._yt_mdl.translate_words_en_ru(words)
