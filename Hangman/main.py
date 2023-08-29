import random
print("""H A N G M A N""")
print()

turns = 8
lost =0
won=0

while True:
    correct =["python", "java", "swift", "javascript"]
    ans = random.choice(correct)
    guesses = ''
    flag = ''
    ask = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if ask == "play":
         while turns > 0:    
            def check():
                 if word_mask == ans:
                     print(f"You guessed the word {ans}!")
                     print("You survived!")
        
            word_mask = "".join(char if char in guesses else "-" for char in ans)    
            print(word_mask)    
            check()
            if word_mask == ans:
                won += 1
                break
            guess = input("Input a letter: ") 
            if len(guess)>1 or guess == "":
                print("Please, input a single letter.")
                print()
            elif guess.islower() == True:
                if guess in flag:
                    print("You've already guessed this letter.")
                    print()
                elif guess not in ans: 
                    print("That letter doesn't appear in the word") 
                    flag += guess          
                    turns -= 1
                    print()
            
                else:
                    guesses += guess
                    print()
            elif guess.islower() == False or guess.isalpha() == False:        
                print("Please, enter a lowercase letter from the English alphabet.")
                print()   
            if guess in word_mask and guess != "":
                print("You've already guessed this letter.")
                print()
        
            if turns == 0:
                lost +=1
                print()
                print("You lost!")
        
    elif ask == "results":
        print(f"You won: {won} times.")
        print(f"You lost: {lost} times.")
    else:
        break    
                