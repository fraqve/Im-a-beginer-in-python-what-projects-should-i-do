
import random

lifes = 3
word_list = ["pro", "dog", "brother", "sister", "mother", "father", "game"]
random_word = random.choice(word_list)

print("Welcome to Hangman")
print()


l = []
for i in range(0,len(random_word)-2):
    l.append("_")

l.insert(0,random_word[0])
l.append(random_word[-1])

print(" ".join(l))

print()
print("Guess the word")
not_guessed_letters = len(random_word)-2
while not_guessed_letters != 0:
    answer = input("Type a letter: ")

    if answer in random_word:
        index = random_word.index(answer)
        not_guessed_letters -= 1
    else:
        print("wrong")
        lifes -= 1

    if lifes == 0:
        print("You lost")
        break

    print()
    print()

    del l[index]
    l.insert(index,random_word[index])



    print(" ".join(l))

