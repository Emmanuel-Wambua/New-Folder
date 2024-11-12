import json

person_JSON = '{"name":"Manu","Girls":0,"age":18}'

print(type(person_JSON))

person = json.loads(person_JSON)

print(type(person))
print(person)
