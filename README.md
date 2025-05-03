# Portfolio Backend API - Django & JWT Authentication

Une API REST robuste et sécurisée construite avec Django et Django REST Framework (DRF), conçue pour alimenter un portfolio de développeur. Elle gère les opérations CRUD sur les projets, les compétences, le profil, ainsi que la réception de messages de contact, le tout protégé par une authentification JWT.

## 🚀 Fonctionnalités

- Authentification via JWT (connexion / inscription / actualisation de token)
- Gestion CRUD des :
  - Projets
  - Compétences
  - Profil de l’utilisateur
  - Messages de contact
- Validation des données côté serveur
- Intégration avec un frontend (Next.js)

## 🛠️ Technologies utilisées

- Django 4+
- Django REST Framework
- djangorestframework-simplejwt (pour JWT)
- SQLite (ou PostgreSQL en production)
- CORS headers

## 📁 Structure du projet

portfolio-backend/
├── manage.py
├── requirements.txt
├── portfolio/ # Configuration principale Django
│ └── settings.py
├── api/ # Application principale
│ ├── models.py # Profile, Project, Skill, ContactSubmission
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── permissions.py
└── ...

markdown
Copier
Modifier

## 🔐 Authentification JWT

- `/api/token/` – Obtenir un token d'accès et de rafraîchissement
- `/api/token/refresh/` – Rafraîchir le token
- Toutes les routes d’administration (CRUD) sont protégées par JWT

## 📬 Endpoints principaux

| Méthode | Endpoint                | Description                         |
|---------|-------------------------|-------------------------------------|
| GET     | `/api/projects/`        | Liste des projets                   |
| POST    | `/api/projects/`        | Ajouter un projet (auth requis)     |
| PUT     | `/api/projects/<id>/`   | Modifier un projet (auth requis)    |
| DELETE  | `/api/projects/<id>/`   | Supprimer un projet (auth requis)   |
| GET     | `/api/skills/`          | Liste des compétences               |
| GET     | `/api/profile/`         | Détails du profil                   |
| POST    | `/api/contact/`         | Envoyer un message de contact       |

## 🧪 Installation & utilisation

1. **Cloner le repo :**
   ```bash
   git clone https://github.com/<votre-username>/portfolio-backend.git
   cd portfolio-backend
