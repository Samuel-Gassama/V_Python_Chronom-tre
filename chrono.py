import time # Importation du module Time 

def convertisseur_temps(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Temps écoulé = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Appuyer sur entre pour commencer")
start_temps = time.time() # Fonction du module time

input("Appuyer sur entre pour arreter")
fin_temps = time.time() # Fonction du module time

temps_ecoule = fin_temps - start_temps #Calcul du tenmps écoulé depuis le lancement du chrono
convertisseur_temps(temps_ecoule)


