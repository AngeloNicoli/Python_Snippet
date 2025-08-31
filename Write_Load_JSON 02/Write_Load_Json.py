import json

def write_json():
	lista_2d = [
    	[1, 2, 3],
    	[4, 5, 6],
    	[7, 8, 9]
	]

	with open("lista_2d.json", "w") as file:
		json.dump(lista_2d, file)

def load_json():
	with open("lista_2d.json", "r") as file:
		lista_caricata = json.load(file)
	print(lista_caricata)
	# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


write_json()
load_json()