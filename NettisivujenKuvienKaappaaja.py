import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

haluttuNettisivu = input("Minkä nettisivun kuvat haluaisit? ")
nettisivunKoodi = requests.get(haluttuNettisivu)
parsittuKoodi = BeautifulSoup(nettisivunKoodi.text, "html.parser")
nettisivunKuvat = parsittuKoodi.find_all("img")

valmiitKuvatLista = []
b = 0
for i in nettisivunKuvat:
    valmisKuva = urljoin(haluttuNettisivu, i["src"])
    if valmisKuva in valmiitKuvatLista:
        continue
    else:
        valmiitKuvatLista.append(valmisKuva)
        b+=1

print(valmiitKuvatLista)
haluatkoLadata = input(f"Haluatko ladata {b} kuvaa laitteellesi nettisivulta {haluttuNettisivu}? (True/False) ")

nettisivunOsoite = urlparse(haluttuNettisivu)
nettisivunOsoite = nettisivunOsoite.netloc

a = 1
if haluatkoLadata == "True":
    for i in valmiitKuvatLista:
        kuvakuva = requests.get(i)
        if kuvakuva.status_code == 200:
            os.makedirs(f"{nettisivunOsoite}_kuvat", exist_ok=True)
            with open(f"{nettisivunOsoite}_kuvat/kuva_{a}.jpg", "wb") as f:
                f.write(kuvakuva.content)
            print(f"kuva_{a} ladattu")
            a+=1
    print(f"Kaikki kuvat ladattu kansioon {nettisivunOsoite}_kuvat")
else:
    print("Okei, lataa sitten ensikerralla :(")
