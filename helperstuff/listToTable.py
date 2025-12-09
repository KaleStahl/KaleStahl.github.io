def listToTable(filename):
    try:
        with open(filename, "r") as file:
            list = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    tableString =   ""
    list = list.splitlines()
    cutIndex1 = [i for i, s in enumerate(list) if "Trainer: " in s][0]
    cutIndex2 = [i for i, s in enumerate(list) if "Energy: " in s][0]
    pokemonList = list[1: cutIndex1-1]
    trainerList = list[cutIndex1 + 1: cutIndex2-1]
    energyList = list[cutIndex2 + 1: ]
    pMaxLen = len(max(pokemonList, key=len))
    tMaxLen = len(cutOff(max(trainerList, key=len)))
    eMaxLen = len(cutOff(max(energyList, key=len)))
    maxRows = max(len(pokemonList), len(trainerList), len(energyList))
    tableString += f"| {'Pokemon'.ljust(pMaxLen)} | {'Trainer'.ljust(tMaxLen)} | {'Energy'.ljust(eMaxLen)} | \n"
    tableString += f"|{'-'*(pMaxLen +2)}|{'-'*(tMaxLen +2)}|{'-'*(eMaxLen +2)}| \n"
    for i in range(maxRows):
        pokemon = pokemonList[i] if i < len(pokemonList) else ""
        pFiller = pMaxLen - len(pokemon)
        pokemon += " "* pFiller
        trainer = cutOff(trainerList[i]) if i < len(trainerList) else ""
        tFiller = tMaxLen - len(trainer)
        trainer += " "* tFiller
        energy = cutOff(energyList[i]) if i < len(energyList) else ""
        eFiller = eMaxLen - len(energy)
        energy += " "* eFiller
        tableString += f"| {pokemon} | {trainer} | {energy} | \n"
    return tableString

def cutOff(input_string):
    words = input_string.split() 
    if len(words) >= 2:
        return " ".join(words[:-2]) 
    else:
        return ""


print(listToTable("E:/_repos/KaleStahl.github.io/helperstuff/listFile.txt"))

