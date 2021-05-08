from claseViajeroFrec import ViajeroFrecuente
import csv
import os

class ManejadorViajeros:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    
    def agregarViajero(self, viajero):
        self.__lista.append(viajero)        #SE AÑADEN LOS OBJETOS A LA LISTA
    
    def testViajeros(self):
        archivo=open('viajeros.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera=True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unViajero=ViajeroFrecuente(int(fila[0]),int(fila[1]),str(fila[2]),str(fila[3]),float(fila[4]))
                self.agregarViajero(unViajero)
        archivo.close()
    
    def buscarViajero(self, numero):
        bandera=False
        i=0
        while not bandera and i < len(self.__lista):
            if self.__lista[i].numViajero()==numero:
                bandera=True
            else:
                i=i+1
        if i>=len(self.__lista):
            retorno= -1             #SI NO SE ENCUENTRA EN LA LISTA SE RETORNA EL VALOR -1
        else:
            retorno=i               #SI SE ENCUENTRA EN LA LISTA SE RETORNA EL VALOR DEL INDICE
        return retorno
    def consultarMillas(self, indice):
        os.system('cls')
        print("CANTIDAD DE MILLAS DEL VIAJERO {} ES DE: {}".format(self.__lista[indice].nombre(), self.__lista[indice].cantidadTotaldeMillas()))
    def acumulador(self,indice,millas):
        os.system('cls')
        self.__lista[indice].acumularMillas(millas)

    def canjeador(self,indice,millas):
        os.system('cls')
        self.__lista[indice].canjearMillas(millas)

   
