import json

objects_list =[]

def Display_Data():
    print(objects_list)
    
    # Print the objects
    for obj in objects_list:
        print(f"Name: {obj.name}, Age: {obj.age}")


def load_data():
    global objects_list
    class MyClass:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    # Read the JSON file
    with open('objects.json', 'r') as json_file:
        data = json.load(json_file)

    # Create objects from the data
    objects_list = [MyClass(obj['name'], obj['age']) for obj in data]
    return(objects_list)

    print("Data Loaded")

