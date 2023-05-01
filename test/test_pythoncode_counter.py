import os
import unittest

from counter.file_counter import FileCounter
from language.syntax_rules import Syntax

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'files/test_python_code.py')

class PythonCodeCounterTest(unittest.TestCase):

   def setUp(self):
       self.testfile = TESTDATA_FILENAME
       self.language = Syntax("python")

   def test_total_lines(self):
       counter = FileCounter(self.testfile, self.language, "python")
       counter.count_lines_in_file()
       assert counter.total_lines == 10

   def test_blank_lines(self):
       counter = FileCounter(self.testfile, self.language, "python")
       counter.count_lines_in_file()
       assert counter.blank_lines == 2

   def test_code_lines(self):
       counter = FileCounter(self.testfile, self.language, "python")
       counter.count_lines_in_file()
       assert counter.code_lines == 6

   def test_comment_lines(self):
       counter = FileCounter(self.testfile, self.language, "python")
       counter.count_lines_in_file()
       assert counter.comment_lines == 2

   def test_import_lines(self):
       counter = FileCounter(self.testfile, self.language, "python")
       counter.count_lines_in_file()
       assert counter.imports == 0