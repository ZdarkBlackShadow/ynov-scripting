# ynov-scripting

Ce dépôt regroupe l'ensemble des exercices et scripts réalisés dans le cadre de notre formation en Scripting Python.

L'objectif de ce projet est de démontrer la capacité de Python à interagir avec le système d'exploitation, le réseau et les protocoles de sécurité pour automatiser des tâches complexes.

## Qu'est-ce que le Scripting ?

Le scripting ne consiste pas seulement à développer des logiciels, mais à créer des outils qui pilotent d'autres programmes ou le système lui-même.

## Pourquoi le pratiquer ?

**Automatisation :** Remplacer des tâches manuelles répétitives par des processus instantanés et sans erreur.

**Administration Système (SysAdmin) :** Gérer des fichiers, des processus et des configurations serveur sans intervention humaine.

**Cybersécurité :** Créer ses propres outils d'audit, de pentest ou d'analyse réseau

**Interopérabilité :** Faire dialoguer différents systèmes entre eux (API, SSH, Sockets).

## Thèmes

Les scripts sont classés par thématiques, allant de la simple interaction système aux concepts avancés de réseau et de sécurité.

### Système & Environnement

*Maitrise de l'environnement d'exécution et interaction avec l'OS hôte.*

**Préparation (Ch. 1 & 15)** : Mise en place de l'environnement virtuel, vérification des dépendances et installation conditionnelle.

**Options de ligne de commande (Ch. 6)** : Création d'outils CLI robustes acceptant des arguments (via argparse ou sys.argv).

**Gestion des processus (Ch. 8)** : Lancement, surveillance et arrêt de programmes externes depuis Python.

**Fichiers temporaires (Ch. 3)** : Manipulation sécurisée de données volatiles.

**Interception des signaux (Ch. 7)** : Gestion propre des interruptions (ex: CTRL+C) pour éviter la corruption de données.

**Multiprocessing (Ch. 12)** : Optimisation des performances via l'exécution parallèle.

### Réseau & Communication

*Développement d'outils pour communiquer sur un réseau local ou internet.*

**SSH (Ch. 2)** : Automatisation de commandes sur des serveurs distants (via paramiko).

**Sockets (Ch. 5)** : Création d'architectures Client/Serveur bas niveau (TCP/UDP).

**Requêtes HTTP (Ch. 9)** : Interaction avec le web et les API (via requests).

**Emails (Ch. 13)** : Envoi automatisé de courriels (alertes, rapports) via SMTP.

**Adresse MAC (Ch. 26)** : Manipulation et spoofing d'adresses physiques pour l'anonymat ou les tests.

### Sécurité & Bas Niveau

*Compréhension des protocoles et analyse de sécurité (Red Teaming / Blue Teaming).*

**Dissection ICMP (Ch. 4)** : Analyse brute de paquets réseau (création d'un scanner type "Ping").

**Sniffing avec Scapy (Ch. 11)** : Interception et manipulation avancée de paquets réseau pour l'audit.

**Malware Showcase & Keylogger (Ch. 20 & 24)** : À but éducatif uniquement. Analyse du fonctionnement des logiciels malveillants (capture de frappe, persistance) pour mieux comprendre comment les détecter et s'en protéger.

### Monitoring

**Activity Report (Ch. 10)** : Génération de rapports d'état du système (CPU, RAM, Disque).

## Comment utiliser ce dépôt

Chaque dossier de chapitre contient un fichier README.md spécifique détaillant :

La consigne de l'exercice.

Les prérequis (bibliothèques à installer via pip).

Le code source.

⚠️ **Avertissement Légal**

*Les scripts liés à la sécurité (Keylogger, Sniffing, Malware) ont été développés dans un environnement contrôlé et isolé (VM) à des fins purement pédagogiques. Nous déclinons toute responsabilité en cas d'utilisation malveillante de ces codes.*