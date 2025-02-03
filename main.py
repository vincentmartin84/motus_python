import requests

from functions import generate_word
from functions import word_input
from functions import compatible_letters
word= generate_word()
print(word)


w= word_input()
print(w)
compatible_letters(word,w)