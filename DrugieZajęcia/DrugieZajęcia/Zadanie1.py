class Ksiazka:
    def __init__(self, tytul, author, rok_wydania):
        self.tytul = tytul
        self.author = author
        self.rok_wydania = rok_wydania

    def opis(self):
        return f"{self.tytul} {self.author} {self.rok_wydania}"

class Ebook(Ksiazka):
    def __init__(self, tytul, author, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, author, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return f"{super().opis()} {self.rozmiar_pliku}"
class Audiobook(Ksiazka):
    def __init__(self, tytul, author, rok_wydania,czas_trwania):
        super().__init__(tytul, author, rok_wydania)
        self.czas_trwania = czas_trwania

    def opis(self):
        return f"{super().opis()} {self.czas_trwania}"

ebook1 = Ebook("tytul1", "autor1", 2001, 256)
ebook2 = Ebook("tytul2", "autor2", 2015, 478)

audiobook1 = Audiobook("tytul1", "autor1", 2001, 256)
audiobook2 = Audiobook("tytul2", "autor2", 2015, 78)

print("Eboki")
print(ebook1.opis())
print(ebook2.opis())
print("AudiobookI")
print(audiobook1.opis())
print(audiobook2.opis())
