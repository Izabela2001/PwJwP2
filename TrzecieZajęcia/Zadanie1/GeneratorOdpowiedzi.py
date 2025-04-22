class GeneratorOdpowiedzi:
    def generuj_odpowiedz(self, analiza):
        odpowiedzi = {
            "pogoda": "Dzisiaj jest słonecznie z temperaturą 20°C.",
            "czas": "Aktualny czas to 14:30.",
            "data": "Dzisiejsza data to 25 marca 2025.",
            "informacja": "Jaką informację potrzebujesz?"
        }
        for klucz in odpowiedzi:
            if klucz in analiza:
                return odpowiedzi[klucz]
        return "Przykro mi, ale nie mam odpowiedzi na to pytanie."
