# Entropy Calculator Tool
# view.py
# Created by Mauro J. Pappaterra on 25 of August 2018.

welcome = """
╔═╗┌┐┌┌┬┐┬─┐┌─┐┌─┐┬ ┬  ╔═╗┌─┐┬  ┌─┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐  ╔╦╗┌─┐┌─┐┬  
║╣ │││ │ ├┬┘│ │├─┘└┬┘  ║  ├─┤│  │  │ ││  ├─┤ │ │ │├┬┘   ║ │ ││ ││  
╚═╝┘└┘ ┴ ┴└─└─┘┴   ┴   ╚═╝┴ ┴┴─┘└─┘└─┘┴─┘┴ ┴ ┴ └─┘┴└─   ╩ └─┘└─┘┴─┘

                =Calculate Password Entropy=
"""

explosion = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____

"""

# MAIN MENU
menu = """\n::::Select one of the available options:
c - Calculate password entropy
s - Settings
a - About: Read more about password entropy
q - Quit"""

size = "Select the size of the set."
choose = "Select how many elements of the set you will choose"

def print_entropy (size, choose, entropy):
    return "Choosing " + str(choose) + " elements at random on a set of " + str(size) + " elements" + \
    "\nThe entropy equals to " + str(entropy)

def compare(ten, twentysix, fiftytwo, sixtytwo):
    print("\nThe necessary length for a randomly generated password to have the same entropy, would be:")
    print("From a set of 10 characters [0-9] => " + ten + " characters long")
    print("From a set of 26 characters [a-z] or [A-Z] => " + twentysix + " characters long")
    print("From a set of 52 characters [a-z] and [A-Z] => " + fiftytwo + " characters long")
    print("From a set of 62 characters [a-z] and [A-Z] and [0-9] => " + sixtytwo + " characters long")

entropy_menu = """\n::::Select one of the available options:
c - Calculate another password entropy
b - Back to main menu
"""

# SETTINGS PAGE
settings = """ blah blah blah
b - Back to menu"""

# ABOUT PAGE
about = """ blah blah blah
b - Back to menu"""

# ERROR MESSAGES
error_input = "\nInvalid Input: Enter a valid option then press <enter>"

def error_size (min, max):
    return "Give a number between " + str(min) + " and " + str(max)

cancel = "\nCANCEL BY USER"
exit = """\n                      <>==(|==============> Exit by User <==============|)==<>\n"""