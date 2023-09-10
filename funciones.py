from typing import List
from time import time
import matplotlib.pyplot as plt
from clases import KDTree
from datos import gen_data
#from datos import imp_data_excel
#from datos import imp_data
#from datos import imp_Iris
from datos import gen_iris
from datos import gen_iris_prueba
from funciones2 import calculo_distancia_euclidiana
from graficos  import graficardor_puntos_iris



########## FUNCION PRINCIPAL #######
def principal(sepalo_longitud,sepalo_ancho,petalo_longitud,petalo_ancho,modo_prueba):
    print("Resultados de pruebas")
    #configuracion de pruebas aleatorias, si queremos nuestro dataset ponemos genera_datos_aleatorios = False
    cantidad_pruebas = 1
    tiempo_calculo= 0
    opcion_graficar_puntos =True
    genera_datos_aleatorios = False
    generador='0000'
    discriminante = gen_data(0, 100, 135)# 135 de conocimiento y 15 de prueba 
    
    if (sepalo_longitud ==0 and sepalo_ancho ==0 and petalo_longitud == 0 and petalo_ancho == 0 ):
        print('No se puede realizar el analisis DATOS INCOMPLETOS 0000')
    elif (sepalo_longitud ==0 and sepalo_ancho ==0 and petalo_longitud == 0 and petalo_ancho > 0 ):
        generador ='0001'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[petalo_ancho]
        n_columnas = 1 # dimension
    elif (sepalo_longitud ==0 and sepalo_ancho ==0 and petalo_longitud > 0 and petalo_ancho == 0 ):
        generador ='0010'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[petalo_longitud]
        n_columnas = 1 # dimension
    elif (sepalo_longitud ==0 and sepalo_ancho >0 and petalo_longitud == 0 and petalo_ancho == 0 ):
        print('Analsisis 1k 0100')
        generador ='0100'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[sepalo_ancho]
        n_columnas = 1 # dimension
    elif (sepalo_longitud >0 and sepalo_ancho ==0 and petalo_longitud == 0 and petalo_ancho == 0 ):
        print('Analsisis 1k 1000')     
        generador ='1000'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[sepalo_longitud]
        n_columnas = 1 # dimension   
    elif (sepalo_longitud >0 and sepalo_ancho ==0 and petalo_longitud > 0 and petalo_ancho == 0 ):
        print('Analsisis 2k 1010')
        generador ='1010'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[sepalo_longitud,petalo_longitud]
        n_columnas = 2 # dimension
    elif (sepalo_longitud >0 and sepalo_ancho >0 and petalo_longitud == 0 and petalo_ancho == 0 ):
        print('Analsisis 2k 1100')
        generador ='1100'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[sepalo_longitud,sepalo_ancho]
        n_columnas = 2 # dimension
    elif (sepalo_longitud ==0 and sepalo_ancho ==0 and petalo_longitud > 0 and petalo_ancho > 0 ):
        print('Analsisis 2k 0011')
        generador ='0011'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[petalo_longitud,petalo_ancho]
        n_columnas = 2 # dimension
    elif (sepalo_longitud ==0 and sepalo_ancho >0 and petalo_longitud > 0 and petalo_ancho == 0 ):
        print('Analsisis 2k 0110')
        generador ='0110'
        puntos_coordenadas= gen_iris(generador)
        punto_buscado_coordenada =[sepalo_ancho,petalo_longitud]
        n_columnas = 2 # dimension
    elif (sepalo_longitud >0 and sepalo_ancho >0 and petalo_longitud > 0 and petalo_ancho == 0 ):
        print('Analsisis 3k 1110')   
        generador ='1110'
        puntos_coordenadas= gen_iris(generador)
        punto_buscado_coordenada =[sepalo_longitud,sepalo_ancho,petalo_longitud]
        n_columnas = 3 # dimension
    elif (sepalo_longitud >0 and sepalo_ancho >0 and petalo_longitud == 0 and petalo_ancho > 0 ):
        print('Analsisis 3k 1101') 
        generador ='1101'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[sepalo_longitud,sepalo_ancho,petalo_ancho]
        n_columnas = 3 # dimension
    elif (sepalo_longitud >0 and sepalo_ancho ==0 and petalo_longitud > 0 and petalo_ancho > 0 ):
        print('Analsisis 3k 1011') 
        generador ='1011'
        puntos_coordenadas = gen_iris(generador)
        punto_buscado_coordenada =[sepalo_longitud,petalo_longitud,petalo_ancho]
        n_columnas = 3 # dimension
    elif (sepalo_longitud ==0 and sepalo_ancho >0 and petalo_longitud > 0 and petalo_ancho > 0 ):
        print('Analsisis 3k 0111') 
        generador ='0111'
        puntos_coordenadas= gen_iris(generador)
        punto_buscado_coordenada =[sepalo_ancho,petalo_longitud,petalo_ancho]
        n_columnas = 3 # dimension
    elif (sepalo_longitud >0 and sepalo_ancho >0 and petalo_longitud > 0 and petalo_ancho > 0 ):
        print('Analsisis 4k 0111') 
        generador ='1111'
        puntos_coordenadas= gen_iris(generador)
        punto_buscado_coordenada =[sepalo_longitud,sepalo_ancho,petalo_longitud,petalo_ancho]
        n_columnas = 4 # dimension
    else:
        print('Revisar otro error')
    
    for conta in range(cantidad_pruebas):
        #contruccion del arbol
        arbol = KDTree()
        arbol.construir_kdtree(puntos_coordenadas, discriminante)
        # KD Tree Search
        start = time()      
        if modo_prueba == 0:
            nd = arbol.busqueda_vecino_mas_cercano(punto_buscado_coordenada)
            print(f"======= Prueba {conta+1}: =======")
            # print(f"Puntos : {puntos_coordenadas}")
            print(f"Punto de Busqueda : {punto_buscado_coordenada}")
            print(f"Punto mas cercano: {nd.split[0]}")
            tiempo_calculo+= time() - start
            distancia_optima = calculo_distancia_euclidiana(punto_buscado_coordenada, nd.split[0])
            print(f"Distancia: {distancia_optima}")
            print(f"Tiempo de calculo: {tiempo_calculo}")
            print("\n")
            graficardor_puntos_iris(opcion_graficar_puntos,conta,puntos_coordenadas,punto_buscado_coordenada,nd.split[0],n_columnas,distancia_optima,generador)
        if modo_prueba == 1:
            datos_prueba = gen_iris_prueba(generador)
            conta=0           
            for fila in datos_prueba:
                conta +=1
                pto_prueba = fila[0:n_columnas]
                nd = arbol.busqueda_vecino_mas_cercano(pto_prueba)
                print(f"======= Prueba {conta}: =======")
                # print(f"Puntos : {puntos_coordenadas}")
                print(f"Punto de Busqueda : {fila}")
                print(f"Punto mas cercano: {nd.split[0]}")
                tiempo_calculo+= time() - start
                distancia_optima = calculo_distancia_euclidiana(pto_prueba, nd.split[0])
                print(f"Distancia: {distancia_optima}")
                print(f"Tiempo de calculo: {tiempo_calculo}")
                print("\n")       
                #graficardor_puntos_iris(opcion_graficar_puntos,conta,puntos_coordenadas,punto_buscado_coordenada,nd.split[0],n_columnas,distancia_optima,generador)


## resultados
    print(f"{cantidad_pruebas} Pruebas realizadas")
    wait = input("Presione ENTER tecla para terminar....")