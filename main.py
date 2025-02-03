import requests

from functions import generate_word
from functions import word_input
from functions import compatible_letters
from functions import word_input
from functions import remove_accents

def game():
    random_word = remove_accents(generate_word())
    print(random_word)

    x = 1
    while x < 4:
        print(f"essai {x}")
        user_word = word_input()

        if random_word == user_word:
            print(f"Bravo vous avez trouvé le mot {random_word}")
            break

        compatible_letters(random_word, user_word)
        print()
        x = x + 1

    if random_word != user_word:
        print(f"Désolé, vous n'avez pas trouvé le mot. Le mot était : {random_word}")


game()