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
<img width="1239" alt="image" src="https://user-images.githubusercontent.com/131292089/233160565-ec54e068-5277-4a0e-9027-7e68d83b5305.png">



**python code_counter.py --file=files/test_java_code.java --type=file**<br/>
The script will output the total number of lines of code and the number of lines of code for each file that matches the specified file extensions.<br/>
**FileName files/test_java_code.java<br/>
<img width="1244" alt="image" src="https://user-images.githubusercontent.com/131292089/233160850-abff7e85-d48a-41ba-984b-eb1a82093937.png">



**python code_counter.py --type=directory**<br/>
files/test_java_code.java: Blank: 4, Comments: 9, Code: 6, Total: 19<br/>
files/test_python_code.py: Blank: 2, Comments: 2, Code: 6, Total: 10<br/>
**Directory files<br/>
<img width="1247" alt="image" src="https://user-images.githubusercontent.com/131292089/233161046-f3509cb6-7fc8-4ed3-80c8-2118687aaa30.png">

