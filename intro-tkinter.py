#!/usr/bin/python3
#coding: utf8
try:
     import tkinter as Tk
except:
     import Tkinter as Tk

def pointeur(event):
	global coup
	# DÃ©termination de l'index pour le joueur
	if tour % 2 == 0:
		joueur = 1
	else :
		joueur = 0
	# clic sur premiÃ¨re ligne
	if event.x >= 5 and event.x <=130 and event.y >= 5 and event.y <=130 :
		zone = 'A1'
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(0,0,135,135,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
	if event.x >= 140 and event.x <=265 and event.y >= 5 and event.y <=130 :
		zone = "A2"
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(135,0,270,135,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
	if event.x >= 275 and event.x <=400 and event.y >= 5 and event.y <=130 :
		zone = "A3"
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(270,0,405,135,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
	# clic sur seconde ligne
	if event.x >= 5 and event.x <= 130 and event.y >= 140 and event.y <=265 :
		zone = "B1"
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(0,135,135,270,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
	if event.x >= 140 and event.x <=265 and event.y >= 140 and event.y <=265 :
		zone = "B2"
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(135,135,270,270,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
	if event.x >= 275 and event.x <=400 and event.y >= 140 and event.y <=265 :
		zone = "B3"
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(270,135,405,270,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
	# clic sur troisiÃ¨me ligne
	if event.x >= 5 and event.x <=130 and event.y >= 275 and event.y <=400 :
		zone = "C1"
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(0,270,135,405,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
	if event.x >= 140 and event.x <=265 and event.y >= 275 and event.y <=400 :
		zone = "C2"
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(135,270,270,405,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
	if event.x >= 275 and event.x <=400 and event.y >= 275 and event.y <=400 :
		zone = "C3"
		if zone in coup :
			erreur(1, tour)
		else:
			dessin(270,270,405,405,tour)
			coup.append(zone)
			phase[joueur].append(zone)
			gestion_gagnant(zone,joueur)
# Fonction pour le dessin des formes
def dessin(x0,y0,x1,y1,forme):
	global tour
	if forme % 2 == 0:
		principal.create_oval(x0+20,y0+20,x1-20,y1-20,width=10)
	else:
		principal.create_line(x0+20,y0+20,x1-20,y1-20,width=10)
		principal.create_line(x1-20,y0+20,x0+20,y1-20,width=10)
	tour = tour + 1
	if tour % 2 == 0:
		label_information.configure(text="A votre tour Joueur 2")
	else :
		label_information.configure(text="A votre tour Joueur 1")
# Fonction pour connaitre le gagnant
def gestion_gagnant(case,joueur):
	global fin_partie
	nb_serie = 0
	jeu_joueur = gagnant[joueur]
	for serie in liste_gagnant :
		try:
			rang = serie.index(case)
			ligne_gagnant = jeu_joueur[nb_serie]
			ligne_gagnant[rang] = True
			jeu_joueur[nb_serie] = ligne_gagnant
			gagnant[joueur] = jeu_joueur
		except ValueError :
			pass
		nb_serie = nb_serie + 1
	for serie in gagnant[joueur] :
		if serie.count(True) == 3 :
			label_information.configure(text="Le joueur "+str(joueur+1)+" a gagnÃ©")
			fin_partie = Tk.Toplevel()
			cadre_fin = Tk.Canvas(fin_partie,height=200,width=200,bg="green")
			label_gagnant = Tk.Label(cadre_fin,text="Le joueur "+str(joueur+1)+", faites un choix pour la suite")
			label_gagnant.pack()
			fin_quitter = Tk.Button(cadre_fin,text="Quitter",command=fenetre.quit)
			fin_nouveau = Tk.Button(cadre_fin,text="Rejouer",command=rejouer)
			fin_nouveau.pack(side="left")
			fin_quitter.pack(side="right")
			cadre_fin.pack()
# Gestion des erreurs
def erreur(numero,tour):
	if numero == 1:
		if tour % 2 == 0:
			joueur = 2
		else :
			joueur = 1
		label_information.configure(text="Case dÃ©jÃ  jouÃ©e, toujours Ã  vous Joueur "+ str(joueur))

# Initialisation de l'interface du jeu
def init():
	# Les lignes
	lig_hor_1 = principal.create_line(0, 135, 405, 135)
	lig_hor_2 = principal.create_line(0, 270, 405, 270)
	lig_vert_1 = principal.create_line(135, 0, 135, 405)
	lig_vert_2 = principal.create_line(270, 0, 270, 405)

	principal.pack()
	# DÃ©tection de clic
	principal.bind("<Button-1>", pointeur)

	# Gestion des informations affichÃ©es
	label_information.configure(text="Joueur 1, commencez !!!")
	information.pack()
	label_information.pack()
# Nouvelle partie aprÃ¨s la fin d'une autre
def rejouer():
	fin_partie.destroy()
	nouveau()
# Nouvelle partie, peu importe le moment
def nouveau():
	global tour, coup, phase, gagnant, partie_en_cours
	partie_en_cours = True
	tour = 1
	coup = []
	phase = [[],[]]
	gagnant[0] = [[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]
	gagnant[1] = [[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]
	principal.delete(Tk.ALL)
	init()

fenetre = Tk.Tk()
fenetre.title('Morpion')
# CrÃ©ation du menu
menu_principal = Tk.Menu(fenetre)
menu_accueil = Tk.Menu(menu_principal)
menu_accueil.add_command(label='Relancer', command=nouveau)
menu_accueil.add_separator()
menu_accueil.add_command(label='Quitter',command=fenetre.quit)
menu_principal.add_cascade(label='Accueil', menu = menu_accueil)
fenetre.config(menu = menu_principal)

# DÃ©clarations des variables
tour = 1
coup = []
phase = [[],[]]
liste_gagnant = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3'],['A1','B1','C1'],['A2','B2','C2'],['A3','B3','C3'],['A1','B2','C3'],['C1','B2','A3']]
gagnant = [[],[]]
gagnant[0] = [[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]
gagnant[1] = [[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]

# crÃ©ation des diffÃ©rentes de la fenÃªtre
principal = Tk.Canvas(fenetre, width=405, height=405, bg='blue')
information = Tk.Canvas(fenetre)
label_information = Tk.Label(information)
init()

# Lancement de la boucle
fenetre.mainloop()