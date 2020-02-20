def liststring(lst):
    string=' '
    for i in lst:
        string += i
        string += ' '
    return  string    



vowel = "aeiou"


import random

repeative_check=[]

HANGMAN  =('''
------------
|         |''','''


------------
|         |         
|          O''','''


------------
|         | 
|          O 
|         / ''','''


------------
|         | 
|          O 
|         / |''','''

------------
|         | 
|          O 
|         / | 
|          | ''','''


------------
|         |
|          O 
|         / |
|          |
|         /  
|
|            ''','''


------------
|         |
|          O 
|         / |
|          |
|         / | 
|
|            '''
)


play_again=True
while play_again:
    with open('words.txt') as f:
        list=[word for line in f for word in line.split()]


    secret_word=random.choice(list).lower()
  
    print('Welcome to the Hangman\nlet me tell you the rules of hangman\n1.You have six lifelines and 3 warnings')
    
    print('2.one wrong guess is equal to loss of one lifeline')
    print("3.one letter can be guessed once if you enter the letter you already guessed that results in loss of one warning")
    print("4.YOU HAVE TO ENTER CORRECT INPUT i.e (i) ONE LETTER AT TIME\n(ii)MUST ENTER AN ALPHABET")
    print("5.violation of rules will result in loss of one warning and if you run out of warning and still violates the rule you lose one attempt")
    
    print('You are all set to go')
    print('Wait.I m thinking of a word....')
    guess= None # player guess input
    guessed_letters=[] #we add all of the user guesses to this list
    blank_word=[] #replacing all of the letters of the chosen word with dashes
    for letter in secret_word:
        blank_word.append("_")
    attempts=6
    warnings=3
    count=0
    while attempts>0:

            if (attempts!=0 and "_" in blank_word):
                print(("\nYou have {} attempts remaining").format(attempts))
                print(("\nYou have {} warnings remaining").format(warnings))

            try:
                guess=str(input('\Please select a letter between A-Z')).lower()
            except:
                print('That is not valid input.Please try again')
                
                if warnings>0:
                        warnings-= 1
                else:
                    attempts-= 1
                
                print(("\nYou have {} warnings remaining").format(warnings))
                continue
            else:
                if not guess.isalpha():
                    print("That is not a letter please try again")
                    if warnings>0:
                        warnings-= 1
                        print(("\nYou have {} warnings remaining").format(warnings))
                    else:
                        attempts-= 1
                    
                    continue
                elif len(guess) > 1:
                    print("There are more than one letter please try again")
                    if warnings>0:
                        warnings-= 1
                    else:
                        attempts-= 1
                    print(("\nYou have {} warnings remaining").format(warnings)) 
                    continue
                elif  guess in guessed_letters:
                    print("Your Have already guessed that letter please try again")
                    if warnings>0:
                        warnings-= 1
                    else:
                        attempts-= 1
                    
                    print(("\nYou have {} warnings remaining").format(warnings))
                    continue
                else:
                    pass
                for i in range(len(secret_word)):
                    if secret_word[i]==guess:
                        blank_word[i]=guess



                if guess in secret_word and guess.isalpha() and guess not in repeative_check:
                    print("good guess:" +liststring(blank_word))
                    for i in range(len(secret_word)):
                        if secret_word[i]==guess:
                            repeative_check.append(guess)

                if guess not in secret_word and guess.isalpha() and guess in vowel:
                    print("Letter not in word"+liststring(blank_word))
                 
                    attempts-=2
                    print("2 attempts lost")
                if guess not in secret_word and guess.isalpha() and guess not in vowel:
                    print("Letter not in word"+liststring(blank_word))
                    print("You Have lost an attempt")

                    attempts-=1
                if guess not in secret_word  :
                    attempts-= 1
                    print(HANGMAN[(len(HANGMAN)  -  1)  -  attempts])


                if attempts == 0:
                    print("Sorry the game is over. The word was " + secret_word )
                    print("\n would you like to play again?")
                    response = input(">").lower()
                    if response not in ("yes","y"):
                        play_again = False
                        print("Thanks for playing Hangman")
                    break

                if "_" not in blank_word:
                    print(("\n CONGRATULATIONS! {} was the word").format(secret_word))
                    print("\n would you like to play again?")
                    response = input("> ").lower()
                    if response not in ("yes","y"):
                        play_again = False
                        print("Thanks for playing Hangman")
                    break








               





