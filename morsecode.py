dictionary = {
'A': '.-',
'B':   '-...',
'C':   '-.-.',
'D':   '-..',
'E':  '.',
'F':  '..-.',
'G':   '--.',
'H':   '....',
'I':   '..',
'J':   '.---',
'K':  '-.-',
'L':   '.-..',
'M':  '--',
'N':   '-.',
'O':   '---',
'P':   '.--.',
'Q':   '--.-',
'R':   '.-.',
'S':   '...',
'T':   '-',
'U':   '..-',
'V':   '...-',
'W':   '.--',
'X':   '-..-',
'Y':   '-.--',
'Z':   '--..',
' ': '  ',}

on = True
print('Welcome to the Morse Code Translator!\n')
while on:
    given_word = input("Please type the word you would like translated to Morse Code here. If done, type end: ").upper()
    letter_list = [x for x in given_word]

    morse_word = ""

    for x in range(len(letter_list)):
        new_letter = dictionary[letter_list[x]]
        morse_word += f'{new_letter} '
    if given_word == 'END':
        on = False
    else:
        print(f"\nYou're word in Morse code is: {morse_word}\n")

