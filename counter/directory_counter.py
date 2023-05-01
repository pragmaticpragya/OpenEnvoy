import os

from counter.file_counter import FileCounter
from language import Language
from language.syntax_rules import Syntax


class DirectoryCounter:
    def __init__(self, directory_name):
        self.total_lines = 0
        self.blank_lines = 0
        self.comment_lines = 0
        self.code_lines = 0
        self.directory = directory_name
        self.imports = 0

    def count_lines_in_directory(self):
        """Count the lines of code in all files in a directory and its subdirectories."""

        for subdir, _, files in os.walk(self.directory):
            for file in files:
                filepath = os.path.join(subdir, file)
                language_name = Language.get_language_for_file_by_extension(filepath)
                syntax = Syntax(language_name)
                counter = FileCounter(filepath, syntax, language_name)
                blank_lines, comment_lines, code_lines, imports = counter.count_lines_in_file()

                self.blank_lines += blank_lines
                self.comment_lines += comment_lines
                self.code_lines += code_lines
                self.imports += imports
                self.total_lines = self.code_lines + self.blank_lines + self.comment_lines
                print(
                    f"{filepath}: Blank: {blank_lines}, Comments: {comment_lines}, Code: {code_lines}, Total: {blank_lines + comment_lines + code_lines}")
