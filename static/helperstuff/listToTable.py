def listToTable(filename):
    try:
        with open(filename, "r") as file:
            list = file.read()
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    tableString =   "| Pokemon | Trainer | Energy | \n |---|---|---| \n"
    list = list.splitlines()
    cutIndex1 = [i for i, s in enumerate(list) if "Trainer: " in s][0]
    cutIndex2 = [i for i, s in enumerate(list) if "Energy: " in s][0]
    pokemonList = list[1: cutIndex1-1]
    trainerList = list[cutIndex1 + 1: cutIndex2-1]
    energyList = list[cutIndex2 + 1: ]
    maxLength = max(len(pokemonList), len(trainerList), len(energyList))
    for i in range(maxLength):
        pokemon = pokemonList[i] if i < len(pokemonList) else ""
        trainer = trainerList[i] if i < len(trainerList) else ""
        energy = energyList[i] if i < len(energyList) else ""
        tableString += f"| {pokemon} | {trainer} | {energy} | \n"
    return tableString


print(listToTable("listFile.txt"))

