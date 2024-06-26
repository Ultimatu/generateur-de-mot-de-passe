# Générateur Automatique de Mots de Passe

Ce projet est un générateur de mots de passe utilisant Python et Tkinter pour créer une interface utilisateur graphique (GUI). Il permet de générer des mots de passe de différentes forces et de les copier automatiquement dans le presse-papiers. Les mots de passe générés sont également enregistrés dans un fichier texte avec un horodatage.

## Fonctionnalités

- Génération de mots de passe avec des caractères minuscules, majuscules, des chiffres et des caractères spéciaux.
- Trois niveaux de sécurité : faible, moyen et super_pro.
- Taille personnalisable des mots de passe entre 8 et 32 caractères.
- Copie automatique du mot de passe dans le presse-papiers.
- Sauvegarde des mots de passe générés dans un fichier texte avec la date et l'heure de création.

## Installation

### Prérequis

- Python 3.x
- Tkinter (généralement inclus avec Python)
- `pyperclip` pour la gestion du presse-papiers

### Étapes d'installation
   ```sh
   #cloner le repo
   git clone <URL-du-dépôt>
   
   cd <URL-du-dépôt>
   
   #Installer les dépendances à partir du fichier requirements.txt. 
   pip install -r requirements.txt

   python password_generator.py
```


