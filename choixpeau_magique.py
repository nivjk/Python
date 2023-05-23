
# Créer le 22 mai 2023
# par Nivetha Jeyakumar
# Master IRS P33
# 
# C vs Python (Mini-jeu)


question1 = int(input("Êtes-vous plutôt :\n1. Ambitieux\n2. Protecteur\n3. Loyal\n4. Empathique\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
question2 = int(input("Êtes-vous plutôt :\n1. Rusé\n2. Aventurier\n3. Travailleur\n4. Intelligent\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
question3 = int(input("Êtes-vous plutôt :\n1. Manipulateur\n2. Impulsif\n3. Trop prudent\n4. Indépendant\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
question4 = int(input("Êtes-vous plutôt :\n1. Egocentrique\n2. Charismatique\n3. Réservé\n4. Introverti\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
question5 = int(input("Êtes-vous plutôt :\n1. Franc\n2. Courageux\n3. Loyal\n4. Réfléchi\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
question6 = int(input("Êtes-vous plutôt :\n1. Ingénieux\n2. Audacieux\n3. Travailleur\n4. Créatif\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
question7 = int(input("Êtes-vous plutôt :\n1. Opportuniste\n2. Téméraire\n3. Trop prudent\n4. Rêveur\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
question8 = int(input("Êtes-vous plutôt :\n1. Persévérant\n2. Enthousiaste\n3. Sincère\n4. Observateur\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
question9 = int(input("Êtes-vous plutôt :\n1. Ambitieux\n2. Courageux\n3. Aimable\n4. Curieux\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))
questionX = int(input("Êtes-vous plutôt :\n1. Rusé\n2. Audacieux\n3. Dévoué\n4. Logique\n\nChoisissez un nombre entre 1, 2, 3 et 4 : "))

totalPoints = question1 + question2 + question3 + question4 + question5 + question6 + question7 + question8 + question9 + questionX

if totalPoints >= 1 and totalPoints <= 10:
    print("<< SERPENTARD !!! >> cria le choixpeau.")
elif totalPoints >= 11 and totalPoints <= 20:
    print("<< GRYFFONDOR !!! >> cria le choixpeau.")
elif totalPoints >= 21 and totalPoints <= 30:
    print("<< POUFFSOUFFLE !!! >> cria le choixpeau.")
else:
    print("<< SERDAIGLE !!! >> cria le choixpeau.")

