#!/usr/bin/python3
# INET4031
# Hamade Yaseen Ali
# create-users2.py

import os
import re
import sys

# Ask user if they want a dry run — reads from terminal even when stdin is redirected
sys.stderr.write("Would you like to do a dry run? (Y/N): ")
sys.stderr.flush()
mode = open('/dev/tty').readline().strip().upper()

def main():
    for line in sys.stdin:
        # Check if line is a comment (starts with #)
        match = re.match("^#", line)

        # Split line into fields using ":"
        fields = line.strip().split(':')

        # Skip comment lines
        if match:
            if mode == "Y":
                print("Skipping commented line.")
            continue

        # Skip lines that don't have exactly 5 fields
        if len(fields) != 5:
            if mode == "Y":
                print("Error: line does not have enough fields, skipping.")
            continue

        # Grab info from the fields
        username = fields[0]
        password = fields[1]
        gecos    = "%s %s,,," % (fields[3], fields[2])
        groups   = fields[4].split(',')

        # Create the user
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        if mode == "Y":
            print("DRY RUN would run: " + cmd)
        else:
            os.system(cmd)

        # Set the password
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        if mode == "Y":
            print("DRY RUN would run: " + cmd)
        else:
            os.system(cmd)

        # Add user to groups
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                if mode == "Y":
                    print("DRY RUN would run: " + cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
