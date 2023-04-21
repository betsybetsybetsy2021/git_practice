""" This is the third in the LinkedIn warm-up exercises."""

#import re

def sort_string(string):
    """This function is intended to split a space delimited string, organize the words 
    alphabetically and return the case insensitive sorted list of words in a joined string."""
    string_list = []
    string_list = string.split()
    string_list.sort(key = lambda x: x.lower())
    #new = re.split(r'\s', string) #This uses regular expressions
    # but I'm not how to IgnoreCase to sort without changing
    print(" ".join(string_list)) #This rejoins the strings

#The solution provided uses key=str.casefold but I am not sure why that doesn't lowercase the split string
sort_string('The rain in Spain falls mainly on the plain.')
