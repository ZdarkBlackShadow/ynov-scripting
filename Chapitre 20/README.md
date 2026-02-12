# Analyse de Malware Python

## Objectif : Étude du comportement de scripts malveillants basiques et analyse des mécanismes d'infection.

    ATTENTION : Tous les tests ont été réalisés dans une Machine Virtuelle isolée (hors réseau)

## Méthodologie

    Acquisition : Clonage du dépôt malware_python.

    Analyse Statique : Revue du code source pour identifier les bibliothèques critiques (pynput, cryptography, socket).

    Analyse Dynamique : Exécution des scripts et monitoring via Process Explorer et Wireshark.

## Résultats des tests
### Script d'Espionnage (Keylogger)

    Fonctionnement : Utilise la librairie pynput pour "hooker" le clavier.

    Comportement observé : Le script intercepte chaque frappe clavier en arrière-plan et stocke les données dans un fichier log local (log.txt).

    Menace : Vol silencieux d'identifiants et de données sensibles.

### Script de Chiffrement (Ransomware PoC)

    Fonctionnement : Utilise Fernet (cryptography) pour générer une clé symétrique.

    Comportement observé : Parcours récursif des dossiers cibles -> Chiffrement du contenu des fichiers -> Suppression des originaux.

    Menace : Perte irréversible de données sans la clé de déchiffrement générée au lancement.

## Conclusion & Défense

Ces scripts démontrent que Python permet de créer des outils offensifs puissants avec peu de lignes de code.
Contre-mesures : Surveillance des processus Python inconnus, restriction des droits d'exécution et utilisation d'un EDR pour détecter les comportements de chiffrement massifs.