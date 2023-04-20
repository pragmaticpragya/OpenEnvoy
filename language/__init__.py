import os
from config import Config
from exceptions.custom_exception import CustomException
from exceptions.validations import Validations


class Language:
    def __init__(self, name, comment_prefixes, import_vars):
        self.name = name
        self.comment_prefixes = comment_prefixes
        self.import_vars = import_vars

    def is_comment(self, line):
        return any(line.strip().startswith(prefix) for prefix in self.comment_prefixes)

    @staticmethod
    def getLanguageForFileByExtension(filepath):
        file_extension = os.path.splitext(filepath)[1]
        for key, value in Config().language_comments_map.items():
            if file_extension == value["extension"]:
                return key

        try:
            Validations.check_language(file_extension)
        except CustomException as e:
            print("Caught a custom exception:", e.message)
            return

