""" This is the third in the LinkedIn warm-up exercises."""

def sort_string(string):
    """This function is intended to split a space delimited string, organize the words 
    alphabetically and return the sorted list of words in the original string."""
    string = 'The rain in Spain falls mainly on the plain.'
    print(string)
    string_list = string.split()
    print (type(string_list))
    string_list.sort()
    print(string_list)

sort_string('The rain in Spain falls mainly on the plain.')
