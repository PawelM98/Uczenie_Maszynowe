import json
import json
import requests

# Prosty przykład serializacji
data = {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium "
            "quis pariatur\nmolestiae porro eius odio et labore et velit aut "
}


with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

# Prosty przykład deserializacji
json_string = """
{
    "researcher": {
        "name": "Pawel Michcinski",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data1 = json.loads(json_string)
# print(data1)

# Przykład z prawdziwego świata
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
# print("TODOS:", todos)

# Mapa userId do wszystkich numerów  TODOs dla tego użytkownika
todos_by_user = {}

# Inkrementacja kompletnych TODOs zliczanych dla każdego użytkownika.
for todo in todos:
    if todo["completed"]:
        try:
            # Inkrementuj istniejące konto użytkownika.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # Ten użytkownik nie był widziany. Ustaw jego licznik na 1.
            todos_by_user[todo["userId"]] = 1

# Utwórz posortowaną listę (userId, num_complete) par.
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)

# Uzyskaj maksymalną liczbę ukończonych TODOs.
max_complete = top_users[0][1]

# Utwórz listę użytkowników którzy ukonczyli
# Maksymalna liczba TODOs
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

# Kodowanie i dekodowanie niestandardowych obiektów Pythona
class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

## Kodowanie typów niestandardowych
def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)


## Dekodowanie typów niestandardowych
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct