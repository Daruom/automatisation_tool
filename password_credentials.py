#!/usr/bin/env python
import sys
import fileinput
import time
import os
from ansible.playbook import Playbook
from shutil import copyfile

def main(arguments):
    username = raw_input("Enter username\n")
    password = raw_input("Enter new password\n")
    playbook_path = "/home/thor/Public/Atom_projects/automatisation_tool/password_reset_with_server.yml"
    playbook_final_path = "/home/thor/Public/Atom_projects/automatisation_tool/password_reset_final.yml"
    copyfile(playbook_path,playbook_final_path)
    for line in fileinput.input(playbook_final_path, inplace=True):
        line = line.rstrip()
        if "username_var" in line:
            line = line.replace('username_var', username)
        if "password_var" in line:
            line = line.replace('password_var', password)
        print line

    ansible_command = "ansible-playbook password_reset_final.yml -K -v"
    os.system(ansible_command)
    time.sleep(2)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
