# This is a sample Python script.
import sys
import re

from validate_email_address import validate_email

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def validate(namedict, domain, output):
    print("")
    for firstName in namedict:
        is_valid = validate_email(firstName + "." + namedict[firstName] + "@" + domain)
        if (is_valid):
            print( "    " + firstName + "." + namedict[firstName] + "@" + domain + " :: Checked and Valid")
            output.write(firstName + "." + namedict[firstName] + "@" + domain)
    print("")
def menu(name, domain):
    print("####################################################################")
    print("   \ \        / / | |                                               ")
    print("    \ \  /\  / /__| | ___ ___  _ __ ___   ___                       ")
    print("    _\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \                      ")
    print("   | |\  /\  /  __/ | (_| (_) | | | | | |  __/                      ")
    print("   | |_\/__\/ \___|_|\___\___/|_| |_| |_|\___|                      ")
    print("   | __/ _ \                                                        ")
    print("   | || (_) |                                                       ")
    print("    \__\___/               _ _  _____ _               _             ")
    print("   |  ____|               (_) |/ ____| |             | |            ")
    print("   | |__   _ __ ___   __ _ _| | |    | |__   ___  ___| | _____ _ __ ")
    print("   |  __| | '_ ` _ \ / _` | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|")
    print("   | |____| | | | | | (_| | | | |____| | | |  __/ (__|   <  __/ |   ")
    print("   |______|_| |_| |_|\__,_|_|_|\_____|_| |_|\___|\___|_|\_\___|_|   ")
    print("")
    print("Made by Daniel Coutinho")
    print("####################################################################")
    print("")
    print("")
    print("Email List:")

    namedict = {}
    domainList = []
    # NEEDS BETTER VALIDATION on input from name and domain
    if(re.match(".+\.txt", name)):
        with open(name) as f:
            for line in f:
                (firstName, lastName) = line.split()
                namedict[firstName.replace("\n", "")] = lastName.replace("\n", "")
    else:
        (firstName, lastName) = name.split()
        namedict[firstName] = lastName

    if (re.match(".+\.txt", domain)):
        with open(domain) as f:
            for line in f:
                domainList.append(line.replace("\n", ""))
    else:
        domainList.append(domain)

    output = open("output.txt", "wt")
    for dmain in domainList:
        validate(namedict, dmain, output)


def main():
    '''Get argument values, convert, call quad.'''

    s1, s2 = sys.argv[1], sys.argv[2]
    menu(s1, s2)





main()