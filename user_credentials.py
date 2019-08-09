#!/usr/bin/env python
# Python script to create new user credentials
import sys
import fileinput
import time
import os
from ansible.playbook import Playbook
from shutil import copyfile

def main(arguments):

    username = raw_input("Enter user name which need to be created\n")
    home = raw_input("Enter home directory\n")
    user_id = raw_input("Enter user ID\n")
    group_id = raw_input("Enter primary group name or group id\n")
    sgroup_id = raw_input("Enter secondary group name separated by , if there are multiple secondary groups\n")
    comments = raw_input("Enter comments for user\n")
    playbook_path = "/home/thor/Public/Atom_projects/automatisation_tool/user_creation_with_server.yml"
    playbook_final_path = "/home/thor/Public/Atom_projects/automatisation_tool/user_creation_final.yml"

    copyfile(playbook_path, playbook_final_path)
    for line in fileinput.input(playbook_final_path, inplace=True):
        line = line.rstrip()
        if "username_var" in line:
            line = line.replace('username_var', username)
        if "hme_var" in line:
            line = line.replace('hme_var', home)
        if "userid_var" in line:
            line = line.replace('userid_var', user_id)
        if "pgrp_var" in line:
            line = line.replace('pgrp_var', group_id)
        if "sgrp_var" in line:
            line = line.replace('sgrp_var', sgroup_id)
        if "comments_var" in line:
            line = line.replace('comments_var', comments)
        print line

    ansible_command = "ansible-playbook user_creation_final.yml -K -vvv"
    os.system(ansible_command)
    time.sleep(2)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
