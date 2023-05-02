from config import Config
from exceptions import CustomException
from exceptions.validations import Validations
from language.__init__ import Language


class Syntax(Language):
    def __init__(self, language):
        try:
            syntax = Config().language_comments_map[language]
            super().__init__(language, syntax["comments"], syntax["import_vars"])
            Validations.check_language(language)
        except CustomException as e:
            print("Caught a custom exception:", e.message)
            return
