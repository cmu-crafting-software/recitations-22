import requests

res = requests.get("https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=state:*")
data = res.json()[1:]
total_population = 0
for row in data:
    state_name, population, state_code = row
    total_population += int(population)
print(total_population)
    


