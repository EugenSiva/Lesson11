class LinkedList:
    def __init__(self):
        self.head = None

    def vloz_prvok(self, prvok):
        if self.head == None:
            self.head = prvok
        else:
            aktualny = self.head
            while aktualny.dalsi_prvok != None:
                aktualny = aktualny.dalsi_prvok
            aktualny.dalsi_prvok = prvok

    def vypis_vsetky(self):
        aktualny = self.head
        while aktualny.dalsi_prvok != None:
            print(aktualny.data)
            aktualny = aktualny.dalsi_prvok

        print(aktualny.data)

class Prvok:
    def __init__(self, data):
        self.data = data
        self.dalsi_prvok = None


prvok1 = Prvok(15)
prvok2 = Prvok("Eugen")
prvok3 = Prvok(23.8)

moj_zoznam = LinkedList()
moj_zoznam.vloz_prvok(prvok1)
moj_zoznam.vloz_prvok(prvok2)
moj_zoznam.vloz_prvok(prvok3)

moj_zoznam.vypis_vsetky()