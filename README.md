# Installation

1. Download from https://www.python.org/downloads
2. Install Pip: https://pip.pypa.io/en/stable/installation
  - After we run cmd:  pip install virtualenv (default a verison will be installed)
  We will have a path of package:  c:\users\nhanphamv\appdata\local\programs\python\python310\lib\site-packages (20.14.1)
  We can create multiple version for env:
  virtualenv --python=/c/Users/nhanphamv/Appdata/Local/Programs/Python/Python310/python.exe venv/python-39
  virtualenv /c/users/nhanphamv/appdata/local/programs/python/python310/python.exe venv/python-31.

  Active stript: $ > venv/python-39/Scripts/activate.

  !importan: the terminal on VSCODE, PHPstorm maybe can't run this cmd. We should re-open terminal or use another terminal.

3. Install and Export Package:

  - Can follow: https://note.nkmk.me/en/python-pip-install-requirements
  - Use cmd: pip -r requirements.txt or pip freeze > requirements.txt

4. Execute by cmd:
   Example: py .\example\variable.py