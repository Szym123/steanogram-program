import fileAction
import spaceAction
import others

####################################################################################

def hideKey(Key,Pad,Name,Option):
    Iterator=0
    SpaceZero=""
    SpaceOne=" "

    if Option==1:
    # jezeli w kluczu jest wiecej bitow o stanie 1, to zmienie kodowanie na odwrotne
        fileAction.saveEdit(Name," ")
        # zapisuje fakt zmiany przy pomocy spacji na samym poczatku pierwszej linii
        SpaceZero=" "
        SpaceOne=""

    for Line in Pad:
    # iteruje po liniach w podkladce

        Words=Line.split(" ")
        # dzieli linie na slowa

        fileAction.saveEdit(Name,others.deleteEnter(Words[0]))
        # zapisuje pierwszy wyraz z linii
        # jezeli wystepuje to usuwa enter z konca wyrazu

        del Words[0]
        # przenosi pierwsze slowo do pliku z steanogramem

        for Item in Words:
        # iteruje po slowach rozpoczynajac od pierwszego

            Item=others.deleteEnter(Item)
            # jezeli wystepuje to usuwa enter z konca wyrazu

            if Iterator<len(Key):
            # sprawda, czy iterator miesci sie w zakresie klucza
            # jezeli tak, to:
                if Key[Iterator]=="0":
                    fileAction.saveEdit(Name," "+SpaceZero)
                # przypisuje 0 pojedzyncza spacje
                elif Key[Iterator]=="1":
                    fileAction.saveEdit(Name," "+SpaceOne)
                # natomiast 1 podwujna spacje

            else:
                fileAction.saveEdit(Name," ")
            # jezeli iterator wyszedl poza zakres klucza,
            # to wstawia pojedyncza spacje

            fileAction.saveEdit(Name,Item)
            # zapisuje kolejne slowo do pliku

            Iterator+=1
            # inkrementuje iterator

        if Iterator<len(Key):
        # sprawdza czy wartosc iteratora miewsci sie w zakrasie klucza
            if Key[Iterator]=="0":
                # jezeli wartosc bitu na, którym jest iterator jest równa 0
                # wtedy na koncu linii dodawana jest ilosc spacji odpowiadajaca przyjetemu kodowaniu
                fileAction.saveEdit(Name,SpaceZero)
            if Key[Iterator]=="1":
            # jezeli wartosc bitu na, którym jest iterator jest równa 1
            # wtedy na koncu linii dodawana jest ilosc spacji odpowiadajaca przyjetemu kodowaniu
                fileAction.saveEdit(Name,SpaceOne)

        fileAction.saveEdit(Name,"\n")
        # dodaje znak enter na koncu linii

        Iterator+=1
        # inkrementuje iterator

    if Iterator<len(Key):
    # po zakonczeniu iterowania po tekscie z podkladki
    # sprawdza czy jakas czesc klucza pozostala niezapisana
        print("Za krutka podkaladka")
        return "~"
        # jezeli to zwraca blad

    return "."

####################################################################################

def readKey(Pad):
    Key=[]
    Counter=0
    Option=0

    if Pad[0][0]==" ":
    # sprawdza czy nie zostal zasosowany odwrucony zapis bitow
        Pad[0]=Pad[0][1:]
        Option=1
        # jesli tak to spacje z poczatku i zmienia tryb odczytu

    for Line in Pad:
    # iterujemy po liniach w steanogranie

        Line=Line[:len(Line)-1]
        # usowa z końca linii znak entera

        for Char in Line:
        # iterujemy po znakach w linii
            if Char==" ":
            # jezeli dany znak to spacja, to zwiekszamy licznik o 1
                Counter+=1
            else:
            # jezeli nie, to sprawdzamy jaka jest wartosc na liczniku
            # dla 1 do klucza dodajemy 0
            # dla 2 dodajemy 1
                if Counter in [1,2]:
                    Key.append(str(spaceAction.spaceSum(Counter,Option)))
                    # zerujemy licznik
                    Counter=0

        Key.append(str(spaceAction.spaceSum(Counter+1,Option)))
        Counter=0
        # po przeiterowaniu sprawdzamy ilość spacji doklejonuch na końcu linii

    return Key