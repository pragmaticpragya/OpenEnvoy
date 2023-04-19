import os
import unittest

from counter.file_counter import FileCounter
from language.syntax_rules import Syntax

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'files/test_java_code.java')

class JavaCodeCounterTest(unittest.TestCase):

   def setUp(self):
       self.testfile = TESTDATA_FILENAME
       self.language = Syntax("java")

   def test_total_lines(self):
       counter = FileCounter(self.testfile, self.language)
       counter.count_lines_in_file()
       assert counter.total_lines == 19

   def test_blank_lines(self):
       counter = FileCounter(self.testfile, self.language)
       counter.count_lines_in_file()
       assert counter.blank_lines == 4

   def test_code_lines(self):
       counter = FileCounter(self.testfile, self.language)
       counter.count_lines_in_file()
       print(counter.code_lines)
       assert counter.code_lines == 6

   def test_comment_lines(self):
       counter = FileCounter(self.testfile, self.language)
       counter.count_lines_in_file()
       assert counter.comment_lines == 9

   def test_import_lines(self):
       counter = FileCounter(self.testfile, self.language)
       counter.count_lines_in_file()
       assert counter.imports == 1

