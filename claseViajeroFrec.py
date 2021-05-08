import os
class ViajeroFrecuente:
    __numero=-1
    __dni=-1
    __name=''
    __lastname=''
    __millasAcum=-1.0

    def __init__(self,num=-1,dni=-1,nombre='',apellido='',millas=-1.0):
        if isinstance(num, int) and isinstance(dni, int) and isinstance(nombre, str) and isinstance(apellido, str) and isinstance(millas, float):
            self.__numero=num
            self.__dni=dni
            self.__name=nombre
            self.__lastname=apellido
            self.__millasAcum=millas
    
    def mostrar(self):
       if self.__numero==-1 or self.__dni==-1 or self.__name==-1 or self.__lastname==-1 or self.__millasAcum==-1.0:
            print('[INSTANCIA NO CREADA]')
       else:
            print("NUMERO:{}, DNI:{}, NOMBRE:{}, APELLIDO:{}, MILLAS:{}".format(self.__numero,self.__dni,self.__name,self.__lastname,self.__millasAcum))
    
    def cantidadTotaldeMillas(self):
        if self.__millasAcum!=None and self.__millasAcum!=-1.0:
            retorna=float(self.__millasAcum)
        else:
            retorna='[INSTANCIA NO CREADA]'
        return retorna
    def acumularMillas(self, millas):
        if isinstance(millas, float):
            self.__millasAcum=millas+self.cantidadTotaldeMillas()
        else:
            print('INGRESE VALOR DECIMAL DE MILLAS')

    def canjearMillas(self, canje):
        if isinstance(canje,float):
            if canje<=self.cantidadTotaldeMillas():
                self.__millasAcum=self.cantidadTotaldeMillas()-canje
            else:
                print("\n ---MILLAS INSUFICIENTES----")
        else:
            print('INGRESE VALOR DECIMAL DE MILLAS')
        
    def numViajero(self):
        if self.__numero>-1:
            retorna= int(self.__numero)
        else:
            retorna='[INSTANCIA NO CREADA]'
        return retorna
        
    def nombre(self):
        if self.__name!='':
            retorna= str(self.__name)
        else:
            retorna='[INSTANCIA NO CREADA]'
        return retorna
    
    def __eq__(self, otro):
        band=None
        if isinstance(otro, ViajeroFrecuente):
            if self.__numero==otro.numViajero:
                band= True
            else:
                band= False
