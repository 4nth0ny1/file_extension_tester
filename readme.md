# Readme

This is a file extension testing script that I use for capture the flag and tryhackme rooms. I created this specifically for the Vulnerversity room to figure out what file extensions where allowed in the input. 

The goal of the CTF was to get a reverse shell by submitting a file to the CTF's server. We did not know what file extensions would make it through, so I made this script to test them out. The CTF gave 5 options, and explained how to use Burp Suite Intruder to do this, but I felt it would be a good exercise to make a python script after watching John Hammond's walk through of the room. 

There he created a more basic version of this script, specifically for vulnerversity and I decided to add on to it by adding an argument parser and a larger file extension list. 

Credits are in the ape.py file at the top.  

filename extension list 
https://gist.github.com/securifera/e7eed730cbe1ce43d0c29d7cd2d582f4

### DO NOT USE THIS FOR ANY ILLEGAL REASONS. THIS IS PURELY INTENDED FOR EDUCATIONAL PURPOSES AND FOR LEGAL PENTESTING. 

## Installation and Usage 

git clone https://github.com/4nth0ny1/file_extension_tester.git
cd file_extension_tester

## Help
python ape.py -h 

I used the pentester monkey php reverse shell for Vulniversity on THM and copied it to the file_extension_tester directory for ease of use. 

https://github.com/pentestmonkey/php-reverse-shell

you can use whatever file you want, just change the value of the two variables old_filename and filename. 

## Example usage 

python ape.py -i 10.10.X.X:3333 -s /internal/index.php -e ./file_extension_list.txt -em "Extension not allowed" 

plus make a change the if not statement on line 44 to accomodate for the error message that is in the r.text when a file extension is not allowed. 


