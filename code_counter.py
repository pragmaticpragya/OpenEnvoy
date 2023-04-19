import argparse
from counter.directory_counter import DirectoryCounter
from counter.file_counter import FileCounter
from language.syntax_rules import Syntax

## main function which takes input arguments
##  --file : file name
##  --type : file or directory
##  --directory : name of file

def main():
    parser = argparse.ArgumentParser(description='Count lines of code in a file')
    parser.add_argument('--file', help='File to count lines of code')
    parser.add_argument('--language', choices=['java', 'python'], default='java',
                        help='Programming language used in the file')
    parser.add_argument('--type', choices=['file', 'directory'], default='file',
                        help='parse file or directory')
    parser.add_argument('--directory', default='files')
    args = parser.parse_args()

    if args.type == "directory":
        directory_name = "files"
        counter = DirectoryCounter(directory_name)
        counter.count_lines_in_directory()

        print(f"Directory {directory_name}")
        print('Total: {}'.format(counter.directory_total_lines))
        print('Blank: {}'.format(counter.directory_blank_lines))
        print('Comments: {}'.format(counter.directory_comment_lines))
        print('Code: {}'.format(counter.directory_code_lines))
        print('Imports: {}'.format(counter.directory_imports))

    else:
        language = Syntax(args.language)
        counter = FileCounter(args.file, language)
        counter.count_lines_in_file()

        print(f"FileName {args.file}")
        print('Total: {}'.format(counter.total_lines))
        print('Blank: {}'.format(counter.blank_lines))
        print('Comments: {}'.format(counter.comment_lines))
        print('Code: {}'.format(counter.code_lines))
        print('Imports: {}'.format(counter.imports))



if __name__ == '__main__':
    main()
