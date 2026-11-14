FILENAME = "mätdata.csv"
tider = []
temperaturer = []

#Reads messurement from file
def load_list_from_file():
    try:
        with open(FILENAME, "r", encoding="utf-8") as fil:
            next(fil)   #Hoppar över första raden med rubriken
            for rad in fil:
                if rad.strip():  # rensar mellanslag och så raden ej är tom
                    temp = rad.split(",")
                    tider.append(temp[0].strip())
                    temperaturer.append(temp[1].strip())
    except FileNotFoundError:
        pass
    print(tider)



load_list_from_file()