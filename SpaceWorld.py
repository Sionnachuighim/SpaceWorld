from random import *

class Attraktion:

    def __init__(self, namn, magpirrFaktor): 
        self.namn = namn
        self.magpirrFaktor = magpirrFaktor

    def slumpOrd(self):
        o = ['läskigaste', 'roligaste', 'häftigaste', 'spännande', 'coolaste' ]
        return o[randrange(len(o))]        

    def reklam(self):
        print()
        print("Välkommen till den " + self.slumpOrd() + " attraktionen " + self.namn + ". Åkturen har blivit klassificerad med " + str(self.magpirrFaktor) + " på magpirr-listan.\n")

    def start(self):
        print("Attraktionen startar")

    def stopp(self):
        print("Attraktonen har stoppats, tack för att du åkte med " + self.namn + ".\n")

    def haveri(self):
        print("Åh, nej! Attraktionen har gått sönder.\n")       


    def kor(self):
        print()
        self.start()
        print()
        antal = randrange(1,7)
        if antal == 6:
            self.haveri()
        elif antal < 4:
            print("Wiiee! Vad roligt det var!\n")
        else:
            print("Usch, det var inte alls roligt!\n")
        self.stopp()
        print()

class SpaceWorld:

    def intro(self):
        print("Välkommen till Space World! Ett nöjesfält du aldrig har skådat innan!\n")

        self.listaAttraktioner()

    def listaAttraktioner(self):
        lista = dict()
        lista['maskhålet'] = Attraktion('Maskhålet', 6)
        lista['andromeda'] = Attraktion('Andromeda', 8)
        lista['hemsöktaherrgården'] = Attraktion('HemsöktaHerrgården', 4)

        while True:
            print("Detta är våra attraktioner:\n")
            print("(M)askhålet")
            print("(A)ndromeda")
            print("(H)emsöktaHerrgården")
            print()
            print("För mer information om våra attraktioner, skriv i + en tillhörande bokstav. Tex. i+M")
            
            print()
            svar = input("Vad vill du åka för någon attraktion?\n")
            svar = svar.strip()                                                                     
            if(svar == "i+m" or svar == "i+M"): lista['maskhålet'].reklam()
            elif(svar == "i+a" or svar == "i+A"): lista['andromeda'].reklam()
            elif(svar == "i+h" or svar == "i+H"): lista['hemsöktaherrgården'].reklam()
            elif(svar == "m" or svar == "M"):
                lista['maskhålet'].kor();                                                          
            elif(svar == "a" or svar == "A"):
                lista['andromeda'].kor();                                                          
            elif(svar == "h" or svar == "H"):
                lista['hemsöktaherrgården'].kor();                                                 
            else: print("Jag förstår inte vad du säger!")


spaceworld = SpaceWorld()
spaceworld.intro()
