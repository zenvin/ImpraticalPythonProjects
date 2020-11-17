## This program will take a word and turn it into pig latin.
import sys
import random

##get input
non_pig_word = str(input("Please enter a word to be converted into pig latin:"))
new_non_pig_word = non_pig_word.split()
print(new_non_pig_word)
## if input start with a vowel do the following:
##      add "way" to the end of the word

## else (input starts with a consonant) do the following:
##      remove the constant (cut?)
##      add it to the end of the input (append?)
##      add "ay" after the constant
##      perhaps we can add consonant and "ay" in one line

##  elseif (if the input is a number or begins with a symbol)
##      print("We need a leter")
