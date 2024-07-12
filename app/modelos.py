from enum import Enum, auto
class TipoEntrada(Enum):
    BEBE = (0,2)
    NIÑO = (14,12)
    ADULTO = (23,64)
    JUBILADO = (18,99)

class Entrada:
    def __init__(self,edad: int):
        self.__validate_edad(edad)
        
        self.__edad = edad

        for tipo in TipoEntrada:
            if edad <= tipo.value[1]:
                self.tipo = tipo
                self.precio = tipo.value
                break

    def __validate_edad(self, edad):
         if edad < 0:
            raise ValueError("La edad no debe ser negativa")
        
        
        


class Grupo_entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipo_entrada = {}
        for tipo in TipoEntrada:
            self.tipo_entrada[tipo] = {"Q":0, "P":tipo.value[0] }
    
       #Con deepcompension 
        #self.tipo_entrada = {tipo: {"Q":0, "P":tipo.value } for tipo in TipoEntrada}
    
    def add_entrada(self,edad):
        """
        En función de una edad crear una entrada e incrementar el contador de entrada
        Con el precio de la entrada nueva incrementar el total
        """
        #  En función de una edad crear una entrada
        entrada = Entrada(edad)

        #incrementar el contador de entrada

        self.num_entradas += 1
        self.total += entrada.precio


        self.tipo_entrada[entrada.tipo]["Q"] += 1

    def cantidad_entradas_por_tipo(self,tipo):
        return self.tipo_entrada[tipo]["Q"]
    
    def subtotal_tipo(self,tipo :TipoEntrada) -> int:

        return self.tipo_entrada[tipo]["Q"] * self.tipo_entrada[tipo]["P"]
        #return self.tipo_entrada[tipo] * self.precio_entrada[tipo]


       
