import pandas as pd

# Lire le fichier CSV
data = pd.read_csv("data/Patients.csv")

# Afficher le contenu du fichier
print("=== Données des patients ===")
print(data)
