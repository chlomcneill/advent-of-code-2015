f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day5/Day5input.txt","r")
strings = f.readlines()
f.close()
strings = [i[:-1] for i in strings]

def find_pairs_of_letters(string):
    pairs_of_letters = []
    i = 0
    while i < (len(string)-1):
        pairs_of_letters.append(string[i] + string[i+1])
        i += 1
    return pairs_of_letters

def remove_overlapping_pairs(string):
    pairs = find_pairs_of_letters(string)
    i = 0
    while i < (len(pairs)-1):
        if pairs[i][0] == pairs[i][1] and pairs[i] == pairs[i+1]:
            del pairs[i+1]
        i += 1
    return pairs

def pair_appears_twice_check(string):
    pairs = remove_overlapping_pairs(string)
    count = 0
    for pair in pairs:
        if pairs.count(pair) > 1:
            count += 1
    if count > 0:
        return True
    else: 
        return False

def letter_repeat_around_diff_letter_check(string):
    count = 0
    i = 0
    while i < (len(string)-2):
        if string[i] == string[i+2]:
            count += 1
        i += 1
    if count > 0:
        return True
    else:
        return False

def nice_string_check(string):
    if pair_appears_twice_check(string) == True and letter_repeat_around_diff_letter_check(string) == True:
        return True
    else:
        return False

def how_many_strings_are_nice():
    nice_strings = []
    for string in strings:
        if nice_string_check(string) == True:
            nice_strings.append(string)
    return len(nice_strings)

print(how_many_strings_are_nice())


