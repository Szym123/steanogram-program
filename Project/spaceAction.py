####################################################################################

def delZero(Key):
    Iterator=len(Key)-1
    # Ustrawiamy iterator na koncu klucza w zapisie binarnym

    try:
        while Key[Iterator]=="0":
        # iteruje po kluczu od tyłu w poszukiwaniu pierwszej napotkanej 1 
            Iterator-=1

        while Iterator%3!=2:
            Iterator+=1
            # przesuwa się do przodu
            # w poszukiwaniu konca ostatniej istotnej trujki bitow klucza

        if Iterator==len(Key)-1:
            return Key
            # jezeli iterator znalazl sie na koncu klucza to zwraca caly klucz

        return Key[:Iterator+1]
        # jezeli iterator nie znalazl sie na koncu to usowa wszystkie nadmiarowe 0
        # znajdujace sie za ostatnia istotna trujka bitow

    except:
        print("Problem z steanogramem")
        # jezeli wysapi jakikolwiek problem z zmodyfikowaniem klucza
        # to zwruci blad
        return ["~"]

####################################################################################

def spaceSum(Counter,Option):
# uzaleznia stan bitu od ilosci spacji

    if Option==0:
    # dla pocji 0 odczytujemy spacje w kodowaniu podstawowym
        if Counter==1:
        # dla 1 spacji przypisujemy 0
            return "0"
        elif Counter==2:
        # dla 2 spacji przypisujemy 1
            return "1"

    elif Option==1:
    # dla pocji 1 odczytujemy spacje w kodowaniu odwrotnym
        if Counter==1:
        # dla 1 spacji przypisujemy 1
            return "1"
        elif Counter==2:
        # dla 2 spacji przypisujemy 0
            return "0"