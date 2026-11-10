# Huvudmeny Main
print("-=Huvudmenyn=-")
print("0. Avsluta programmet.")
print("1. Visa listan.")
print("2. Lägg till.")
print("3. Ta bort.")
the_list = []
#Startar en evighetsloop som avslutas först när användaren ber om det med break
while True:
    usr_pick = int(input("Ange menyval (0-3): "))        #Inmatning av menyval castat som int, error måste hanteras sen
    if usr_pick == 1:                                    #Om Visa listan
        if not the_list:                                 #Kollar om listan är tom
            print("Listan är tom")
        else:                                            #Värderna ska skrivas ut
            # skapar par med hjälp av enumerate som startar med (nummer, x) som forloopen går igenom av listans innehåll
            for number, x in enumerate(the_list, start=1):
                print(f"{number}: {x}")
    elif usr_pick == 2:                                 #Om Lägg till
        new_value = input("Ange vill du lägga till?: ")  #Ber anv om värde att lägga till
        if not new_value:                                 #Kollar att det faktiskt är ett värde
            print("Måste innehålla ett värde")
        else:                                            #lägger till värdet sist i samlingen
            the_list.append(new_value)
    elif usr_pick == 3:                                   #om ta bort
        if not the_list:                                   #Kollar att listan inte är tom
            print("Listna är tom")
        else:
            new_value = input("Ange vill du tabort?: ")     #Ber om värde att radera
            if new_value in the_list:                       #Kontrollerar att värdet existerar samt raderar
                the_list.remove(new_value)
            else:
                print("Värdet finns ej")
    else:                                                  #Menyval avsutar programmet genom att bryta loopen
        break
