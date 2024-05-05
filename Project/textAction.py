
####################################################################################

def hideText(Text,Pad):
    Key=[]
    # zmienna w, ktorej zapisywany jest klucz steanogramu
    Iterator=0

    Text=Text.lower()
    # zamienia wszsystkie litery w tekscie na male

    for Line in Pad:
    # iteruje po liniach w tekscie podkladki

        Tab=Line.lower().split()
        # dzieli linie na slowa i zamienia litery na male

        for Word in Tab:
        # iteruje po slowach w linii
            if Iterator<len(Text):
                if Word.rfind(Text[Iterator])<7:
                    # jezeli znajdzie w slowie litere odpowiadajaca liteze tekstu ukrytego
                    Key.append(Word.rfind(Text[Iterator])+1)
                    # to dodaje do klucza jej pozycje w slowie
                    if Key[len(Key)-1]!=0:
                        Iterator+=1
                    # jezeli nie to do klucza dodaje wartosc 0
                    # jezeli pozycja litery jest mniejsza niz 7
                else:
                    Key.append(0)
                    # jezeli nie to do klucza dodaje 0

    if Iterator<len(Text):
    # sprawdza czy zapisano cala podana informacje
        print("Zabraklo znakow dla infomacji")
        # jezeli nie to zwraca blad
        return ["~"]

    return Key
    # zwraca klucz

####################################################################################

def readText(Key,Pad):
    Result=""
    # zmienna w ktorej zapisywany jest ukryty tekst
    Iterator=0

    for Line in Pad:
    # iteruje po liniach w steanogramie

        if Iterator>len(Key):
            break
            # pomja linie jezeli odczytal juz wszystkie znaki

        Line=Line[:len(Line)-1]
        # usow znak enter z konca linii

        Tab=Line.lower().split(" ")
        # dzieli linie na słowa

        for Word in Tab:
        # iteruje po slowach w linii
            if Word!="":
            # sprawdza czy slowo zawiera jakiekolwiek litery
                
                if Iterator<len(Key) and Key[Iterator]>0 and Key[Iterator]<=len(Word):
                # jezeli dana pozycja klucza jest wieksza niz 0,
                    Result+=Word[Key[Iterator]-1]
                    # to dodaje do klucza jej pozycje w slowie

                Iterator+=1
                # inkrementuje iterator

    return Result
    # zwrasca ukryta infomacje