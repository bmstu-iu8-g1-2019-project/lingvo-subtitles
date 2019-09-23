from subtitles.models import opensubtitles
from subtitles.models import converter
from subtitles.models import yandex_translate


class Controller(object):
    def __init__(self):
        self._os_mdl = opensubtitles.OpenSubtitlesModel()
        self._yt_mdl = yandex_translate.YandexTranslateModel()

    def search_by_name_get_first_n(self, name, n=2):
        return self._os_mdl.search_by_name_get_first_n(name, n)

    def get_learning_mode_data(self, name):
        path_to_subtitle_file = self._os_mdl.download_by_file_id(self._os_mdl.search_by_name_get_most_fit(name).get('IDSubtitleFile'))
        conv = converter.Converter(path_to_subtitle_file)
        return self._yt_mdl.translate_words_en_ru(conv.to_list())
