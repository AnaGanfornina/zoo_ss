from enum import Enum, auto
class TipoEntrada(Enum):
    BEBE = 0
    NIÑO = 14
    ADULTO = 23
    JUBILADO = 18

class Entrada:
    def __init__(self,edad: int):
        
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        
        elif edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else: 
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18


class Grupo_entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipo_entrada ={
            TipoEntrada.BEBE:{"Q":0,"P":0},
            TipoEntrada.NIÑO:{"Q":0,"P":14},
            TipoEntrada.ADULTO:{"Q":0,"P":23},
            TipoEntrada.JUBILADO:{"Q":0,"P":18}
        
        }
        """ 
        self.precio_entrada ={
            TipoEntrada.BEBE:0,
            TipoEntrada.NIÑO:14,
            TipoEntrada.ADULTO:23,
            TipoEntrada.JUBILADO:18
        } 
        """
    
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


       
