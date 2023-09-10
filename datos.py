import networkx as nx
from time import time
from copy import copy
from itertools import tee
from numpy import exp, ndarray
from random import randint
from statistics import median
from time import time
from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
## generar datos aleatorio
def gen_data(minimo, maximo, n_filas, n_columnas=None): #
    if n_columnas is None:
        ret = [randint(minimo, maximo) for _ in range(n_filas)]
    else:
        ret = [[randint(minimo, maximo) for _ in range(n_columnas)]
            for _ in range(n_filas)]
    return ret

## importar datos dataset
def imp_data(dato): #
    archivo = 'Iris_Excel_datos.xlsx'
    df = pd.read_excel(archivo, sheet_name='Iris')
    npArray = df.to_numpy()
    print(npArray)
    puntos = list()
    if dato =='Puntos':
        i=0
        for pto in npArray:
            #puntos[i][0] = pto[1]
            punto = [pto[1],pto[2]] #,pto[3],pto[4])
            puntos.append(punto)
            i +=1
        return puntos
    if dato =='Discriminante':
        return [1,1]

## importa dataset
def imp_data_excel():
    archivo = 'customersXLS.xlsx'
    df = pd.read_excel(archivo, sheet_name='marketing')
    print(df)
    #plt.bar(df['Kidhome'],df['Teenhome'])
    #plt.show()

    npArray = df.to_numpy()
    print(npArray)


def imp_Iris():
    iris_ds = datasets.load_iris()
    df = pd.DataFrame(iris_ds.data, columns=iris_ds.feature_names)
    #df['target'] = iris_ds.target
    print(df)
    
def gen_iris(dato): #
    archivo = 'Iris_Excel_datos.xlsx'
    df = pd.read_excel(archivo, sheet_name='Iris')
    npArray = df.to_numpy()
    print(npArray)
    puntos = list()
    id_puntos = list()
    # 4k
    if dato =='1111':
        for pto in npArray:
            punto = [pto[1],pto[2],pto[3],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    # 3k
    if dato == '1110':
        for pto in npArray:
            punto = [pto[1],pto[2],pto[3],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1101':
        for pto in npArray:
            punto = [pto[1],pto[2],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1011':
        for pto in npArray:
            punto = [pto[1],pto[3],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '0111':
        for pto in npArray:
            punto = [pto[2],pto[3],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos           
    # 2k
    if dato == '0011':
        for pto in npArray:
            punto = [pto[3],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos          
    if dato == '0110':
        for pto in npArray:
            punto = [pto[2],pto[3],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1010':
        for pto in npArray:
            punto = [pto[1],pto[3],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1100':
        for pto in npArray:
            punto = [pto[1],pto[2],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    # 1k
    if dato == '0001':
        for pto in npArray:
            punto = [pto[4]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1000':
        for pto in npArray:
            punto = [pto[1],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '0010':
        for pto in npArray:
            punto = [pto[3],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '0100':
        for pto in npArray:
            punto = [pto[2],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos

def gen_iris_prueba(dato): #
    archivo = 'Iris_Excel_pruebas.xlsx'
    df = pd.read_excel(archivo, sheet_name='Iris')
    npArray = df.to_numpy()
    print(npArray)
    puntos = list()
    id_puntos = list()
    # 4k
    if dato =='1111':
        for pto in npArray:
            punto = [pto[1],pto[2],pto[3],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    # 3k
    if dato == '1110':
        for pto in npArray:
            punto = [pto[1],pto[2],pto[3],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1101':
        for pto in npArray:
            punto = [pto[1],pto[2],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1011':
        for pto in npArray:
            punto = [pto[1],pto[3],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '0111':
        for pto in npArray:
            punto = [pto[2],pto[3],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos           
    # 2k
    if dato == '0011':
        for pto in npArray:
            punto = [pto[3],pto[4],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos          
    if dato == '0110':
        for pto in npArray:
            punto = [pto[2],pto[3],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1010':
        for pto in npArray:
            punto = [pto[1],pto[3],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1100':
        for pto in npArray:
            punto = [pto[1],pto[2],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    # 1k
    if dato == '0001':
        for pto in npArray:
            punto = [pto[4]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '1000':
        for pto in npArray:
            punto = [pto[1],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '0010':
        for pto in npArray:
            punto = [pto[3],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos
    if dato == '0100':
        for pto in npArray:
            punto = [pto[2],pto[5]] #,pto[3],pto[4])
            puntos.append(punto)
            id_punto = [pto[0],pto[5]] 
            id_puntos.append(id_punto)
        return puntos


