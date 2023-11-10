
"""
Jouer au jeu du devin en laissant le choix à l’utilisateur d’être le devin ou le joueur.

Principe : Le joueur choisit s’il veut être le devin ou non. En fonction, la machine ou le joueur doit deviner un nombre
entre 0 et 999 que le joueur ou la machine choisi en faisant des propositions et en étant aiguillé par le devin avec des
réponses de type plus petit ou plus grand. Le devin doit deviner la réponse avec le moins d’essais possible.

"""
import random

def Main():
	choix_de_partie()
	
	

# Afficher le Menu.
def choix_de_partie():

	choix_partie = " "  
	while choix_partie != "0": 
		# Présenter du menu
		print("1- L'ordinateur choisit un nombre et vous le devinez")		
		print("2- Vous choisissez un nombre et l'ordinateur le devine")
		print("0- Quitter le programme")

		#Saisir le choix
		choix_partie = input("Votre choix :")

		
		if choix_partie == "1":
			joueurdevin()
		
		
		elif choix_partie == "2":
			ordidevin()
		
		print("Au revoir…")
			
#Jouer au devin, l’utilisateur est le devin.
def joueurdevin():

	# Choisir un nombre entre 0 et 999
	from random import randint; nbre_a_deviner = random.randint(0, 1000)
	print("J'ai choisi un nombre compris entre 1 et 999.", end='\n')


	# Faire deviner le nombre.
	nbre_propose = 1000
	nbre_essais = 0
	while nbre_a_deviner != nbre_propose:

		# Acquérir la proposition du joueur.
		nbre_propose = int(input("Proposition:"))

		# Compter les essais
		nbre_essais += 1

		# Evaluer de la proposition
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
		# Demander si le joueur a choisi un nombre.
		pret = input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ?")
		if pret != "o":
			print("J’attends…")

	# Faire les propositions pour trouver le nombre
	#initialiser l'intervale de recherche.
	a = 0	
	b = 999

	nombre_essais = 0 # initialisation du compteur d'essais.
	verif = " " # pour entre dans la bouche
	
	# Faire des propositions
	while verif != 't':
		# Faire une proposition
		proposition = (a + b) // 2
		# Initier le calcul de la proposition
		print(proposition)
		# Afficher la proposition
		nombre_essais += 1
		# Compte le nombre d'essais
		
		ok=False
		while not ok:	
		# S'assurer que la lettre entrée est parmis celles nécessaires
			verif = input("Trop (g)rand, trop (p)etit ou (t)rouvé ?")
			if vérif in ('g','p','t'):
				ok = True
			
		# Vérifier la proposition
		if verif == 'p':
			a = proposition
			ok = True

		elif verif == 'g':
			b = proposition
			ok = True

		elif verif == 't':
			print("Trouvé!")
			ok = True

	# Afficher le nombre d'essais.
	print(f"J’ai trouvé en {nombre_essais} essais.")
	


Main()
