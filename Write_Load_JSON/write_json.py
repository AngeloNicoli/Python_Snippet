import json


def save_data():
    class MyClass:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    # Instantiate two objects
    obj1 = MyClass("Alice", 25)
    obj2 = MyClass("Bob", 30)

    Continue_Insertion = input("Enter new Values? Y/N")
    while Continue_Insertion == "Y":
        print("e")
        Continue_Insertion = input("Enter new Values? Y/N")
    else:
        print("no more value")

    # Create a list to store the objects
    objects_list = [obj1.__dict__, obj2.__dict__]

    # Save the list to a JSON file
    with open('objects.json', 'w') as json_file:
        json.dump(objects_list, json_file)

    print("Objects saved to JSON file.")




