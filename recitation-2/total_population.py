import requests

def total_population_21():  
    """
    Compute the total population of 2021 using the census API
    """
    res = requests.get(
        "https://api.census.gov/data/2021/pep/population?get=POP_2021,NAME&for=state:*")
    data = res.json()[1:]
    total_population = 0
    for row in data:
        population, state_name, state_code = row
        total_population += int(population)
    return total_population

print(total_population_21())
