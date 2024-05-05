####################################################################################

def changeEncoding(Key,Pad):
    Sum=0
    SumOne=0

    for Line in Pad:
    # zlicza ilosc spacji w podkladce
        Sum+=len(Line.split(" "))

    for Char in Key:
    # zlicza wystapienia 1 w binarnym zapisie klucza
        if Char=="1":
            SumOne+=1

    if Sum-SumOne<SumOne:
    # jezeli liczba jedynek jest wieksza, to zwraca 1
        return 1

    return 0
    # jezeli nie to zwraca 0

####################################################################################

def encryption(Key,Kod):
    Iterator=0
    Key=list(Key)
    # zamienia klucz ze stringa na liste w celu ułatwienia operacji

    try:
    # jezeli dziala poprawnie

        Kod=list(str(bin(int(Kod)).replace("0b","")))
        # zamienia haslo na liste binarna

        while Iterator<len(Key):
        # iteruje po bitach klucza wykonujac funkcje OR
            if Kod[Iterator%len(Kod)]=="1":
                Key[Iterator]=str((int(Key[Iterator])+int(Kod[Iterator%len(Kod)]))%2)
                # jezeli bit chasla ma wartosc 1, to zamienia bit klucza na przeciwny

            Iterator+=1
            # inkrementuje iterator

        return Key
        # zwraca zaszyfrowany klucz steanogramu

    except:
        print("Bledne chaslo")
        # przerywa funkcje, jezeli wystapia jakiekolwiek problemy z kluczem
        return "~"

####################################################################################

def isSizeOk(Text,Pad):
    Sum=0

    for Line in Pad:
    # zlicza ilosc spacji w podkaldce
        Sum+=len(Line.split(" "))
    
    if Sum<3*len(Text):
    # sprawadza klucz w zapisie binarnym ma wiecej znakow od ilosci spacji w podkladce
        print("Podkladka jest za mala")
        # jezeli tak to zwraca blad
        return "~"
    
    return "."

####################################################################################

def deleteEnter(Text):
    if Text[len(Text)-1]=="\n":
    # sprawedza czy na koncu stringa wystepuje znak spacji
        return Text[:len(Text)-1]
        # jezeli jest to go usowa i zwraca string

    return Text
    # jezeli nie to zwraca niezmodyfikowany string