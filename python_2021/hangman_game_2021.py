import random

# lista di parole
words_list = ["car"]

occurrences_char = list()
occurrences_index = list()

while True:
    word_to_guess = random.choice(words_list)
    word_len = len(word_to_guess)
    temp = ["c", "a", "r"]

    # tentativi
    attempts_remaining = 5
    attempts_correct = 0

    print("******************")
    print(f"Let's begin!. The word to guess has {word_len} letters.")
    #print(word_len * " _ ")
    underscore = word_len * "_"
    print(underscore)
    print("")
    print("******************")

    # crea una lista dei caratteri della parola
    l_word = list(word_to_guess)
    # print(l_word)

    while True:

        if attempts_remaining > 0:
            if attempts_correct < word_len:
                insert = input("Insert a character: ")

                if insert not in occurrences_char:
                    if insert in l_word:
                        occurrences_char.append(insert)
                        occurrences_index.append(l_word.index(insert))
                        attempts_correct += 1

                for char in temp:
                    if char in occurrences_char:
                        underscore = underscore[:temp.index(char)] + char + underscore[temp.index(char) + 1:]


                # Printing informations
                # Occurrences
                print("Occurrences characters are: ", occurrences_char)
                occurrences_index.sort()
                #print("Occurrences index are: ", occurrences_index)

                # Attempts
                print("Attempts correct: ", attempts_correct)
                print("Attempts remaining: ", attempts_remaining)

                print("Word in completion is: ", underscore)
                print("******************")

                attempts_remaining -= 1
            else:
                print("Good boy, my man! You win!")
                break
        else:
            print("Sorry, game's over!")
            # break the inner cicle
            break
    # break the outer cicle
    break

###################################################################################################

# # References
# https://www.tutorialgateway.org/python-program-to-find-all-occurrence-of-a-character-in-a-string/