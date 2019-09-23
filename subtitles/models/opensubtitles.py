from pythonopensubtitles.opensubtitles import OpenSubtitles


class OpenSubtitlesModel(object):
    def __init__(self):
        self.ost = OpenSubtitles('en')

    def _refresh_auth(self):
        return self.ost.login('doctest', 'doctest')

    def search_by_name_get_first_n(self, name, n):
        self._refresh_auth()
        search_result = self.ost.search_subtitles([{'sublanguageid': 'eng', 'query': name}])
        if type(search_result) == list and len(search_result) > 0:
            parsed_result = search_result[0:n]
            return parsed_result
        else:
            return

    def search_by_name_get_most_fit(self, name):
        return self.search_by_name_get_first_n(name, 1)[0]

    def download_by_file_id(self, id_subtitle_file):
        self._refresh_auth()
        path_to_files_by_id = self.ost.download_subtitles([id_subtitle_file])  # Files are placed at project root
        return path_to_files_by_id
