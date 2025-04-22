def pole_kwadratu(bok):
    return bok ** 2

def obwod_kwadratu(bok):
    return 4 * bok

def pole_prostokata(a, b):
    return a * b

def obwod_prostokata(a, b):
    return 2 * (a + b)

def pole_kola(promien):
    from math import pi
    return pi * promien ** 2

def obwod_kola(promien):
    from math import pi
    return 2 * pi * promien

# geompy/figury3d.py
def objetosc_szescianu(bok):
    return bok ** 3

def pole_szescianu(bok):
    return 6 * bok ** 2

def objetosc_prostopadloscianu(a, b, h):
    return a * b * h

def pole_prostopadloscianu(a, b, h):
    return 2 * (a*b + a*h + b*h)

def objetosc_kuli(promien):
    from math import pi
    return 4/3 * pi * promien ** 3

def pole_kuli(promien):
    from math import pi
    return 4 * pi * promien ** 2

from geompy import figury2d, figury3d

print("Pole kwadratu 5x5:", figury2d.pole_kwadratu(5))
print("Obwod kola r=3:", figury2d.obwod_kola(3))
print("Objetosc kuli r=2:", figury3d.objetosc_kuli(2))
print("Pole prostopadloscianu 2x3x4:", figury3d.pole_prostopadloscianu(2, 3, 4))
