""" Yet another LinkedIn Learning coding warm-up"""

import json
import os.path

def create_dict():
    contents = {'one':1, 'two':2, 'three':3}
    print(type(contents))
    print("Please enter the destination file path and name : ") #\n<For example C:\Users\User1\myfile.txt>")
    file_name = input()
    file1 = open(file_name, "w")
    with open(file_name,'w') as file1: #This saves the file as a string in the file path
      file1.write(str(contents))
    file1.close()
    return


def sort_string():
    return

create_dict()
