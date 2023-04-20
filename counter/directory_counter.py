import os

from counter.file_counter import FileCounter
from language import Language
from language.syntax_rules import Syntax


class DirectoryCounter:
    def __init__(self, directory_name):
        self.directory_total_lines = 0
        self.directory_blank_lines = 0
        self.directory_comment_lines = 0
        self.directory_code_lines = 0
        self.directory = directory_name
        self.directory_imports = 0

    def count_lines_in_directory(self):
        """Count the lines of code in all files in a directory and its subdirectories."""

        for subdir, _, files in os.walk(self.directory):
            for file in files:
                filepath = os.path.join(subdir, file)
                language_name = Language.getLanguageForFileByExtension(filepath)
                syntax = Syntax(language_name)
                counter = FileCounter(filepath, syntax, language_name)
                blank_lines, comment_lines, code_lines, imports = counter.count_lines_in_file()

                self.directory_blank_lines += blank_lines
                self.directory_comment_lines += comment_lines
                self.directory_code_lines += code_lines
                self.directory_imports +=imports
                self.directory_total_lines = self.directory_code_lines + self.directory_blank_lines + self.directory_comment_lines
                print(
                    f"{filepath}: Blank: {blank_lines}, Comments: {comment_lines}, Code: {code_lines}, Total: {blank_lines + comment_lines + code_lines}")
