import socket
import re
import math
import codecs
#https://www.root-me.org/fr/Challenges/Programmation/TCP-La-roue-romaine

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenge01.root-me.org", 52021))
msg = s.recv(1024).decode('utf8')

pattern = r"my string is '([A-Za-z0-9+/=]+)'"
match = re.search(pattern, msg)
msg = match[1]

msg = codecs.decode(msg, 'rot-13') + '\n'
s.send(msg.encode('utf8'))
print(s.recv(1024))
