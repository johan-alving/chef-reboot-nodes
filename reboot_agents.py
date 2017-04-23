import subprocess
import os
import sys
import argparse
import platform

CHEF_REPO = "C:\\Users\\a-johana\\Workspace\\internal_cifw_tools\\chef"


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wildcard")
    parser.add_argument("--all", action="store_true")
    return parser.parse_args()

def reboot_agents(wildcard):
    if platform.system() == "Windows":
        subprocess.call("knife exec -E \"nodes.find(\'name:*{}*\') {{ |n| puts n.name }}\"".format(wildcard), shell=True, cwd=CHEF_REPO)
    elif platform.system() == "Darwin":
        subprocess.call("knife exec -E 'nodes.find(\"name:{}\") {{ |n| puts n.name }}'".format(wildcard), shell=True, cwd=CHEF_REPO)

def main():
    args = parse_arguments()
    if args.all:    
        while True:
            user_input = raw_input("Are you sure you want to reboot all agents? (y/n) ")
            if user_input == 'y':
                print("The following agents will be rebooted:")
                reboot_agents("*")
                break
            elif user_input == 'n':
                break
    elif args.wildcard:
        print("The following agents will be rebooted:")
        reboot_agents(args.wildcard)

if __name__ == '__main__':
    main()
