import textAction
import KeyAction
import fileAction
import printInformation
import spaceAction
import binaryAction
import others

####################################################################################

def hideInformation():
    Option=0

    Text=printInformation.question("Podaj wiadomosc do ukrycia")
    print("Minimalny wymagany rozmiar podkladki w slowach:",3*len(Text))
    # pobiera wiadomosc do ukrycia

    Source=printInformation.question("Podaj nazwe pliku z podkladka")
    # pobierara nazwe pliku z podkladka
    Source=fileAction.setPathToFile(Source)
    # ustala scieszke bezwzgledna do niego
    Pad=fileAction.openFile(Source)
    #sprawdza czy istnieje i jezeli tak, to pobiera jego zawartosc
    if Pad=="~":
        return

    if others.isSizeOk(Text,Pad)=="~":
    # sprawdza czy tekst zmiesci sie w podkladce
        return

    Key=textAction.hideText(Text,Pad)
    # generuje klucz steanogramu, zaminia go na postac binarna
    if Key[0]=="~":
        return

    Key=binaryAction.decToBin(Key)
    print("Rozmiar klucza w bitach:",len(Key))

    File=printInformation.question("Podaj plik do zapisu")
    # pobiera nazwe pliku do zapisu steanogramu
    File=fileAction.setPathToFile(File)
    # ustala scieszke bezwzgledna do niego
    

    Kod=printInformation.question("Podaj chaslo")
    Key=others.encryption(Key,Kod)
    # pobiera chaslo do odszyfrowania klucza i
    # sprawdza czy jest podane w poprawny sposob
    if Key=="~":
        return

    Option=others.changeEncoding(Key,Pad)
    # dostowuje kodowanie do charakterystyki klucza

    Verification=KeyAction.hideKey(Key,Pad,File,Option)
    # zapisuje klucz do pliku ze steanogramem
    if Verification=="~":
        return

####################################################################################

def findInformation():
    Source=printInformation.question("Podaj nazwe pliku ze steanogramem")
    # pobierara nazwe pliku z steanogramem,
    Source=fileAction.setPathToFile(Source)
    # ustala scieszke bezwzgledna do niego
    Pad=fileAction.openFile(Source)
    #  sprawdza czy istnieje i jezeli tak, to pobiera jego zawartosc
    if Pad=="~":
        return

    Key=KeyAction.readKey(Pad)
    # odczytuje klucz steanogramu

    Key=spaceAction.delZero(Key)
    # usowa nadmiarowe nadmiarowew zera z 
    if Key[0]=="~":
        return

    Kod=printInformation.question("Podaj chaslo")
    # pobiera chaslo do odszyfrowania klucza i
    Key=others.encryption(Key,Kod)
    # sprawdza czy jest podane w poprawny sposob
    if Key=="~":
        return

    # zamienia steanogram na postać dziesietna
    Key=binaryAction.binToDeci(Key)

    print("Tajna wiadomosc to:")
    print(textAction.readText(Key,Pad))
    # odczytuje tajna wiadomosc i wyswietla ja

####################################################################################

def main():
    while True:
    # nieskonczaoana petla dzialania programu
        Option=printInformation.mainMenu()
        # pobiera opcje wybrana przez urzytkownika

        if Option==1:
            hideInformation()
            # przelacza program w tryb do ukrywania informacji
        elif Option==2:
            findInformation()
            # przelacza program w tryb do odczytu ukrytej injformacji
        elif Option==3:
            exit()
            # wylacza program

if __name__=="__main__":
    main()