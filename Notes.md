"pip install PyQt5" into the Intelij Terminal

Download the latest version for Windows
Download Python 3.12.3
under https://www.python.org/downloads/

- paste and run in command prompt:
  "pip install PyQt5" (https://pypi.org/project/PyQt5/)


(It seems like the pip command is not recognized in your command prompt? 
This typically happens when Python is not added to your system's PATH environment variable during installation.

To fix this issue, you can follow these steps:

- Find the Path to Python Scripts:
First, find out where Python is installed on your system. You can usually find it in C:\PythonXX (where XX is the version number) or C:\Users\<YourUsername>\AppData\Local\Programs\Python\PythonXX.
- Look for the Scripts directory within the Python installation directory. This directory contains the pip executable.
- Add Python Scripts to PATH:
1) Copy the path to the Scripts directory.
2) Open the Control Panel and search for "environment variables".
3) Click on "Edit the system environment variables".
4) In the System Properties window, click on the "Environment Variables..." button.
5) In the Environment Variables window, under "System variables", find the "Path" variable and select it. Then click "Edit...".
6) Click "New" and paste the path to the Scripts directory.
7) Click "OK" on all windows to save your changes.
8) Restart Your Command Prompt:
Close and reopen your command prompt. Now, the pip command should be recognized.)


