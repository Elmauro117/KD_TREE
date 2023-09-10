#### PRINCIPAL ####
from time import time
import matplotlib.pyplot as plt
from clases import KDTree
from datos import gen_data
from datos import imp_data_excel
from datos import imp_data
from datos import imp_Iris
from datos import gen_iris
from funciones2 import calculo_distancia_euclidiana
from graficos  import graficardor_puntos_iris


clases_predichas = []

### Def que acepta "masivamente" nuevos puntos
def ejecutor(puntos_predecir):
    print("Resultados de pruebas")

    #configuracion de pruebas aleatorias, si queremos nuestro dataset ponemos genera_datos_aleatorios = False
    cantidad_pruebas = 1
    tiempo_calculo= 0
    opcion_graficar_puntos =True
    genera_datos_aleatorios = False
    
    ## Bule for para cada PUNTO:    
    for punto in puntos_predecir:
        ### caracteristicas de prueba   
        sepalo_longitud = float(punto[0])
        sepalo_ancho = float(punto[1])
        petalo_longitud = float(punto[2])
        petalo_ancho = float(punto[3])
        
        #sepalo_longitud = float(input ('Ingrese longitud de sepalo en cm. ='))
        #sepalo_ancho = float(input ('Ingrese longitud de sepalo en cm. ='))
        #petalo_longitud = float(input ('Ingrese longitud de sepalo en cm. ='))
        #petalo_ancho = float(input ('Ingrese longitud de sepalo en cm. ='))
        
        generador='0000'
        discriminante = gen_data(0, 100, 150)
        
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
            puntos_coordenadas = gen_iris(generador)
            punto_buscado_coordenada =[sepalo_ancho,petalo_longitud]
            n_columnas = 2 # dimension
        elif (sepalo_longitud >0 and sepalo_ancho >0 and petalo_longitud > 0 and petalo_ancho == 0 ):
            print('Analsisis 3k 1110')   
            generador ='1110'
            puntos_coordenadas = gen_iris(generador)
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
            puntos_coordenadas = gen_iris(generador)
            punto_buscado_coordenada =[sepalo_ancho,petalo_longitud,petalo_ancho]
            n_columnas = 3 # dimension
        elif (sepalo_longitud >0 and sepalo_ancho >0 and petalo_longitud > 0 and petalo_ancho > 0 ):
            print('Analsisis 4k 0111') 
            generador ='1111'
            puntos_coordenadas = gen_iris(generador)
            punto_buscado_coordenada =[sepalo_longitud,sepalo_ancho,petalo_longitud,petalo_ancho]
            n_columnas = 4 # dimension
        else:
            print('Revisar otro error')
            
            
            
    
        for conta in range(cantidad_pruebas):
            minimo = 0 # rango minimo de coordenadas
            maximo = 100 # rango maximo de coordenadas
            n_filas = 30 # numero de puntos
    
            #Contruccion del arbol
            arbol = KDTree()
            arbol.construir_kdtree(puntos_coordenadas, discriminante)
            # KD Tree Search
            #start = time()
            nd = arbol.busqueda_vecino_mas_cercano(punto_buscado_coordenada)
            #print(f"======= Prueba {conta+1}: =======")
            #print(f"Puntos : {puntos_coordenadas}")
            #print(f"Punto de Busqueda : {punto_buscado_coordenada}")
            print(f"Punto mas cercano: {nd.split[0]}")
            clase = nd.split[0][4]
            clases_predichas.append(clase)
            #tiempo_calculo+= time() - start
            distancia_optima = calculo_distancia_euclidiana(punto_buscado_coordenada, nd.split[0])
            print(f"Distancia: {distancia_optima}")
            #print(f"Tiempo de calculo: {tiempo_calculo}")
            print("\n")       
            
            #graficardor_puntos_iris(opcion_graficar_puntos,conta,puntos_coordenadas,punto_buscado_coordenada,nd.split[0],n_columnas,distancia_optima,generador)
    ## resultados
        #print(f"{cantidad_pruebas} Pruebas realizadas")
        #print(clases_predichas)
        #wait = input("Presione ENTER tecla para terminar....")
    

            
#print(clases_predichas)
## def main, acá metemos las métricas y llamamos a la funcion q ejecuta la busqueda, no sé que tan buena práctica sea hacerlo en una func MAIN()
def main():    
    from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
    import pandas as pd
    
    dataframe_prueba = pd.read_csv("Iris_Excel_pruebas_si.csv", sep =";") ## CARGA DE DATASET
    array_df1 = dataframe_prueba.to_numpy()
    array_x = array_df1[:,1:5]  ### Features a "predecir"
    array_y = array_df1[:,5:]   ### labels|clases REALES
        
    #clases_reales = ["Iris-setosa",   "Iris-setosa",    "Iris-setosa",    "Iris-setosa",    "Iris-setosa",
    #                 "Iris-versicolor","Iris-versicolor","Iris-versicolor","Iris-versicolor","Iris-versicolor",
     #                "Iris-virginica","Iris-virginica","Iris-virginica","Iris-virginica","Iris-virginica"]
    #puntos_predecir = [[1,2,3,1],[1,2,2,1],[1,2,1,1],[1,2,3,3]]
    start = time()
    ejecutor(array_x)  ## Ejecutamos l codigo para busqueda de K vecinos
    tiempo_calculo = time() - start
    
    print(f"Tiempo de calculo: {tiempo_calculo}")
    print("reales",  array_y)
    print("predichas", clases_predichas)
    print(" "*16)
    print(classification_report(array_y,clases_predichas))
    print(confusion_matrix(array_y,clases_predichas))
    print(" "*16)
    print("accuracy", accuracy_score(array_y,clases_predichas))
    
if __name__ == "__main__":
    main()
