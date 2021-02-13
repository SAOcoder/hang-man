print("Oh no! I think that dude needs help!")
print("We have to guess the secret word so that he can excape and not get eaten alive ")

number_of_lines = len(word)
print(f""" 
--------|
|     (⁰д⁰) "Please Help! I dont want to be eaten by the piranha!"
|      /|\   [{number_of_lines}]
|     _/ \_
|
|[≈ >-( ͡° ͜ʖ ͡°) ≈≈]
""")
  
word_1c = word
censored_word = [i.replace(i, '_') for i in word_1c]
print("\n", censored_word)
print("\n", list(word_1c))

guess_letter = input(f""" \n Aight, guess a letter: \n """)

from words import word_inventory
import random

#word = random.choice(word_inventory)
#print(word)

def game():
  word = "cat"
  word_status = " _ " * len(word)
  guessed_letters = []
  tries = 7

      
guess_letter = input(f""" \n Aight, guess a letter: \n """)
  print(word_status)

game()
#censored_word =  str(list(word)).replace(i,"_")
#for i in word:
  #if letter not in word:
    #print(censored_word)
  #if letter in word:
    #find(letter in word)
    #censored_word = censored_word


#censored = True
#while censored == True:
    #list(word)
    #for i in word:
        #censored_word = word.replace(i, "_")
    #print(censored_word)