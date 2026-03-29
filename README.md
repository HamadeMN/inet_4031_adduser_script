# Create Users Script

## Description
This program reads user data from an input file and creates users, sets passwords, and assigns groups automatically on a Linux system.

## How It Works
The script reads each line from the input file. It skips comments and invalid lines. Then it extracts the username, password, and group info, and runs Linux commands to create users and assign them to groups.

## How to Run
Make script executable:
chmod +x create-users.py

Dry run:
./create-users.py < create-users.input

Real run:
sudo ./create-users.py < create-users.input# inet_4031_adduser_script
