from xml.sax.handler import feature_string_interning

import requests
import unicodedata

def remove_accents(word):
    return ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')

def welcome():
    print("Bienvenue sur motus en version terminal! \n ")
    print("Ce jeux génère un mot aléatoire et il ne vous reste plus qu'a le deviner, vous n'avez que 8 chances! ")
    print("lorsque vous proposez un mot si une des lettres est bonne elle s'affiche \n sinon un . apparait à l'emplacement d'une consonne ou un * à l'emplacement d'une voyelle! \n")


def generate_word():
    response = requests.get("https://trouve-mot.fr/api/random")


    if response.status_code == 200:
        try:
            words = response.json()
            return words[0]['name']
        except KeyError:
            print("La clé 'name' n'est pas présente dans la réponse.")
        except ValueError:
            print("Erreur lors de la conversion de la réponse en JSON.")
    else:
        print(f"Erreur {response.status_code}: La requête n'a pas abouti.")



def word_input():
    while True:
        user_word= input("Saisir un mot : ").lower()
        if not user_word or not user_word.isalpha():
            print("La Saisie est incorrecte!")
            continue
        return user_word


def compatible_letters(random_word, user_word):
    voyelles = ("a", "e", "i", "o", "u", "y")


    if len(user_word) != len(random_word):
        print("Les mots doivent avoir la même longueur.")
        return


    for l, c in zip(random_word, user_word):
        if c == l:
            print(c, end='')
        elif l not in voyelles:
            print(".", end='')
        else:
            print("*", end='')

def game():
    voyelles = ("a", "e", "i", "o", "u", "y")
    random_word = remove_accents(generate_word())
    #print(random_word)
    print("Indice du mot à trouver : " + random_word[0], end='')
    for c in random_word[1:]:
        if c in voyelles:
            print("*", end='')
        else:
            print(".", end='')

    x = 1
    while x < 4:
        print(f"\n essai {x} \n ")
        user_word = word_input()

        if random_word == user_word:
            print(f"Bravo vous avez trouvé le mot {random_word}")
            break

        compatible_letters(random_word, user_word)
        print()
        x = x + 1

    if random_word != user_word:
        print(f"Désolé, vous n'avez pas trouvé le mot. Le mot était : {random_word}")



def retry():
    while True:
        retry = input("Voulez-vous rejouer ?  tapez oui/non  ").lower()

        if retry== "oui":
            game()
        elif retry == "non":
            break
        else:
            print("Saisie incorrecte! Tapez oui/non  ")