from replit import clear 

  

from hangman_art import stages,logo 

print(logo) 

  

from hangman_words import word_list 

import random 

  

chosen_word = random.choice(word_list) 

length = len(chosen_word) 

#print(type(chosen_word)) 

  

#testing code 

print(f"The chosen word is {chosen_word} \n") 

  

#create blanks 

blanks = []    

for i in range(length): 

  blanks += "_" 

  

life = 6 

end_of_game = False 

  

while not end_of_game: 

  guess = input("Guess a letter: ").lower() 

  #print(guess) 

  clear() 

  

  #check if guessed letter is in word 

  for i in range(length):   

    if guess == chosen_word[i]: 

      blanks[i] = guess 

  

  #check if guess is wrong 

  if guess not in chosen_word: 

    print(f"You guessed {guess}, that's not in the word. You lose a life.") 

  

    life -= 1 

    if life == 0: 

        print("You lose.") 

  

  print(stages[life]) 

   

  if life == 0: 

    end_of_game = True 

    print("you lose")    #game over if life zero 

  else: 

    print(f"{' '.join(blanks)}") 

    print("\n") 

   

  

  if "_" not in blanks: #imp 

    end_of_game = True 

    print("You win")    #game over if blanks over 

                    

  

     

  

  

     

       

  

  

  

 
