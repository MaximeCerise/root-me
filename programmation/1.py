import socket
import re
import math

#https://www.root-me.org/fr/Challenges/Programmation/TCP-Retour-au-college

# Connexion au serveur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenge01.root-me.org", 52002))

# Réception du message du serveur
msg = s.recv(1024)
msg = msg.decode("utf-8")

# Affichage du message reçu du serveur
print("Message reçu :")
print(msg)

# Utilisation d'une expression régulière pour extraire les nombres
pattern = r'Calculate the square root of (\d+) and multiply by (\d+) ='
match = re.search(pattern, msg)

if match:
    # Extraction des deux nombres
    a = int(match.group(1))
    b = int(match.group(2))
    print(a)
    # Calcul de la racine carrée de a et multiplication par b
    result = math.sqrt(a) * b
    result = round(result, 2)
    print(b)
    # Préparation du résultat à envoyer au serveur
    data = str(result) + '\n'  # Conversion en string + ajout de '\n', le \n sert à indiquer au serveur la fin du message
    data = data.encode("utf-8")     # Encodage en UTF-8
    
    # Envoi de la réponse au serveur
    s.sendall(data)
    print(data)
    # Réception de la réponse du serveur après envoi
    response = s.recv(1024)
    print("Réponse du serveur :")
    print(response.decode("utf-8"))
else:
    print("Aucun motif trouvé dans le message.")
