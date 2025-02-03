import requests

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
        user_word= input("Saisir un mot : ")
        if not user_word or not user_word.isalpha():
            print("La Saisie est incorrecte!")
            continue
        return user_word

def compatible_letters(random_word, user_word):
    voyelles = ("a","e","i","o","u","y")
    for l in random_word:
        #print(l)
        for c in user_word:
            #print(c)

            if c == l :
                print(c)