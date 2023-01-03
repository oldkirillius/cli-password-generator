# necessary imports
import secrets
import string
import argparse

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


# # generate password meeting constraints
# while True:
#   pwd = ''
#   for i in range(pwd_length):
#     pwd += ''.join(secrets.choice(alphabet))

#   if (any(char in special_chars for char in pwd) and 
#       sum(char in digits for char in pwd)>=2):
#           break
# print(pwd)


def read_arguments():
    parser = argparse.ArgumentParser(
    description="Create password."
    )
    parser.add_argument(
        "-length", "-l", help="Length of password.", type=int, default=12
    )
    parser.add_argument(
        "-complexity", "-c", help="Set password complexity options: [L]etters, [N]umbers, [S]ymbols.", default="LNS"
    )
    args = parser.parse_args()
    return args

def create_password(length, complexity):
    alphabet = ''
    pwd = ''
    
    if "L" in complexity:
        alphabet += letters
    if "N" in complexity:
        alphabet += digits
    if "S" in complexity:
        alphabet += special_chars
    
    if len(alphabet) == 0:
        alphabet += letters
    
    for i in range(length):
        pwd += ''.join(secrets.choice(alphabet))

    print (pwd)

def main ():
    args = read_arguments()
    create_password(args.length, args.complexity)
    
main()

import os
os.system("pause")