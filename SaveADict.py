""" Yet another LinkedIn Learning coding warm-up"""

import json
import os.path

def create_dict():
    """This function writes the contents to the user input file path and file name."""
    contents = {'one':1, 'two':2, 'three':3}
    print(type(contents))
    print("Please enter the destination file path and name : ") #\n<For example C:\Users\User1\myfile.txt>")
    file_name = input()
    file1 = open(file_name, "w")
    with open(file_name,'w') as file1: #This saves the file as a string in the file path
      file1.write(str(contents))
    file1.close()
    return


def retrieve_object():
    """ This function currently opens the file and returns the text file as a string and then converts it to a dictionary. """
    print("Please enter the file path and name of the dictionary file to open:")
    file_name = input("(opening files that are not formatted as dictionaries will cause errors): ")
    file2 = open(file_name, "r")
    file2_string = file2.read()
    file2.close()
    print("This is the string read from file: " + file2_string)
    new_dict = eval(file2_string) #If this isn't a dictionary, this will throw errors.
    #print("This is the results of the eval")
    #print(type(new_dict))
    print(new_dict)
    return

create_dict()
retrieve_object()
