#!/usr/bin/env python3
import sys
from scapy.all import IP, ICMP, sr1

def main():
    target_ip = "8.8.8.8"

    print(f"--- [1] Création du paquet ICMP vers {target_ip} ---")
    paquet = IP(dst=target_ip) / ICMP()

    print("\n--- [2] Observation du contenu du paquet créé ---")
    paquet.show()

    print("\n--- [3] Envoi du paquet et attente de la réponse ---")
    reponse = sr1(paquet, timeout=2, verbose=0)

    print("\n--- [4] Observation de la réponse reçue ---")
    if reponse:
        print(f"Succès ! Réponse reçue de {reponse[IP].src}")
        reponse.show()
        
        if reponse[ICMP].type == 0:
            print("\n>> Confirmation : C'est bien un 'Echo Reply'.")
    else:
        print("Aucune réponse reçue (Délai dépassé ou paquet perdu).")

if __name__ == "__main__":
    main()