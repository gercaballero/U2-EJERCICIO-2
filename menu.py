import os
from manejadorViajeros import ManejadorViajeros
from claseViajeroFrec import ViajeroFrecuente

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, maneja,indice):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(maneja,indice)

    def salir(self, maneja,indice):
        print('Salida del programa')

    def opcion1(self, manej,indice):
             manej.consultarMillas(indice)
    def opcion2(self, manej,indice):
        millas= float(input("INGRESE CANTIDAD DE MILLAS RECORRIDAS EN EL ULTIMO VIAJE: "))
        manej.acumulador(indice,millas)
    def opcion3(self,manej,indice):
        millas= float(input("INGRESE CANTIDAD DE MILLAS A CANJEAR: "))
        manej.canjeador(indice,millas)
        