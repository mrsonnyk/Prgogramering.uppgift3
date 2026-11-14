import matplotlib.pyplot as plt


def load_list_from_file():
    """Reads messurements from file
    Reads data from: (fil) mätdata.csv
    Return: tider (list of string), temperaturer (list of float)
    """
    temp_tider = []
    temp_temperaturer = []
    filename = "mätdata.csv"
    try:
        with open(filename, "r", encoding="utf-8") as fil:
            next(fil)   #Hoppar över första raden med rubriken
            for rad in fil:
                if rad.strip():  # rensar mellanslag och så raden ej är tom
                    temp = rad.strip().split(",")
                    temp_tider.append(str(temp[0]))
                    temp_temperaturer.append(float(temp[1]))
    except FileNotFoundError:
        print("Ajdå, filen saknas! ")
    except ValueError:
        print("Ajdå, filen verkar vara korrupt!")

    return temp_tider, temp_temperaturer


def plot_time_and_temperature(tider, temperaturer):
    """Plots the graph with times vs temp
    tider: list[] with timesstaps as string
    temperaturer: list[] with temperatur as float
    """
    avg_temp = sum(temperaturer) / len(temperaturer)
    figure, axes = plt.subplots()          #Skapar plt och delar upp figuren i bild / kordinatsystem för att underlätta

    axes.plot(tider, temperaturer,color="red", marker="o", label="Temperatur") #Skapar grund plotten med tider /temp
    axes.axhline(avg_temp, color="blue", linestyle="--", label=f"Medel ({avg_temp:.1f} °C)") #Lägger till en avg_t linje

    axes.set_title("Temeraturmätning")
    axes.set_ylabel("Temperatur (°C)")
    axes.set_xlabel("Tid")
    axes.grid(True)                                                                 # Lägger till ett rutnät
    plt.legend()   #Visar F-string med avg_temp, samt temp längst upp till höger i rutan

    plt.savefig("temperatur.png", dpi=300, bbox_inches="tight")  # Sparar plotten
    plt.show()  # Öppnar fönstret med grafen
    plt.close() #Avslutar plot som försiktighets åtgärd

#Huvudprogram
tider, temperaturer = load_list_from_file() #Hämtar mätdata från fil och sparar i 2 listor

if tider and temperaturer:        #Kollar så listerna ej är tomma
    plot_time_and_temperature(tider, temperaturer)  #plottar värderna från listorna
else:
    print("Saknar tillräkligt med mätdata för att plotta en graf")