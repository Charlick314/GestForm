import random


# 'est_divisible' renvoie si 'nombre' est divisible par 'denominateur_1' et 'denominateur_2'
# si 'denominateur_2' n'est pas spécifié, renvoie si 'nombre' est divisible par 'denominateur_1' uniquement

def est_divisible(nombre, denominateur_1, denominateur_2 = 1):
    return (nombre % denominateur_1 == 0) and (nombre % denominateur_2 == 0)


# 'liste_aleatoire' renvoie une liste aléatoire de 'longeur' entiers
# entre 'min' et 'max', par défaut entre -1000 et 1000

def liste_aleatoire(longeur, min = -1000, max = 1000):
    liste = []
    for i in range(longeur):
        n = random.randint(min, max)
        liste.append(n)
    return liste


# 'gestform' renvoie "Gestform", "Geste" ou "Forme"
# si 'nombre' est divisible respectivement par 3 et 5, 3 ou 5
# renvoie 'nombre' sinon
def gestform(nombre):
    if est_divisible(nombre, 3, 5):
        return "Gestform"
    elif est_divisible(nombre, 3):
        return "Geste"
    elif est_divisible(nombre, 5):
        return "Forme"
    else:
        return nombre


# - Main -
if __name__ == '__main__':

    test = liste_aleatoire(8)
    print(test)

    for i in test:
      print(gestform(i))

