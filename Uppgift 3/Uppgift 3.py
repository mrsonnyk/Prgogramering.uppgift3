#Ask user for menu choise: (0-3)
#    return: menu_value
def get_user_menu_choise():
     return int(input("Ange menyval (0-3): "))

#Print list
#Kollar om listan är tom, om inte skriver ut listan
def print_list():
    if not the_list:
        print("Listan är tom")
    else:
        for number, x in enumerate(the_list):
            print(f"{number+1}: {x}")

#Add new Value to List
#Kollar efter dubletter samt lägger till värden i listan
def add_new_value_to_list():
    new_value = input("Vad vill du lägga till? (lämna fältet tomt för att komma till menyn: ): ")
    if not new_value:
        print("Åter till menyn")
    else:
        if new_value in the_list:
            print("Värdet fanns redan, inget ändrades")
        else:
            the_list.append(new_value)

#Remove value from list
def delete_value_from_list():
    if not the_list:
        print("Listan är tom, åter till menyn.")
    else:
        value = input("Vad vill du ta bort? (lämna tomt för att återgå till menyn): ")
        if value == "":
            print("Åter till menyn")
        elif value in the_list:
            the_list.remove(value)
            print("Följande har raderats: " + value)
        else:
            print("Värdet fanns ej i listan, åter till menyn")

# Huvudmeny Main
the_list = []
#Startar en evighetsloop som avslutas först när användaren ber om det med break 
while True:
    print("-=Huvudmenyn=-")
    print("0. Avsluta programmet.")
    print("1. Visa listan.")
    print("2. Lägg till.")
    print("3. Ta bort.")
    usr_pick = get_user_menu_choise()        #hämter värdet från separat funktion
    if usr_pick == 1:                        #Om Visa listan
        print_list()                         #Skriver listan med separat funktion
    elif usr_pick == 2:                      #Om Lägg till
        add_new_value_to_list()              #Lägger till värde i separat funktion
    elif usr_pick == 3:                      #om ta bort
        delete_value_from_list()             #Tar bort värde i separat funktion
    else:                                    #Menyval avsutar programmet genom att bryta loopen
        break                                #Bryter loopen och avslutar
