def presenteer(dict, totaal):
    uitvoer = []
    for el in dict:
        uitvoer.append(f"{el} : {dict[el]} euro")
    uitvoer.append(25 * "=")
    uitvoer.append(f"totaal : {totaal}")
    for el in uitvoer:
        print(el)
    return 

       
    

