# Goal: Make a random password generator. Have the password be between 12-18 characters, and must include:
#   - One special character
#   - At least one upper case letter
#   - Three to five numbers

# Imports
import random # For random number generation
import string # For random string generation
import secrets # For secure randomization
import time # For a delay between welcome and starting

# Color codes
LIGHTER_RED = '\033[91m'
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

def welcome():
    line1 = "-------------------------------------------------------------\n"
    line2 = f"\t\t{BOLD}{GREEN}Random Password Generator{END}\n"
    line4 = "-------------------------------------------------------------"
    result = line1 + line2 + line4
    return result

# ------------ NOT USED. REPLACED WITH random_string(). SEE BELOW. ------------
def string_randomizer():
    while True:
        try:
            num = int(input("How many letters do you want in your password?: "))

            if num < 0:
                print(f"{LIGHT_RED}Error.{END} Number cannot be negative")
                continue
            elif num < 8:
                print(f"{LIGHT_RED}Error.{END} Number must be {DARK_GRAY}at least{END} 8.")
            elif num > 12:
                print(f"{LIGHT_RED}Error.{END} Number must be {LIGHT_BLUE}at most{END} 12.")
            else:
                letters = ''.join(random.choices(string.ascii_letters, k=num))
                return letters
        except ValueError:
            print(f"{RED}Invalid{END}")

def random_string():
    while True:
        try:
            length = int(input("How many letters do you want in your password?: "))

            alphabet = string.ascii_letters + string.digits

            if length < 0:
                print(f"{LIGHT_RED}Error.{END} Number cannot be negative.")
                continue
            elif length < 8:
                print(f"{LIGHT_RED}Error.{END} Number must be {DARK_GRAY}at least{END} 8.")
            elif length > 12:
                print(f"{LIGHT_RED}Error.{END} Number must be {DARK_GRAY}no more than{END} 12.")
            else:
                uppercase = secrets.choice(string.ascii_uppercase)
                letters = uppercase + ''.join(secrets.choice(alphabet) for _ in range(length - 1))
                return f"{YELLOW}{letters}{END}"
        except ValueError:
            print(f"{RED}Enter a valid number.{END}")

# Ask the user how many numbers they want in their password, and randomize them
def random_num():
    while True:
        try:
            num = int(input("How many numbers would you like in your password?: "))

            if num < 0:
                print(f"{LIGHT_RED}Error.{END} Number cannot be negative.")
                continue
            elif num < 3:
                print(f"{LIGHT_RED}Error.{END} Number must be {DARK_GRAY}at least{END} 3.")
            elif num > 5:
                print(f"{LIGHT_RED}Error.{END} Number must be {DARK_GRAY}no more than{END} 5.")
            else:
                x = 0
                result = ''
                while x < num:
                    result += secrets.choice(string.digits)
                    x += 1
                return f"{YELLOW}{result}{END}"

        except ValueError:
            print(f"{RED}Enter a valid number{END}")

# Required special character, throw an error if not in special characters list
def special_char():
    while True:
        char = input("Enter a special character: ")

        if char == 'help':
            for char in string.punctuation:
                print(char, end="  ")
            print("\n")
        elif char in string.punctuation and len(char) == 1:
            return f"{YELLOW}{char}{END}"
        else:
            print(f"{LIGHT_RED}Error.{END} Please enter {UNDERLINE}one{END} special character or type {DARK_GRAY}help{END} to view all options.")
            continue

print(welcome())
time.sleep(.5)
print(f"Your password is:", random_string() + random_num() + special_char())