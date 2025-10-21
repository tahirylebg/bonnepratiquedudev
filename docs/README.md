# bonnepratiquedudev
# 📚 Bookstore API – Projet Bonne Pratique de Développement

Présentation du projet : 

Ce projet a pour objectif de concevoir une **API REST moderne** permettant de gérer une **boutique de livres** :  
- Consultation du catalogue  
- Ajout de nouveaux livres  
- Création et gestion des commandes  

L’accent a été mis sur les **bonnes pratiques de développement** :  
architecture modulaire, gestion des erreurs, logging structuré, tests automatisés et documentation claire.

---

## 🏗️ Architecture du projet

<<<<<<< HEAD
<img width="700" height="833" alt="image" src="https://github.com/user-attachments/assets/73ebe73b-da64-4b24-a534-d6d5d61f422f" />


## L'installation de notre projet et l'execution est le suivant : 
=======
bookstore_api/
├── app/
│   ├── main.py                     # Point d'entrée de l'application FastAPI
│   ├── api/                        # Routes et endpoints
│   │   ├── books.py                # Routes /books (GET, POST, GET/{id})
│   │   └── orders.py               # Routes /orders (POST)
│   │
│   ├── services/                   # Logique métier
│   │   ├── book_service.py         # Gestion des livres (CRUD)
│   │   └── order_service.py        # Gestion des commandes
│   │
│   ├── models/                     # Schémas de données (Pydantic)
│   │   ├── book_model.py
│   │   └── order_model.py
│   │
│   ├── database/                   # Simulation d'une base de données locale (JSON)
│   │   └── db.py
│   │
│   ├── core/                       # Cœur technique (logs, erreurs, utilitaires)
│   │   ├── logging_config.py
│   │   ├── errors.py
│   │   └── utils.py
│   │
│   ├── middlewares/                # Middleware personnalisés
│   │   ├── request_logger.py
│   │   └── error_handler.py
│   │
│   └── __init__.py
│
├── tests/                          # Tests unitaires et d’intégration
│   ├── test_books.py
│   ├── test_orders.py
│   └── conftest.py
│
├── logs/
│   ├── app.log                     # Logs applicatifs
│   └── error.log                   # Logs d’erreurs
│
├── docs/
│   ├── README.md                   # Documentation projet
│   ├── RUNBOOK.md                  # Procédures de debug & rollback
│   └── ARCHITECTURE.md             # Décisions techniques & schéma logique
│

L'installation de notre projet et l'execution est le suivant : 
>>>>>>> 442ce5b (chore(project): finalisation du projet et préparation à la soutenance)
- On clone notre projet
- cd bookstore_api

- On crée un environnement virtuelle comme ceci : python -m venv venv
- On l'active : .\venv\Scripts\activate
- Nous lancons notre API : uvicorn app.main:app --reload
<<<<<<< HEAD
- On clique sur le lien puis ont tape http://"le lien " 
- Pour la partie test on test avec cet commande : pytest -v

- Si on a déjà venv installé : on tape cmd et on reprends de .\venv\Scripts\


## Logging & gestion d’erreurs : 

Loguru pour un logging clair et structuré (fichier logs/app.log)
Middleware personnalisé pour enregistrer toutes les requêtes
Gestion d’erreurs centralisée via error_handler.py
Exceptions typées (ex: StockError) pour une meilleure traçabilité
├── requirements.txt                # Dépendances du projet
└── .gitignore


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
- Pour la partie test on test avec cet commande : pytest -v

Logging & gestion d’erreurs : 

Loguru pour un logging clair et structuré (f
>>>>>>> 442ce5b (chore(project): finalisation du projet et préparation à la soutenance)
