"""This is a file that contains a warm-up coding example"""

def is_palindrome(input_str):
    """This function determines if a string is a palindrom and prints the input and whether
     or not it passes the Boolean test of is or is not a palindrome"""
    #lower the string
    input_str_low = input_str.lower()
    #Reverse the string
    reverse_str = input_str_low[::-1]
    if input_str_low == reverse_str:
        print ("[" + input_str + "] is a Palindrome!")
    else:
        print ("[" + input_str + "] is not a Palindrome!")
    return

is_palindrome("The wicked witch of the West")
is_palindrome("Ananas sananA")
is_palindrome("Ananas sanana")
