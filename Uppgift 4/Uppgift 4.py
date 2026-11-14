import matplotlib.pyplot as plt

"""Reads messurements from file
Reads data from: (fil) mätdata.csv
Return: tider[], temperaturer[]
"""
def load_list_from_file():
    tider = []
    temperaturer = []
    FILENAME = "mätdata.csv"
    try:
        with open(FILENAME, "r", encoding="utf-8") as fil:
            next(fil)   #Hoppar över första raden med rubriken
            for rad in fil:
                if rad.strip():  # rensar mellanslag och så raden ej är tom
                    temp = rad.strip().split(",")
                    tider.append(temp[0])
                    temperaturer.append(temp[1])
    except FileNotFoundError:
        print("Ajdå, filen saknas! ")
    return tider, temperaturer


#Huvudprogram
tider, temperaturer = load_list_from_file()