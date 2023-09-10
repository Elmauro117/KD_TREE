import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def graficardor_puntos(opcion_graficar_puntos,conta,puntos_coordenadas,punto_buscado_coordenada,punto_mas_cercano, dimension,distancia_optima):
    if opcion_graficar_puntos:
        if dimension ==2:
            coordenadas_x = list()
            coordenadas_y = list()
            for coordenada in puntos_coordenadas:
                array = coordenada
                coordenadas_x.append(array[0])
                coordenadas_y.append(array[1])
                #print(X[0])
            plt.scatter(coordenadas_x,coordenadas_y)
            plt.scatter(punto_buscado_coordenada[0],punto_buscado_coordenada[1], c="red",marker='x') #pto buscado
            plt.scatter(punto_mas_cercano[0],punto_mas_cercano[1], c="green") # pto mas cercano
            #plt.title("Prueba %d: " %(conta+1))
            #plt.legend(("P.Datos","P.Datos {Xi[0]},{Xi[1]}"), loc='lower left', fontsize='small') #"center left" ,
            plt.suptitle(f"Prueba {(conta+1)},Distancia optima : {distancia_optima}")
            plt.plot((punto_buscado_coordenada[0],punto_mas_cercano[0]),(punto_buscado_coordenada[1],punto_mas_cercano[1]), c='green',linestyle='dotted') # linea une pto buscado con mas cercano
            plt.legend(['Puntos',f'P.Buscado:({punto_buscado_coordenada[0]},{punto_buscado_coordenada[1]})',f'P.Cercano:({punto_mas_cercano[0]},{punto_mas_cercano[1]})'],ncols=3, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small') #"center left" ,'upper left','lower left'
            #plt.title(f'Distancia optima : {distancia_optima}')
            plt.show()
        elif dimension == 3:
            print('MUESTRA GRAFICO 3D')
            coordenadas_x = list()
            coordenadas_y = list()
            coordenadas_z = list()
            for coordenada in puntos_coordenadas:
                array = coordenada
                coordenadas_x.append(array[0])
                coordenadas_y.append(array[1])
                coordenadas_z.append(array[2])
                #print(X[0])
            #px.scatter_3d(coordenadas_x,coordenadas_y,coordenadas_Z)
            #px.scatter_3d(punto_buscado_coordenada[0],punto_buscado_coordenada[1], punto_buscado_coordenada[2],color="red",marker='x')
            #px.scatter_3d(punto_mas_cercano[0],punto_mas_cercano[1],punto_mas_cercano[2], color="green")

            #plt.suptitle(f"Prueba {(conta+1)}")
            #plt.plot((punto_buscado_coordenada[0],punto_mas_cercano[0]),(punto_buscado_coordenada[1],punto_mas_cercano[1]), c='green',linestyle='dotted') # linea une pto buscado con mas cercano
            #plt.legend(['Puntos',f'P.Buscado:({punto_buscado_coordenada[0]},{punto_buscado_coordenada[1]})',f'P.Cercano:({punto_mas_cercano[0]},{punto_mas_cercano[1]})'],ncols=3, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small') #"center left" ,'upper left','lower left'
            fig = plt.figure() 
            # syntax for 3-D projection
            ax = plt.axes(projection ='3d')
 
            # plotting
            ax.scatter(coordenadas_x, coordenadas_y, coordenadas_z, 'blue')
            ax.scatter(punto_buscado_coordenada[0],punto_buscado_coordenada[1],punto_buscado_coordenada[2], c="red",marker='x') #pto buscado
            ax.scatter(punto_mas_cercano[0],punto_mas_cercano[1],punto_mas_cercano[2], c="green", s=50) # pto mas cercano
            ax.plot3D((punto_buscado_coordenada[0],punto_mas_cercano[0]),(punto_buscado_coordenada[1],punto_mas_cercano[1]),(punto_buscado_coordenada[2],punto_mas_cercano[2]), c='green',linestyle='dotted')
            ax.set_title(f"Prueba {(conta+1)}, tiempo optimo {distancia_optima}")
            mng = plt.get_current_fig_manager()
            #mng.full_screen_toggle()
            
            plt.show()          
        else:
            print('NO MUESTRA GRAFICO')
            #no muestra graficos
def graficardor_puntos_iris(opcion_graficar_puntos,conta,puntos_coordenadas,punto_buscado_coordenada,punto_mas_cercano, dimension,distancia_optima,generador):
    if opcion_graficar_puntos:
        coordenadas_x1 = list()
        coordenadas_y1 = list()
        coordenadas_z1 = list()
        coordenadas_x2 = list()
        coordenadas_y2 = list()
        coordenadas_z2 = list()        
        coordenadas_x3 = list()
        coordenadas_y3 = list()
        coordenadas_z3 = list()
        clase1='Iris-virginica'
        clase2 ='Iris-versicolor'
        clase3 = 'Iris-setosa'
        if dimension ==2:
            for coordenada in puntos_coordenadas:
                array = coordenada
                if array[2]== clase1:# virginica
                    coordenadas_x1.append(array[0])
                    coordenadas_y1.append(array[1])
                if array[2]==clase2: # versicolos
                    coordenadas_x2.append(array[0])
                    coordenadas_y2.append(array[1])
                if array[2]== clase3:# setosa
                    coordenadas_x3.append(array[0])
                    coordenadas_y3.append(array[1])
            plt.scatter(coordenadas_x1,coordenadas_y1,c='pink', label=clase1)
            plt.scatter(coordenadas_x2,coordenadas_y2,c='cyan',label=clase2)
            plt.scatter(coordenadas_x3,coordenadas_y3,c='orange', label=clase3)
            plt.scatter(punto_buscado_coordenada[0],punto_buscado_coordenada[1], c="red",marker='x') #pto buscado
            #plt.scatter(punto_mas_cercano[0],punto_mas_cercano[1], c="green") # pto mas cercano
            #plt.title("Prueba %d: " %(conta+1))
            #plt.legend(("P.Datos","P.Datos {Xi[0]},{Xi[1]}"), loc='lower left', fontsize='small') #"center left" ,
            plt.suptitle(f"Prueba {(conta+1)},Distancia optima : {distancia_optima}")
            plt.plot((punto_buscado_coordenada[0],punto_mas_cercano[0]),(punto_buscado_coordenada[1],punto_mas_cercano[1]), c='green',linestyle='dotted') # linea une pto buscado con mas cercano
            plt.legend(['Iris-virginica', 'Iris-versicolor', 'Iris-setosa'])
            #plt.legend(['Puntos',f'P.Buscado:({punto_buscado_coordenada[0]},{punto_buscado_coordenada[1]})',f'P.Cercano:({punto_mas_cercano[0]},{punto_mas_cercano[1]})'],ncols=3, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small') #"center left" ,'upper left','lower left'
            #plt.title(f'Distancia optima : {distancia_optima}')
            if generador =='1010':
                plt.xlabel('Long. Sepalo cm.')
                plt.ylabel('Long. Petalo cm.')
            if generador =='1100':
                plt.xlabel('Long. Sepalo cm.')
                plt.ylabel('Ancho Sepalo cm.')
            if generador =='0011':
                plt.xlabel('Long. Petalo cm.')
                plt.ylabel('Ancho Petalo cm.')
            if generador =='0110':
                plt.xlabel('Ancho Sepalo cm.')
                plt.ylabel('Long. Petalo cm.')
            plt.show()
        elif dimension == 3:
            print('MUESTRA GRAFICO 3D')
            coordenadas_x = list()
            coordenadas_y = list()
            coordenadas_z = list()
            for coordenada in puntos_coordenadas:
                array = coordenada
                if array[3]== clase1:
                    coordenadas_x1.append(array[0])
                    coordenadas_y1.append(array[1])
                    coordenadas_z1.append(array[2])
                if array[3]== clase2:
                    coordenadas_x2.append(array[0])
                    coordenadas_y2.append(array[1])
                    coordenadas_z2.append(array[2])
                if array[3]== clase3:
                    coordenadas_x3.append(array[0])
                    coordenadas_y3.append(array[1])
                    coordenadas_z3.append(array[2])
                #print(X[0])
            fig = plt.figure() 
            # syntax for 3-D projection
            ax = plt.axes(projection ='3d')
 
            # plotting
            ax.scatter(coordenadas_x1,coordenadas_y1,coordenadas_z1,c='pink', label=clase1)
            ax.scatter(coordenadas_x2, coordenadas_y2, coordenadas_z2,c='cyan', label=clase2)
            ax.scatter(coordenadas_x3, coordenadas_y3, coordenadas_z3,c='orange', label=clase2)
            ax.scatter(punto_buscado_coordenada[0],punto_buscado_coordenada[1],punto_buscado_coordenada[2], c="red",marker='x') #pto buscado
            #ax.scatter(punto_mas_cercano[0],punto_mas_cercano[1],punto_mas_cercano[2], c="green", s=50) # pto mas cercano
            ax.plot3D((punto_buscado_coordenada[0],punto_mas_cercano[0]),(punto_buscado_coordenada[1],punto_mas_cercano[1]),(punto_buscado_coordenada[2],punto_mas_cercano[2]), c='green',linestyle='dotted')
            ax.set_title(f"Prueba {(conta+1)}, Distancia optima {distancia_optima} cm. 'P.Cercano:({punto_mas_cercano[0]},{punto_mas_cercano[1]},{punto_mas_cercano[2]})' ")
            ax.legend(['Iris-virginica', 'Iris-versicolor', 'Iris-setosa'])
            if generador =='1110':
                ax.set_xlabel('Long. Sepalo cm.')
                ax.set_ylabel('Ancho Sepalo cm.')
                ax.set_zlabel('Long. Petalo cm.')
            if generador =='1101':
                ax.set_xlabel('Long. Sepalo cm.')
                ax.set_ylabel('Ancho Sepalo cm.')
                ax.set_zlabel('Ancho Petalo cm.')
            if generador =='1011':
                ax.set_xlabel('Long. Sepalo cm.')
                ax.set_ylabel('Long. Petalo cm.')
                ax.set_zlabel('Ancho Petalo cm.')
            if generador =='0111':
                ax.set_xlabel('Ancho Sepalo cm.')
                ax.set_ylabel('Long. Petalo cm.')
                ax.set_zlabel('Ancho Petalo cm.')
            mng = plt.get_current_fig_manager()
            #mng.full_screen_toggle()
            
            plt.show()          
        else:
            print('NO MUESTRA GRAFICO')
            #no muestra graficos
