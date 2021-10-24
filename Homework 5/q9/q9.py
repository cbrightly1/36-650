# q9

def palindrome(string):
    if len(string) < 2: # stop condition 1
        return True
    elif string[0] != string[-1]: # stop condition 2
        return False
    return palindrome(string[1:-1]) # decreases the length of the string by one on each side each time
    
print(palindrome("kayak"))
print(palindrome("hello"))
