####################################################################################

def isLen3(Binar):
    if len(Binar)==3:
    # sprawdza czy pozycja litery w zapisie binarnym ma dokladnie 3 znaki
        return list(Binar)
        # zwraca nie zmieniony ciag

    while len(Binar)<3:
    # jezeli ma mniej to dodaje na poczatku 0, do momentu uzyskania 3 znakow
        Binar="0"+Binar

    return list(Binar)
    # zwraca zmodyfikowany ciag

####################################################################################

def decToBin(Key):
    Binar=[]

    for Number in Key:
    # iteruje po kolejnych liczbach z klucza,
        Binar=Binar+(isLen3(bin(Number).replace("0b","")))
        # zamienia je postac binarna i wyrownuje ich dlugosc do trzech

    return Binar
    # zwraca klucz w wersji binarnej

####################################################################################

def binToDeci(Key):
    Tab=[]
    Iterator=3
    # ustawiamy iterator na 3 pozycji

    while Iterator<=len(Key):
    # iteruje po kolejnych trojkach bitow z klucza
        Tab.append(4*int(Key[Iterator-3])+2*int(Key[Iterator-2])+int(Key[Iterator-1]))
        # mnozy je przez kolejne potegi 2 i dodaje do siebie
        Iterator+=3
        # przesuwa iterator o trzy bity

    return Tab
    # zwraca klucz w wersji decymalnej