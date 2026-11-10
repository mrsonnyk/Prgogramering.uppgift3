FILENAME = "backup_file.txt"

#Reading from file saved content and restoring the list
def load_list_from_file():
     try:
         with open(FILENAME, "r",encoding = "utf-8") as fil:
             for rad in fil:
                 if rad.strip():    #rensar mellanslag och så raden ej är tom
                      the_list.append(rad.strip())
     except FileNotFoundError:
         #ignorerar om filen inte finns, den skapas mew när python försöker skriva till den
         pass


#Creates or writes over the backup file with the_list
def save_list_to_file():
     with open(FILENAME, "w",encoding = "utf-8") as fil:
         for value in the_list:
             fil.write(value + "\n")



#Ask user for menu choise: (0-3)
#    return: menu_value
def get_user_menu_choise():
    while True:      #Körs till loopen bryts när giltigt värde matats in
        try:         #Måste ha en catch här eftersom jag ber om int men kan få annat
            value = int(input("Ange menyval (0-3): "))
            if value < 0 or value >3:            #Kollar så value ligger inom menyvalen
                print("Värdet ligger utanför intervallet, försök igen.")
            else:
                return value                        #Giltigt menyval
        except ValueError:         #Fångar upp värdes-fel då value försöker ta imot ett (int)
            print("Värdet måste av typen (int) dvs ett tal (0, 1, 2, 3).")


#Print list
#Kollar om listan är tom, om inte skriver ut listan
def print_list():
    if not the_list:                            #the_list är False om den är tom
        print("Listan är tom")
    else:
        print("\n - - Listans innehåll - -") 
        for number, x in enumerate(the_list):     #Skapar värdepar av samtliga värden i listan:

            print(f"{number+1}: {x}")       # ex: list = ["ett","två"] hade gett (1, ett) (2, två). nummer=1,x=ett


#Add new Value to List
#Kollar efter dubletter samt lägger till värden i listan
def add_new_value_to_list():
    new_value = input("Vad vill du lägga till? (lämna fältet tomt för att komma till menyn: ): ")
    if not new_value:         #Fältet lämnades tomt, inmatning: ""
        print("Åter till menyn")
    else:
        if new_value in the_list:
            print("Värdet fanns redan, inget ändrades")
        else:
            the_list.append(new_value)
            print("Följande värde lades till i listan: " + new_value)

#Remove value from list
def delete_value_from_list():
    if not the_list:
        print("Listan är tom, åter till menyn.")
    else:
        value = input("Vad vill du ta bort? (lämna tomt för att återgå till menyn): ")
        if value == "":     #Kunde öven använt "if not value" här
            print("Åter till menyn")
        elif value in the_list:
            the_list.remove(value)
            print("Följande har raderats: " + value)
        else:
            print("Värdet fanns ej i listan, åter till menyn")

# Huvudmeny Main
the_list = []    #Skapar en tom lista, efter som listan bara är en referens till minnet kommer alla funtioner åt den
load_list_from_file()   #Hämtar om det finns sparade värden i separat funktion från lista
#Startar en evighetsloop som avslutas först när användaren ber om det med menyval som genererar break
while True:
    print("\n-=Huvudmenyn=-")
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
        save_list_to_file()                  #Sparar värderna
        print("\nListan har sparats och programmet avslutas nu.")
        break                                #Bryter loopen och avslutar
