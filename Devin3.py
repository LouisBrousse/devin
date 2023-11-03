
"""
Jouer au jeu du devin en laissant le choix à l’utilisateur d’être le devin ou le joueur.

Principe : Le joueur choisit s’il veut être le devin ou non. En fonction, la machine ou le joueur doit deviner un nombre
entre 0 et 999 que le joueur ou la machine choisi en faisant des propositions et en étant aiguillé par le devin avec des
réponses de type plus petit ou plus grand. Le devin doit deviner la réponse avec le moins d’essais possible.

"""
def Main():
	choix_de_partie()
	joueurdevin()
	ordidevin()

# Afficher le Menu.
def choix_de_partie():

	choix_partie = " "  
	while choix_partie != "0": 
# présentation du menu
		print("1- L'ordinateur choisit un nombre et vous le devinez")
		print("2- Vous choisissez un nombre et l'ordinateur le devine")
		print("0- Quitter le programme")

#Saisie le choix
		choix_partie = input("Votre choix :")

# Jouer au Devin avec l'utilisateur qui fait deviner le nombre?
		if choix_partie == "1":
			joueurdevin()
# Jouer au Devin avec l'utilisateur qui fait deviner le nombre?
		elif choix_partie == "2":
			ordidevin()
# Traite la réponse si le choix est que l’utilisateur souhaite quitter la partie?
		elif choix_partie == "0":
			print("Au revoir…")
			exit()

def joueurdevin():
#Jouer au devin, l’utilisateur est le devin.
	import random
	nbre_propose = 1000
	nbre_essais = 0

	# Choisir un nombre entre 0 et 999
	from random import randint; nbre_a_deviner = random.randint(0, 1000)
	print("J'ai choisi un nombre compris entre 1 et 999.", end='\n')


# faire deviner le nombre.
	while nbre_a_deviner != nbre_propose:

		# Acquérir la proposition du joueur.
		nbre_propose = int(input(f"Proposition:"))

		# Compter les essais
		nbre_essais += 1

		# Evaluation de la proposition
		if nbre_propose > nbre_a_deviner:
			print("Trop grand!")
		elif nbre_propose < nbre_a_deviner:
			print("Trop petit!")
		else:
			print("Trouvé!")

	# Afficher le résultat avec le décompte des essais
	print(f"Bravo ! Vous avez trouvé en {nbre_essais} essais.")
	

def ordidevin():
#Jouer au devin, l’ordinateur est le devin.
	# Faire Choisir un nombre
	pret = ''
	while pret != "o":
		# Demande si le joueur a choisi un nombre.
		pret = input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ?")
		if pret != "o":
			print("J’attends…")

	# Faire les propositions pour trouver le nombre
	#initialisation de l'intervale de recherche.
	a = 0	
	b = 999

	nombre_essais = 0 # initialisation du compteur d'essais.
	verif = " " # pour entre dans la bouche
	
	# Faire des propositions
	while verif != 't':
		# Faire une proposition
		proposition = (a + b) // 2
		# Calcule la proposition
		print(proposition)
		# Affiche la proposition
		nombre_essais += 1
		# Compte le nombre d'essais
		ok=False
		while not ok
			verif = input("Trop (g)rand, trop (p)etit ou (t)rouvé ?")
		# Vérifie la proposition
		if verif == 'p':
			a = proposition

		elif verif == 'g':
			b = proposition

		elif verif == 't':
			print("Trouvé!")

	# Affiche le nombre d'essais.
	print(f"J’ai trouvé en {nombre_essais} essais.")
	


Main()