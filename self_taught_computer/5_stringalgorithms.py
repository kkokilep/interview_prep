import string

def is_anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if(sorted(s1) == sorted(s2)):
        return True
    else:
        return False

def is_palindrome(s1):
    if(s1.lower() == s1[::-1].lower()):
        return True
    return False

def last_digit(s1):

    return [c for c in s1 if c.isdigit()][-1]

def cipher(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt
