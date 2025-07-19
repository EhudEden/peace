contacts = {}
def ajout_contact(nom, numero):
    contacts.nom = numero
   # print(f"Nom   : {nom}")
   # print(f"Numero: {numero}")
    print()
    print("Contact {nom} ajouter :) !")

def suppr_contact(nom):
    if nom in contacts.keys():
        print(f"le contact {nom}({contacts.pop(nom)}) a été supprimé de votre repertoire")
    else:
        print("Contact non-trouvé !")

def affich_contacts():
    print("VOS CONTACTS !")
    for contact in contacts:
        print(f"Nom: {contact}, Numero: {contacts.get(contact)}")

def quitter():
    raise SystemExxit("Quitter")

def recher_contact(nom):
    for contact in contacts.keys():
        if nom in contact:
            print("Resultats de la recherche ...")
            print(f"{contact} : {contacts[contact]}")
        else:
            print("Aucun contact trouvé ): !")
            break
    for numero in contacts.values():
        if nom in numero:
            print("Resultats de la recherche ...")
            print(f"{numero}")

print("Veuillez choisir l'une des options suivantes :")
print("1.Ajouter un contact")
print("2.Supprimer un contact")
print("3.Rechercher un contact")
print("4.Afficher tous les contacts")
print("5.Quitter")
print()


choix = input("Veuillez entrer votre choix en entrant le chiffre correspondant: ")

while choix.isnumeric():

    match choix:

        case "1":
            print("veuillez entrer les informations ci-dessous demandées")
            ajout_contact(input("Nom: ").lower(), input("Numero: "))
            choix = input("Veuillez entrer votre choix en entrant le chiffre correspondant: ")

        case "2":
            suppr_contact(input("Entrez ici le nom du contact à supprimer: ").lower())
            choix = input("Veuillez entrer votre choix en entrant le chiffre correspondant: ")

        case "3":
            recher_contact(input("Veuillez entrer le nom du contact recherché :) : ").lower())
            choix = input("Veuillez entrer votre choix en entrant le chiffre correspondant: ")

        case "4":
            affich_contacts()
            choix = input("Veuillez entrer votre choix en entrant le chiffre correspondant: ")

        case "5":
            quitter()
            break
        case _:
            print("ERREUR: entrez un chiffre entre 1, 2, 3, 4 et 5")
            choix = input("Veuillez entrer votre choix en entrant le chiffre correspondant: ")




