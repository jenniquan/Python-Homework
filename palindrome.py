statement = raw_input ('Enter a word: ')

if statement [::1] == statement [::-1]:
    print statement, " is a palindrome"
elif statement [::1] != statement [::-1]:
    print statement, " is not a palindrome"
    
