
class FileCounter:
    def __init__(self, file_path, language):
        self.file_path = file_path
        self.language = language
        self.total_lines = 0
        self.blank_lines = 0
        self.comment_lines = 0
        self.code_lines = 0
        self.imports = 0

    def count_lines_in_file(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            self.total_lines = len(lines)
            in_multiline_comment = False

            for line in lines:
                if line.strip() == '':
                    self.blank_lines += 1
                elif line.strip().startswith('/*'):
                    self.comment_lines += 1
                    in_multiline_comment = True
                elif line.strip().endswith('*/') and in_multiline_comment:
                    self.comment_lines += 1
                    in_multiline_comment = False
                elif in_multiline_comment:
                    self.comment_lines += 1
                elif self.language.is_comment(line):
                    self.comment_lines += 1
                else:
                    self.code_lines += 1

                if line.startswith("import") or line.startswith("from"):
                    self.imports += 1
            return [self.blank_lines, self.comment_lines, self.code_lines, self.imports]


