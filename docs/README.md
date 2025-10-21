# bonnepratiquedudev
# 📚 Bookstore API – Projet Bonne Pratique de Développement

Présentation du projet : 

Ce projet a pour objectif de concevoir une **API REST moderne** permettant de simuler la gestion d'une **boutique de livres** :  
- Consultation du catalogue  
- Ajout de nouveaux livres  
- Création et gestion des commandes  

L’accent a été mis sur les **bonnes pratiques de développement** :  
architecture modulaire, gestion des erreurs, logging structuré, tests automatisés et documentation claire car c'est le principe de la matière .

---

## 🏗️ Architecture du projet

<img width="700" height="833" alt="image" src="https://github.com/user-attachments/assets/73ebe73b-da64-4b24-a534-d6d5d61f422f" />


## L'installation de notre projet et l'execution est le suivant : 

- On clone notre projet
- cd bookstore_api

- On crée un environnement virtuelle comme ceci : python -m venv venv
- On l'active : .\venv\Scripts\activate
- Nous lancons notre API : uvicorn app.main:app --reload
- On clique sur le lien puis ont tape http://"le lien " 
- Pour la partie test on test avec cet commande : pytest -v

- Si on a déjà venv installé : on tape cmd et on reprends a partir de .\venv\Scripts\


## Logging & gestion d’erreurs : 

-Loguru pour un logging clair et structuré (fichier logs/app.log)

-Middleware personnalisé pour enregistrer toutes les requêtes

-Gestion d’erreurs centralisée via error_handler.py

##

## Bonne pratique qu'on a respecté :
✅ Convention de commits Conventional Commits (feat, fix, chore, etc.)
✅ Architecture modulaire et scalable
✅ Tests automatisés et reproductibles
✅ Documentation claire et complète
✅ Logs centralisés et gestion d’erreurs propre

Language de programmation utilisé : python 



Auteurs : 
Tahiry Ramambazafy
Lorenzo Sinigaglia
Thomas Peysabures
=======


