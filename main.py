from manejadorViajeros import ManejadorViajeros
from claseViajeroFrec import ViajeroFrecuente
from menu import Menu
import os

def test():
    #TEST CON DIFERENTES CREACIONES DE OBJETOS DE LA CLASE VIAJERO FRECUENTE
    print('  -----------TEST DE VIAJEROS-----------')
    print('\n\n VIAJERO 1: CON DATOS CORRECTOS')
    v1=ViajeroFrecuente(99, 11698876, 'VIAJERO', '1', 1243.2)   #SOLO PERMITE MOSTRAR LOS DATOS DE                                                     
    v1.mostrar()                                                #LOS OBJETOS CORRECTAMENTE CREADOS
    print('\n\n VIAJERO 2: CON TIPO DE DATOS INCORRECTOS')
    v2=ViajeroFrecuente('100',11.23, 'VIAJERO', '2', 123)
    v2.mostrar()
    print('\n\n VIAJERO 3: SIN UN DATO')
    v3=ViajeroFrecuente()
    v3.mostrar()
    print('\n\n VIAJERO 4: CON DATOS FALTANTES')
    v4=ViajeroFrecuente(100,14631791,'VIAJERO 4')
    v4.mostrar()
    print('------------------------------------------\n')

if __name__=='__main__':
    t=str(input('DESEA PROBAR EL TEST (S/N) : '))
    if t.lower()=='s':
        test()
        input()
    os.system('cls')
    print('~~~~~~~~PROGRAMA PRINCIPAL~~~~~~\n')
    manej=ManejadorViajeros()
    manej.testViajeros()
    menu= Menu()
    salir= False
    band=True
    while band:
            nume = int(input('Ingrese el numero de viajero: '))
            indice=manej.buscarViajero(nume)        #SE BUSCA EL INDICE DEL VIAJERO EN LA LISTA DEL MANEJADOR
            if indice != -1:                      
                    while not salir:
                        print("\n-------------------Menu-------------------")
                        print(' 1- Consultar cantidad de millas')
                        print(' 2- Acumular millas')
                        print(' 3- Canjear millas')
                        print(' 4- Salir')
                        op= input('\n INGRESE UNA OPCION: ')
                        if op in ('1','2','3','4'):
                             menu.opcion(int(op),manej,indice)
                             if op==4:
                                 salir=True
                        else:
                            os.system('cls')
                            print ("---OPCION NO VALIDA---")
                    band = False
            else:
                print('Error: el numero ingresado no pertenece a ningun viajero.') 