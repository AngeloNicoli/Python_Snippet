with open("demofile.txt", "r") as file:
    lines = file.readlines()
    print(f"Numero di righe: {len(lines)}")
    for i, line in enumerate(lines):
        print(f"Riga {i+1}: {line}")