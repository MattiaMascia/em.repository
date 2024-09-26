# Creare 2 script:
# 1) genera 5 numeri casuali e li salva in un file;
# 2) Se l'utente avrà indovinato 2 numeri avrà vinto, 
# altrimenti potrà arrendersi o ritentare per altri 3 tentativi
# write 2 scripts:
# 1) generate 5 random numbers and save them in a file
# 2) game where the user should guess at least 2 of these numbers; if they lose, they can try again 3 more times or decide to give up at any time

import random

def rng(count,path):  # writes a csv file with the list of numbers
    truth = random.sample(range(1,11),count)
    truth = [str(element) for element in truth]
    truth_csv = ','.join(truth)
    with open(path,'w') as my_file:
        my_file.write(truth_csv)

def convert_file_to_list(file_path):  # outputs a list of integers from the csv file
    with open(file_path,'r') as my_file:
        content = my_file.read()
        string_list = content.split(',')
        return [int(element) for element in string_list]

def guessing_game(numbers_sampled = 5, lives = 4):
    rng(numbers_sampled,'09-12/rng.txt')
    true_list = convert_file_to_list('09-12/rng.txt')
    guessed_numbers = []
    while lives>0 and len(guessed_numbers)<2:
        guess = int(input("Type an integer between 1 and 10 (included):\n"))
        if guess in true_list:
            print("Correct")
            guessed_numbers.append(guess)
            true_list.remove(guess)
        else:
            print("Wrong")
            lives -= 1
        if lives == 0:
            print("You lost")
            exit()
        if len(guessed_numbers)==2:
            print("You won")
            exit()
        if int(input("Would you like to continue?\n    1) No\n    2) Yes\n"))-1:
            continue
        else:
            exit()

guessing_game()
