from typing import List
### FUNCIONES ###
def calculo_distancia_euclidiana(arr1: List, arr2: List) -> float:
    return sum((x1 - x2) ** 2 for x1, x2 in zip(arr1, arr2)) ** 0.5