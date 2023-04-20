def is palindrome
    #Accept input text
    string = input("Enter a string to test if it is a palindrome: ")
    #Reverse the string
    reverse_string = string[::-1]
    if string == reverse_string
        print "Is a Palindrome!"
    else:   
        print "Is not a Palindrome!"