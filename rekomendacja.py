#  Wzorowane na przykładzie Rona Zacharskiego
#
import numpy
from math import sqrt

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
    rating1 = users[rating1]
    rating2 = users[rating2]
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    [sx, sy, sxy, sxk, syk, n] = [0]*6
    for klucz in users[rating1].keys():
        if klucz in users[rating2].keys():
            sx += users[rating1][klucz]
            sy += users[rating2][klucz]
            sxy += users[rating1][klucz]*users[rating2][klucz]
            sxk += users[rating1][klucz]*users[rating1][klucz]
            syk += users[rating2][klucz]*users[rating2][klucz]
            n += 1
    korelacja = (sxy - (sx*sy)/n) / ( sqrt(sxk - sx*sx/n) * sqrt(syk - sy*sy/n) )
    return korelacja

def pearsonNumpy(rating1, rating2):
    korelacja = 0
    x = []
    y = []
    for klucz in users[rating1].keys():
        if klucz in users[rating2].keys():
            x.append(users[rating1][klucz])
            y.append(users[rating2][klucz])
    cxy = numpy.corrcoef(x,y)
    korelacja = cxy[0,1]
    return korelacja

print manhattan("Ania", "Bonia")
print pearson("Ania", "Bonia")
print pearsonNumpy("Ania","Bonia")
