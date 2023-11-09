import random
import math
'''Kérj be 1 páros számot a felhasználótól. (1 pont)
Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)'''
def elso_feladat():
    paros_szam:int=int(input("Kérek egy páros számot! "))
    while not (paros_szam %2 ==0 ):
        paros_szam:int=int(input("Ez nem páros! Páros számot kérek!"))
    print(f"{paros_szam} egy páros szám")
    print("")

'''Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!'''
def masodik_feldat():
    i:int=0
    harommal_oszthato:int=0
    while i<13:
        szamok: int = math.floor(random.random() * (150 - 10) + 10)
        print(szamok, end=" ")
        i +=1
        if szamok % 3 ==0:
            harommal_oszthato+=1
    print("")
    print(f"A számok között {harommal_oszthato} db 3-mal osztható van!")
    print("")

def harmadik_feladat(txt, n):
    txt:str=""
    n:int=0
    szoveg_hossz:int=len(txt)
    negyedik:str=txt.find()
    if n > len(txt):
        print(f"Nincs {n} karakter!")
    elif n < szoveg_hossz:

        print(f"A szöveg 4. karaktere {negyedik} - {negyedik.upper()}")

'''Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
Hány nevet adott meg a felhasználó?
A kiírás formája: „A felhasználó 12 nevet adott meg.'''

def negyedik_feldat():
    nevek:str=str(input("Kérek egy nevet, vagy állistd meg @ jelel: "))
    szamlalo:int=0
    while not (nevek == "@"):
        nevek: str = str(input("Kérek egy nevet, vagy állistd meg @ jelel: "))
        szamlalo +=1
    print(f"A felhasználó {szamlalo} nevet adott meg.")
    print("")

'''Szimuláljuk a kő-papír-olló játékot. 
Írj eljárást, amiben: 
A felhasználótól bekérjük a tippjét, ami kő/papír/olló lehet. Alakítsd át csupa kisbetűssé a szöveget, majd tárold el a felhasznalo_tippje változóban. 
Ezután a gép generál egy egész számot [1,3] között.  1- kő, 2- papír – 3 olló. Tárold el a gep_tippje változóban
Ezután írd ki, hogy ki nyert!
	Ha a két szó ugyanaz, írja ki, hogy Döntetlen. 
	Egyéb esetben azt írja ki, aki győzött!
++ Ha valami más szót ad meg a felhasznló  a kő, papír, ollón kívül, akkor kérje be újra!
'''
def otodik_feldat():
    beker: str = str(input("Kő-papír-olló játék. Add meg a tippedett: "))
    felhasznalo_tippje: str = beker.casefold()
    gep_tippje:str=""
    while not(beker=="kő" or beker=="papír" or beker=="olló"):
        beker: str = str(input("Kő-papír-olló játék. Add meg a tippedett: "))
        felhasznalo_tippje: str = beker.casefold()
    random_tipp:int=math.floor(random.random()*(1-3)+3)
    print(random_tipp)
    if random_tipp == 1:
        gep_tippje= "kő"
    elif random_tipp==2:
        gep_tippje="papír"
    elif random_tipp==3:
        gep_tippje="olló"
    if gep_tippje == felhasznalo_tippje:
        print("Döntetlen")

    elif gep_tippje == "kő" and felhasznalo_tippje=="papír":
        print("A felhasználó gyözött")
    elif gep_tippje == "kő" and felhasznalo_tippje == "olló":
        print("A gép gyözött")
    elif gep_tippje == "papír" and felhasznalo_tippje == "kő":
        print("A felhasználó gyözött")
    elif gep_tippje == "papír" and felhasznalo_tippje == "olló":
        print("A felhasználó gyözött")
    elif gep_tippje == "olló" and felhasznalo_tippje == "kő":
        print("A gép gyözött")
    elif gep_tippje == "olló" and felhasznalo_tippje == "papír":
        print("A gép gyözött")