""" This is the third in the LinkedIn warm-up exercises."""

#import re

def sort_string(string):
    """This function is intended to split a space delimited string, organize the words 
    alphabetically and return the sorted list of words in the original string."""
    string_list = []
    string_list = string.split()
    string_list.sort(key = lambda x: x.lower())
    #new = re.split(r'\s', string) #This uses regular expressions
    # but I'm not how to IgnoreCase to sort without changing
    print(string_list)


sort_string('The rain in Spain falls mainly on the plain.')
