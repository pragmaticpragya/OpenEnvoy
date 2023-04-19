import os
from config import Config

class Language:
    def __init__(self, name, comment_prefixes):
        self.name = name
        self.comment_prefixes = comment_prefixes

    def is_comment(self, line):
        return any(line.strip().startswith(prefix) for prefix in self.comment_prefixes)

    @staticmethod
    def getLanguageForFileByExtension(filepath):
        if os.path.splitext(filepath)[1] == '.py':
            return Config.PYTHON
        elif os.path.splitext(filepath)[1] == '.java':
            return Config.JAVA
        else:
            ValueError("not found")