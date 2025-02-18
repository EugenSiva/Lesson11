import json

class Student():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"Student sa vola {self.name} z krajiny {self.country} a ma {self.age} rokov"


eugen = Student(name="Eugen", age=36, country="Slovensko")
json_object = json.dumps(eugen.__dict__)
print(json_object)