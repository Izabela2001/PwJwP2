from TrzecieZajęcia.Zadanie1.AnalizaJezykowa import AnalizaJezykowa
from TrzecieZajęcia.Zadanie1.Asystent import Asystent
from TrzecieZajęcia.Zadanie1.GeneratorOdpowiedzi import GeneratorOdpowiedzi


class InteligentnyAsystent(Asystent):
    def __init__(self, nazwa, wersja):
        super().__init__(nazwa, wersja)
        self.analizator = AnalizaJezykowa()
        self.generator = GeneratorOdpowiedzi()

    def odpowiedz_na_zapytanie(self, zapytanie):
        analiza = self.analizator.analizuj_zapytanie(zapytanie)
        odpowiedz = self.generator.generuj_odpowiedz(analiza)
        return odpowiedz

# Test działania asystenta
asystent = InteligentnyAsystent("Twój super asystent", "v2.0")
zapytanie = "Jaka jest dzisiaj ?"
print(asystent.odpowiedz_na_zapytanie(zapytanie))