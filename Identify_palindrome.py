def is_palindrome(input_str):
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