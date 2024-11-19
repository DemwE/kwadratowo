import math
from typing import Tuple, Union, Optional
import numpy as np


def _format_liczba(wspolczynnik: float) -> Union[int, float]:
    """Sprawdzanie, czy wspolczynnik może być przekonwertowany do int (czy jest liczbą całkowitą)."""
    if wspolczynnik == int(wspolczynnik):
        return int(wspolczynnik)  # Konwertuj na int, jeśli liczba jest całkowita (np. 2.0)
    return wspolczynnik  # W przeciwnym razie zwróć oryginalną liczbę


def _format_wspolczynnik(wspolczynnik: float) -> str:
    """Pomocnicza funkcja do formatowania współczynnika z odpowiednim znakiem."""
    wspolczynnik = _format_liczba(wspolczynnik)  # Przekształć współczynnik na int, jeśli to możliwe

    if wspolczynnik >= 0:
        return f"+ {wspolczynnik}"
    else:
        return f"- {-wspolczynnik}"


class FunkcjaKwadratowa:
    def __init__(self, *args: float, forma: str = "ogólna"):
        """
        Inicjalizuje funkcję kwadratową w jednej z trzech form:
        'ogólna', 'kanoniczna', 'iloczynowa'.
        """
        self.forma = forma

        if forma == "ogólna":
            self.a, self.b, self.c = args  # Przyjmuje współczynniki w postaci ogólnej
        elif forma == "kanoniczna":
            self.a = args[0]
            p = args[1]
            q = args[2]
            self.b = -2 * self.a * p  # Oblicza b z postaci kanonicznej
            self.c = self.a * p ** 2 + q  # Oblicza c z postaci kanonicznej
        elif forma == "iloczynowa":
            self.a = args[0]
            x1, x2 = args[1], args[2]
            self.b = -(x1 + x2)  # Oblicza b z postaci iloczynowej
            self.c = x1 * x2  # Oblicza c z postaci iloczynowej
        else:
            raise ValueError(f"Błędna forma funkcji: {forma}")

    @property
    def p(self) -> float:
        return -self.b / (2 * self.a)

    @property
    def q(self) -> float:
        return self.wartosc_punktu(self.p)

    def postac_ogolna(self) -> str:
        """Zwraca funkcję w postaci ogólnej."""
        return f"f(x) = {self.a}x² {_format_wspolczynnik(self.b)}x {_format_wspolczynnik(self.c)}"

    def postac_kanoniczna(self) -> str:
        """Zwraca funkcję w postaci kanonicznej."""
        return f"f(x) = {self.a}(x {_format_wspolczynnik(-self.p)})² {_format_wspolczynnik(self.q)}"

    def postac_iloczynowa(self) -> Optional[str]:
        """Zwraca funkcję w postaci iloczynowej."""
        pierwiastki = self.pierwiastki()
        if pierwiastki is None:
            return None  # Brak pierwiastków
        x1, x2 = pierwiastki
        return f"f(x) = {self.a}(x {_format_wspolczynnik(-x1)})(x {_format_wspolczynnik(-x2)})"

    def wartosc_punktu(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """Zwraca wartość funkcji w punkcie x."""
        return self.a * x ** 2 + self.b * x + self.c

    def pierwiastki(self) -> Optional[Union[float, Tuple[float, float]]]:
        """Oblicza pierwiastki funkcji kwadratowej."""
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta < 0:
            return None  # Brak pierwiastków
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return _format_liczba(x)  # Jeden pierwiastek
        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return _format_liczba(x1), _format_liczba(x2)  # Dwa pierwiastki

    def wspolczynniki(self) -> Tuple[float, float, float]:
        """Zwraca współczynniki funkcji kwadratowej."""
        return self.a, self.b, self.c

    def przedzial_wartosci(self) -> str:
        """Zwraca przedział wartości funkcji kwadratowej."""
        if self.a > 0:
            return f"<{_format_liczba(self.q)}; ∞)"
        else:
            return f"(-∞; {_format_liczba(self.q)}>"

    def monotonicznosc(self) -> str:
        """Zwraca przedział monotoniczności funkcji kwadratowej."""
        if self.a > 0:
            return f"(-∞, {_format_liczba(self.p)}) - malejąca, ({_format_liczba(self.p)}, ∞) - rosnąca"
        else:
            return f"(-∞, {_format_liczba(self.p)}) - rosnąca, ({_format_liczba(self.p)}, ∞) - malejąca"