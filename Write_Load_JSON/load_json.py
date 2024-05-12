import json


def load_data():
    class MyClass:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    # Read the JSON file
    with open('objects.json', 'r') as json_file:
        data = json.load(json_file)

    # Create objects from the data
    objects_list = [MyClass(obj['name'], obj['age']) for obj in data]

    # Print the objects
    for obj in objects_list:
        print(f"Name: {obj.name}, Age: {obj.age}")
