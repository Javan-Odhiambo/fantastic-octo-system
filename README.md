## Setting up

### Clone the repository from your terminal with the command <br>
```
git clone https://github.com/Javan-Odhiambo/fantastic-octo-system.git
```

### Move into the folder<br>
```
cd fantastic-octo-system
```

**Make sure python is installed and if not install it from _[here](https://www.python.org/downloads/)_.<br>Depending on how you installed python you might change the word `python` to `py` in the following commands.**

### Create a virtual environment <br>
```
python -m venv venv
```

### Activate the virtual environment <br>
In windows cmd `venv\Scripts\activate`<br>
In windows git bash `source venv\Scripts\activate`<br>
In linux `source venv/bin/activate`

**NOTE: The windows command does not work in powershell** <br>
Your cmd should look something like this if you succesfully activated the environment.
```
(venv) C:\Users\path\to\repository\fantastic-octo-system>
```

### Install the requirements <br>
```
pip install -r requirements.txt
```

### Set a Normal username<br>
In the file `variables.py` remove the 0 and put a valid username that you are sure either works or is normal.

### Run the program <br>
```
python run.py
```
**Ignore the warnings in the terminal for now**

### **ALL working usernames will be written to a file called `Working.txt`**

## Customization of the program
All customizable parameters are in the `variables.py` file. **DO NOT MODIFY ANY OTHER FILES** <br>
You can customize the following parameters in the program:<br>

- [x] MIN_RANGE - The minimum username to test.
- [x] MAX_RANGE - The highest username to test.
- [x] NO_OF_TRIALS -How many usernames should be tested before quiting.
- [x] SECONDS_TO_WAIT_BEFORE_NEXT_TEST - Number of seconds to wait before checking for a network connection and moving to the next.
- [x] NORMAL_USERNAME - A username that you are sure works or is atleast normal.

**NB: You have to set the normal username parameter.**
