#Jeux motus en python

Ce programme python est inspiré du jeux télévisé motus, le principe est simple un mot est généré de manière aléatoire par le programme, l’utilisateur doit trouver le mot en 6 tentatives, l’utilisateur propose un mot, si une lettre est correcte et se trouve à la bonne place le programme l’affiche sinon le programme affiche un . pour les consonne et un * pour les voyelles.
si l’utilisateur échoue un message lui indique le mot qui été à trouver et lui propose de recommencer.

##Description des fichiers
###main.py
Ce fichier est le fichier principale du programme


###functions.py
ce fichier comporte toutes les fonctions nécessaires au programme


##Installation du projet

###Cloner le projet
git clone https://github.com/vincentmartin84/motus_python

###Vérifier que Python3 est installé
python --version

###Créer un environnement virtuel Python
python3 -m venv env

###Activer l'environnement virtuel
source env/bin/activate

###Importer les bibliothèques
pip install -r requirements.txt

###Lancer le programme
python3 main.py

