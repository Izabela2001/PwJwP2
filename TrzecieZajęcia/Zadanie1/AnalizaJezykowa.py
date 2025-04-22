class AnalizaJezykowa:
    def analizuj_zapytanie(self, zapytanie):
        # Prosta analiza: wykrywa słowa kluczowe
        kluczowe_slowa = ["pogoda", "czas", "data", "informacja"]
        for slowo in kluczowe_slowa:
            if slowo in zapytanie.lower():
                return f"Zapytanie dotyczy: {slowo}"
        return "Nie rozpoznano intencji."