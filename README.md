# Installation

1. Download from https://www.python.org/downloads
2. Install Pip: https://pip.pypa.io/en/stable/installation
  - After we run cmd:  pip install virtualenv (default a verison will be installed)
  We will have a path of package:  c:\users\nhanphamv\appdata\local\programs\python\python310\lib\site-packages (20.14.1)
  We can create multiple version for env:
  virtualenv --python=/c/Users/nhanphamv/Appdata/Local/Programs/Python/Python310/python.exe venv/python-39
  virtualenv /c/users/nhanphamv/appdata/local/programs/python/python310/python.exe venv/python-31.

  Active stript: $ > venv/python-39/Scripts/activate.

3. Install and Export Package:
  - Can follow: https://note.nkmk.me/en/python-pip-install-requirements
  - Use cmd: pip -r requirements.txt or pip freeze > requirements.txt

4. Execute by cmd:
   Example: py .\example\variable.py

5. Handle Errors and Exceptions:
   https://docs.python.org/3/tutorial/errors.html

6. Python OOPs Concepts
https://www.geeksforgeeks.org/python-oops-concepts/

7. Python handle file
   https://www.w3schools.com/python/python_file_handling.asp
   - "r" - Read - Default value. Opens a file for reading, error if the file does not exist
   - "a" - Append - Opens a file for appending, creates the file if it does not exist
   - "w" - Write - Opens a file for writing, creates the file if it does not exist
   - "x" - Create - Creates the specified file, returns an error if the file exists 

8. Format Float 
  - https://appdividend.com/2021/03/31/how-to-format-float-values-in-python