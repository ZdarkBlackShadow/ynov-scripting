# Chapitre 2

## Consigne

Vérifier l'installation de Python, la version du système d'exploitation et la présence de Pip.

## Prérequis

Aucune installation requise

## Script

```python
import sys
import platform
import os

def verifier_environnement():
    print("--- Rapport d'environnement Python ---")
    print(f"Version Python : {sys.version.split()[0]}")
    print(f"Système OS     : {platform.system()} {platform.release()}")
    print(f"Exécutable     : {sys.executable}")
    
    try:
        import pip
        print(f"Version Pip    : {pip.__version__}")
    except ImportError:
        print("Version Pip    : Non installé (Attention : nécessaire pour installer des bibliothèques)")
        
    print("-" * 38)
    print("Votre environnement est prêt à exécuter des scripts.")

if __name__ == "__main__":
    verifier_environnement()
```