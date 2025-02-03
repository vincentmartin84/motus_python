import requests
import unicodedata

def remove_accents(word):
    return ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')



def generate_word():
    response = requests.get("https://trouve-mot.fr/api/random")

    # Vérification de la réussite de la requête
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

    # Parcourir chaque lettre des deux mots
    for l, c in zip(random_word, user_word):
        if c == l:
            print(c, end='')
        else:
            print(".", end='')


