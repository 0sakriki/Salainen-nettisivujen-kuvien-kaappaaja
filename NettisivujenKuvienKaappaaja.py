import requests

haluttuNettisivu = input("Minkä nettisivun kuvat haluaisit? ")

nettisivunKoodi = requests.get(haluttuNettisivu)

print(nettisivunKoodi.text)