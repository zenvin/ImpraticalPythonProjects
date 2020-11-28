## This program will take a word and turn it into pig latin.
import sys
import random

##get input

VOWELS = 'aeiouy'

while True:
    word = input("Type a word and get its pig Latin translation: ")

    if word[0] in VOWELS:
        pig_Latin = word + 'way'
    else:
        pig_Latin = word[1:] + word[0] + 'ay'
    print()
    print("{}".format(pig_Latin), file=sys.stderr)

    try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
    if try_again.lower() == "n":
        sys.exit()
## if input start with a vowel do the following:
##      add "way" to the end of the word

## else (input starts with a consonant) do the following:
##      remove the constant (cut?)
##      add it to the end of the input (append?)
##      add "ay" after the constant
##      perhaps we can add consonant and "ay" in one line

##  elseif (if the input is a number or begins with a symbol)
##      print("We need a leter")
