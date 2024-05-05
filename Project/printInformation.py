####################################################################################

def mainMenu():
    #wyswietla pole  wyboru trybu w kturym będzie działał program
    print("Wybierz opcje:")
    print("1. Ukryj wiadomosc")
    print("2. Odczytaj wiadomosc")
    print("3. Wyjdz")

    return int(input(">>"))

####################################################################################

def question(Text):
    # wyswietla unwersale pole do podania wszystkich informacji
    # potrzebnych do dzialania programu
    print(Text)
    return str(input(">>"))
