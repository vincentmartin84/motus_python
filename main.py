import requests

from functions import generate_word
from functions import word_input
from functions import compatible_letters
from functions import word_input
from functions import remove_accents

random_word= remove_accents(generate_word())
print(random_word)



x = 0
while x<8:
    user_word = word_input()

    if random_word == user_word:
        print(f"Bravo vous avez trouvé le mot {random_word}")
        break

    compatible_letters(random_word,user_word)
    print()


