#!/usr/bin/python
# Script to check load, memory and disk usage in linux
import os
import subprocess 
print "Choose from the options below:\n";
print "1. I will print load on server"
print "2. I will print memory usage on server"
print "3. I will print df output"
print "1 or 2 or 3"
choice = raw_input("Enter Choice:\n")
choice = int(choice)
if ( choice == 1 ) :
    print "Executing w ..."
    subprocess.call(['w'])
if ( choice == 2) :
    print "Executing free ..."
    subprocess.call(['free', '-m'])
if ( choice == 3 ) :
    print "Executing df"
    subprocess.call(['df', '-h'])
    
raw_input ("Press enter to bid adieu")
print "Bye"
