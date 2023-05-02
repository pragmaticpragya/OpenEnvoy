import argparse
import os
from counter.directory_counter import DirectoryCounter
from counter.file_counter import FileCounter
from exceptions import CustomException
from exceptions.validations import Validations
from language import Language
from language.syntax_rules import Syntax

##  main function which takes input arguments
##  --filepath : file/directory name

def main():
    parser = argparse.ArgumentParser(description='Count lines of code in a file')
    parser.add_argument('--filepath', help='File to count lines of code')
    args = parser.parse_args()
    filepath = args.filepath

    # validations
    try:
        Validations.check_file_path(filepath)
    except CustomException as e:
        print("Caught a custom exception:", e.message)
        return

    if os.path.isdir(filepath):
        counter = DirectoryCounter(filepath)
        counter.count_lines_in_directory()

        print(f"Directory {filepath}")
        print('Total: {}'.format(counter.total_lines))
        print('Blank: {}'.format(counter.blank_lines))
        print('Comments: {}'.format(counter.comment_lines))
        print('Code: {}'.format(counter.code_lines))
        print('Imports: {}'.format(counter.imports))

    elif os.path.isfile(filepath):
        language_name = Language.get_language_for_file_by_extension(filepath)
        syntax = Syntax(language_name)
        counter = FileCounter(filepath, syntax, language_name)
        counter.count_lines_in_file()

        print(f"FileName {filepath}")
        print('Total: {}'.format(counter.total_lines))
        print('Blank: {}'.format(counter.blank_lines))
        print('Comments: {}'.format(counter.comment_lines))
        print('Code: {}'.format(counter.code_lines))
        print('Imports: {}'.format(counter.imports))

    else:
        try:
            Validations.not_file_or_directory(filepath)
        except CustomException as e:
            print("Caught a custom exception:", e.message)
            return


if __name__ == '__main__':
    main()
