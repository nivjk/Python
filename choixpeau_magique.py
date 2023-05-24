print("Choixpeau magique : << Difficile, très difficile… Je vois beaucoup de courage et des qualités intellectuelles aussi. Il y a du talent, oh oui, et un grand désir de faire ses preuves. Alors, où vais-je te mettre ? >>\n")
print("Le choixpeau magique a quelques questions à vous poser, veuillez y répondre en choisissant le nombre associé au caractère. À la fin, nous vous révélerons la maison que vous rejoindrez.\n")

serpentard = ["Ambitieux", "Rusé", "Manipulateur", "Franc", "Egocentrique"]
gryffondor = ["Audacieux", "Aventurier", "Impulsif", "Courageux", "Protecteur"]
poufsouffle = ["Trop prudent", "Travailleur", "Dévoué", "Loyal", "Réservé"]
serdaigle = ["Rêveur", "Réfléchi", "Introverti", "Créatif", "Observateur"]

totalPoints = 0

for i in range(5):
    print("Êtes-vous plutôt :")
    print("    1. " + serpentard[i])
    print("    2. " + gryffondor[i])
    print("    3. " + poufsouffle[i])
    print("    4. " + serdaigle[i])

    reponse = int(input("\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
    totalPoints += reponse

if totalPoints > 0 and totalPoints < 6:
    print("<< SERPENTARD !!! >> cria le choixpeau.")
elif totalPoints >= 6 and totalPoints < 11:
    print("<< GRYFFONDOR !!! >> cria le choixpeau.")
elif totalPoints >= 11 and totalPoints < 16:
    print("<< POUFFSOUFFLE !!! >> cria le choixpeau.")
else:
    print("<< SERDAIGLE !!! >> cria le choixpeau.")
