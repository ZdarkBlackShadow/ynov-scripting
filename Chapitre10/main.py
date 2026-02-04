import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import subprocess
from datetime import datetime

def extraire_donnees_sar():
    temps = []
    cpu_idle = []

    try:
        resultat = subprocess.run(['sar', '-u', '1', '5'], capture_output=True, text=True, check=True)
        lignes = resultat.stdout.strip().split('\n')

        for ligne in lignes:
            colonnes = ligne.split()
            if len(colonnes) > 0 and ":" in colonnes[0] and "Average" not in colonnes[0]:
                try:
                    heure = colonnes[0]
                    idle_val = float(colonnes[-1].replace(',', '.'))
                    
                    temps.append(heure)
                    cpu_idle.append(idle_val)
                except ValueError:
                    continue
        
        return temps, cpu_idle
    except subprocess.CalledProcessError as e:
        print(f"Erreur : sar n'est peut-être pas installé. {e}")
        return [], []

def generer_graphique(temps, idle):
    if not temps:
        return

    # Calcul de la charge (Charge = 100 - %idle)
    charge_cpu = [100 - x for x in idle]

    plt.figure(figsize=(10, 5))
    plt.plot(temps, charge_cpu, marker='o', linestyle='-', color='r', label='Charge CPU (%)')
    plt.ylim(0, 100)
    plt.xlabel('Temps')
    plt.ylabel('Activité (%)')
    plt.title('Évolution de l\'activité du serveur (100 - %idle)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    t, i = extraire_donnees_sar()
    generer_graphique(t, i)