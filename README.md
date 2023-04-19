# OpenEnvoy

This Python script counts the lines of code in a given directory (and its subdirectories) that match certain file extensions.

Requirements
Python 3.x

Clone the repository and run the code_counter.py file.

Open a terminal and navigate to the directory where the code_counter.py file is located.

Run the script using the following command:

python code_counter.py --file=files/test_python_code.py --type=file --language=python
The script will output the total number of lines of code and the number of lines of code for each file that matches the specified file extensions.
FileName files/test_python_code.py
Total: 10
Blank: 2
Comments: 2
Code: 6


python code_counter.py --file=files/test_java_code.java --type=file
The script will output the total number of lines of code and the number of lines of code for each file that matches the specified file extensions.
FileName files/test_java_code.java
Total: 19
Blank: 4
Comments: 9
Code: 6


python code_counter.py --type=directory
files/test_java_code.java: Blank: 4, Comments: 9, Code: 6, Total: 19
files/test_python_code.py: Blank: 2, Comments: 2, Code: 6, Total: 10
Directory files
Total: 29
Blank: 6
Comments: 11
Code: 12

