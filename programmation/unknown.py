import socket
import re
import math
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenge01.root-me.org", 52022))
msg = s.recv(1024)

pattern = r"my string is '([A-Za-z0-9+/=]+)'"
match = re.search(pattern, msg.decode('utf8'))[1]
resp =  (base64.b64decode(match).decode()+'\n').encode()
print(match, "=>", resp)
s.send(resp)
print(s.recv(1024))