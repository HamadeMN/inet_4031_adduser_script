#!/usr/bin/python3

# INET4031
# Hamade Yaseen Ali
# 3/26/29
# 3/26/29

import os #os is used to run Linux system commands
import re # re is used for pattern matching
import sys #sys is used to read input from a file

def main():
    for line in sys.stdin:

        # this checks if the line starts with "#" which means it is a comment
        # "#" is used in the input file to mark lines that should be skipped
        match = re.match("^#",line)

        # this removes spaces/newlines and splits the line into parts using ":"
        fields = line.strip().split(':')

        # This IF checks if the line is a comment or does not have exactly 5 fields.
        # If true, the line is skipped and not processed.
        # It uses match from the previous line to detect comments.
        # It uses fields from the previous line to check if the data format is correct.
        # It checks for 5 fields to make sure the input is valid before continuing.
        if match or len(fields) != 5:
            continue

        # this assigns the username from the input line
        username = fields[0]

        # this assigns the password from the input line
        password = fields[1]

        # this creates the gecos field (name info) to match the format used in /etc/passwd
        gecos = "%s %s,,," % (fields[3],fields[2])

        # this splits the group field by commas so the user can be added to multiple groups
        groups = fields[4].split(',')

        # this prints a message showing that a user is about to be created
        print("==> Creating account for %s..." % (username))

        # this builds the command that will create the user account
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # the first time running the code, this should stay commented to do a dry run
        # if uncommented, it will actually create the user on the system
        #print(cmd)
        os.system(cmd)

        # this prints a message showing the password is being set
        print("==> Setting the password for %s..." % (username))

        # this builds the command to set the user's password automatically
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # the first time running the code, this should stay commented to avoid real changes
        # if uncommented, it will actually set the password on the system
        #print(cmd)
        os.system(cmd)

        for group in groups:
            # this checks if the group is not "-" because "-" means no group
            # if true, the user will be added to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
