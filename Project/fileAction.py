import pathlib

####################################################################################

def openFile(Name):
# czyta caly plik do pamieci podrecznej linia po linii
    Tab=[]

    try:
        File=open(Name,"r")
        # otwiera plik w trybie do odczytu

        while True:
            Line=File.readline()
            # czyta plik linia po linii

            if not Line:
                break
                # jezeli linie sie skoncza to przestaje czytac

            Tab.append(Line)
            # dopisuje linie do tablicy z tekstem

        return Tab
        # zwraca tablice z tekstem

    except:
        print("Niema takiego pliku")
        # jezeli nie da sie otworzyc tego pliku to zwraca blad
        return "~"

####################################################################################

def saveFile(Name,Tab):
# zapisuje caly plik linia po linii
    File=open(Name,"a")
    # otwiera plik w trybie dopisywania

    for Key in Tab:
    # iteruje po liniach w tekscie
        File.write(Key)
        # dopisywanie linii do pliku
        File.write("\n")
        # dopisywania znaku spacji do konca linii

    File.close()
    # zamyka plik po zapisaniu wszystkich linii

####################################################################################

def saveEdit(Name,Word):
    # dopiuje fragnent informacji do pliku, bez tworzenia nowej linii
    File=open(Name,"a")
    File.write(Word)
    File.close()

####################################################################################

def setPathToFile(Name):
    Path=str(pathlib.Path(__file__).parent.resolve())
    # ustala bezwzgledno siceszke do katalogu z programem i zapisuje ja jako stringa

    return Path+"/ROBOCZY/"+Name
    # dodaje do nazwy pliku bezwzgledna scierzke do niego
    # plik muis byc w katalogu roboczym bo inaczej nie zadziala