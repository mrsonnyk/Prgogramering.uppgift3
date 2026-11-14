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
                    tider.append(str(temp[0]))
                    temperaturer.append(float(temp[1]))
    except FileNotFoundError:
        print("Ajdå, filen saknas! ")
    except ValueError:
        print("Ajdå, filen verkar vara korrupt!")
    print("tider: ", tider)
    print("temperaturer: ", temperaturer)
    return tider, temperaturer


def plot_time_and_temperature(tider, temperaturer):
    avg_temp = sum(temperaturer)/len(temperaturer)
    figure, axes = plt.subplots()                   #Delar upp figuren i bild / kordinatsystem för att underlätta
    axes.plot(tider, temperaturer,color="red", marker="o")        #Skapar grund plotten med tider /temp
    axes.axhline(avg_temp, color="blue", linestyle="--", label=f"Medel ({avg_temp:.1f} °C)") #Lägger till en avg_t linje
    axes.set_title("Temeraturmätning")
    axes.set_ylabel("Temperatur (°C)")
    axes.set_xlabel("Tid")
    axes.grid(True)                                                                 # Lägger till ett rutnät
    plt.legend()
    figure.savefig("temperatur.png", dpi=300, bbox_inches="tight") # Sparar plotten
    plt.show()  # Öppnar fönstret med grafen
    plt.close()

#Huvudprogram
tider, temperaturer = load_list_from_file() #Hämtar mätdata från fil och sparar i 2 listor
plot_time_and_temperature(tider, temperaturer)  #plottar värderna från listorna