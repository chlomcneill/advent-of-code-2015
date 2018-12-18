f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day4/Day4input.txt","r")
strings = f.readlines()
f.close()

def vowel_check(string):
    vowels = 0
    for letter in string:
        if letter == 'a' or letter == 'i' or letter == 'e' or letter == 'o' or letter == 'u':
            vowels += 1
    if vowels >= 3:
        return True
    else:
        return False

# print(vowel_check('whrf'))

def double_letter_check(string):
    double_letters = 0
    prev = ''
    for letter in string:
        if letter == prev:
            double_letters += 1
        prev = letter
    if double_letters > 0:
        return True
    else:
        return False
    
# print(double_letter_check('rthd'))

def no_bad_substring_check(string):
    if 'ab' not in string and 'cd' not in string and 'pq' not in string and 'xy' not in string:
        return True
    else:
        return False

# print(no_bad_substring_check('bwecdfoiapqhg'))

def nice_string_check(string):
    if vowel_check(string) == True and double_letter_check(string) == True and no_bad_substring_check(string) == True:
        return True
    else:
        return False

def how_many_strings_are_nice():
    nice_strings = 0
    for string in strings:
        if nice_string_check(string) == True:
            nice_strings += 1
    return nice_strings

print(how_many_strings_are_nice())


