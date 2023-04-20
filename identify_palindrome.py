"""This is a file that contains a warm-up coding example"""

def is_palindrome(input_str):
    """This function determines if a string is a palindrom and prints the input and whether
     or not it passes the Boolean test of is or is not a palindrome"""
    #Reverse the string
    #input_str = input("Please enter a string:")
    #print(input_str)
    #print(input_str[::-1])
    reverse_str = input_str[::-1]
    if input_str == reverse_str:
        print ("[" + input_str + "] is a Palindrome!")
    else:
        print ("[" + input_str + "] is not a Palindrome!")
    return

is_palindrome("The wicked witch of the West")
is_palindrome("Ananas sananA")
is_palindrome("Ananas sanana")
