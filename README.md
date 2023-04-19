# OpenEnvoy

This Python script counts the lines of code in a given directory (and its subdirectories) that match certain file extensions.

**Requirements** <br/>
Python 3.x<br/>

Clone the repository and run the code_counter.py file.<br/>

Open a terminal and navigate to the directory where the code_counter.py file is located.<br/>

**Run the script using the following command:**<br/>

**python code_counter.py --file=files/test_python_code.py --type=file --language=python**<br/>
The script will output the total number of lines of code and the number of lines of code for each file that matches the specified file extensions.<br/>
**FileName files/test_python_code.py<br/>
Total: 10<br/>
Blank: 2<br/>
Comments: 2<br/>
Code: 6**<br/>


**python code_counter.py --file=files/test_java_code.java --type=file**<br/>
The script will output the total number of lines of code and the number of lines of code for each file that matches the specified file extensions.<br/>
**FileName files/test_java_code.java<br/>
Total: 19<br/>
Blank: 4<br/>
Comments: 9<br/>
Code: 6**<br/>


**python code_counter.py --type=directory**<br/>
files/test_java_code.java: Blank: 4, Comments: 9, Code: 6, Total: 19<br/>
files/test_python_code.py: Blank: 2, Comments: 2, Code: 6, Total: 10<br/>
**Directory files<br/>
Total: 29<br/>
Blank: 6<br/>
Comments: 11<br/>
Code: 12**<br/>

