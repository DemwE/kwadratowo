import matplotlib.pyplot as plt
import numpy as np
from module import FunkcjaKwadratowa

# Tworzenie funkcji
f = FunkcjaKwadratowa(1, 1, -6, forma="ogólna")

# Wyświetlenie funkcji w różnych postaciach:
print(f"Postac ogólna: {f.postac_ogolna()}")
print(f"Postac kanoniczna: {f.postac_kanoniczna()}")
print(f"Postac iloczynowa: {f.postac_iloczynowa()}")

# Obliczenie miejsc zerowych funkcji kwadratowej
pierwiastki = f.pierwiastki()
if pierwiastki:
    print(f"Miejsca zerowe funkcji: {pierwiastki}")
else:
    print("Brak miejsc zerowych funkcji.")

# Obliczenie wartość funkcji w punkcie x = 2
print(f"Wartość funkcji w punkcie f(x) = 2: {f.wartosc_punktu(2)}")

# Wyświetlenie współczynników funkcji
print(f"Współczynniki funkcji: a = {f.a}, b = {f.b}, c = {f.c}")

# Wyświetlanie przedziału wartości funkcji
print(f"Przedział wartości funkcji: {f.przedzial_wartosci()}")

# Wyświetlenie przedziały monotoniczności funkcji
print(f"Przedziały monotoniczności funkcji: {f.monotonicznosc()}")

# Generowanie danych do wykresu
x = np.linspace(-10, 10, 400)
y = f.wartosc_punktu(x)

# Rysowanie wykresu
plt.plot(x, y, label=f.postac_ogolna())
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji kwadratowej')
plt.legend()

# Zapisanie wykresu do pliku
plt.savefig('wykres_funkcji_kwadratowej.png')
plt.show()