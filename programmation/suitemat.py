import requests
from bs4 import BeautifulSoup
import re

session = requests.Session()
url = "http://challenge01.root-me.org/programmation/ch1/"
response = session.get(url)  # Utiliser la session pour suivre les cookies
html = response.text

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
numbers = re.findall(r"-?\d+", text)
numbers = list(map(int, numbers))

match = re.search(r"\] ([+-]) \[", text)
operator = match.group(1)


def calculate_un(U0, m, a, b):
    if operator == "+":
        return int(U0 + a * m + (b * (m - 1) * (m)) / 2)
    elif operator == "-":
        return int(U0 + a * m - (b * (m - 1) * (m)) / 2)
    else:
        print("operator == None")


U0 = numbers[4]
a = numbers[1]
b = numbers[2]
n = numbers[5]

print(U0, n, a, b)
rep = calculate_un(U0, n, a, b)

result_url = f"http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result={int(rep)}"
result_response = session.get(result_url)

print(text)
print(result_response.text, "html.parser")