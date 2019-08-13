#!/usr/bin/env python
import sys
import fileinput
import time
import os
from ansible.playbook import Playbook
from shutil import copyfile

def main(arguments):
    username = raw_input("Please enter the username to remove\n")
    playbook_path = "/home/thor/Public/Atom_projects/automatisation_tool/user_remove_with_server.yml"
    playbook_final_path = "/home/thor/Public/Atom_projects/automatisation_tool/user_remove_final.yml"
    copyfile(playbook_path,playbook_final_path)
    for line in fileinput.input(playbook_final_path, inplace=True):
        line = line.rstrip()
        if "username" in line:
            line = line.replace('username', username)
        print line

    ansible_command = "ansible-playbook user_remove_final.yml -K -v"
    os.system(ansible_command)
    time.sleep(2)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
