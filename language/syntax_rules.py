from config import Config
from language.__init__ import Language


class Syntax(Language):
    def __init__(self, language):
        for key, value in Config().language_comments_map.items():
            if language == key:
                super().__init__(key, value["comments"])
            else:
                ValueError("Language not found")
