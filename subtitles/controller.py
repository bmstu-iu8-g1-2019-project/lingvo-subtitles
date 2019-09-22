
from subtitles.models import opensubtitles


class Controller(object):
    def __init__(self):
        self.mdl = opensubtitles.OpenSubtitlesModel()

    def search_by_name_get_first_n(self, name, n=2):
        return self.mdl.search_by_name_get_first_n(name, n)

