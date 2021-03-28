#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-9-19
#rclamb27@cus.fullerton.edu
"""Takes string and ethier cipher or deciphers it using the Vigenere cipher"""
import sys
def cypher(code_word, str_word):
    """Takes the word and cyphers it based on the code word"""
    answer = ''
    code_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cindex = 0
    windex = 0
    #pylint says unecessary comprehension but it wouldn't work withought it
    universal = [c for c in (chr(i) for i in range(0, 127))]
    word_int = [i for i in str_word]
    code_int = [i for i in code_word]
    for i in code_int:
        code_int[cindex] = code_x.index(i.upper())
        cindex += 1
    cindex = 0
    for i in word_int:
        if i.upper() not in code_x:
            word_int[windex] = universal.index(i)
        else:
            word_int[windex] = code_x.index(i.upper())
        windex += 1
    windex = 0
    while windex != len(word_int):
        if word_int[windex] < 32:
            calc = word_int[windex] + code_int[cindex]
            if calc > 26:
                calc = calc - 26
            if str_word[windex].isupper():
                answer += code_x[calc]
            else:
                answer += code_x[calc].lower()
        else:
            calc = word_int[windex] + code_int[cindex]
            answer += universal[calc]
        cindex += 1
        windex += 1
        if cindex == len(code_int):
            cindex = 0
    return answer

def decipher(code_word, str_word):
    """Takes the word and cyphers it based on the code word"""
    answer = ''
    code_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cindex = 0
    windex = 0
    #pylint says unecessary comprehension but it wouldn't work withought it
    universal = [c for c in (chr(i) for i in range(0, 127))]
    word_int = [i for i in str_word]
    code_int = [i for i in code_word]
    for i in code_int:
        code_int[cindex] = code_x.index(i.upper())
        cindex += 1
    cindex = 0
    for i in word_int:
        if i.upper() not in code_x:
            word_int[windex] = universal.index(i)
        else:
            word_int[windex] = code_x.index(i.upper())
        windex += 1
    windex = 0
    while windex != len(word_int):
        if word_int[windex] < 32:
            calc = word_int[windex] - code_int[cindex]
            if calc < 0:
                calc = calc + 26
            if str_word[windex].isupper():
                answer += code_x[calc]
            else:
                answer += code_x[calc].lower()
        else:
            calc = word_int[windex] - code_int[cindex]
            answer += universal[calc]
        cindex += 1
        windex += 1
        if cindex == len(code_int):
            cindex = 0
    return answer

def main():
    """Takes arguments and conducts the Vigenere cipher"""
    if len(sys.argv) < 4:
        print('Not enough arguments to cipher or decipher. Need a total of 3.')
        sys.exit()
    c_or_d = sys.argv[1]
    code_word = sys.argv[2]
    str_word = sys.argv[3]
    if not c_or_d in ('cypher', 'decipher'):
        print('Command {} was not understood.'.format(c_or_d))
        sys.exit()
    if c_or_d == 'cypher':
        print(cypher(code_word, str_word))
    else:
        print(decipher(code_word, str_word))

if __name__ == '__main__':
    main()
