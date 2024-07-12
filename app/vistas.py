from modelos import Grupo_entrada,TipoEntrada
from simple_screen import locate, Print,Screen_manager,Input
"""
               1         2         3        
      1234567890123456789012345678901234567
01    TIPO             PU     Q       TOTAL
02    =====================================
03    BEBE (≤2)      0.00    99     9999.99
04    NINO (≤12)    14.00    99     9999.99
05    ADULTO (<65)  23.00    99     9999.99
06    JUBILADO      18.00    99     9999.99
07    -------------------------------------
08                          999    99999.99
09                          
10    EDAD: 
11    CONF
"""

class Vista_Grupo:
    def __init__(self,grupo: Grupo_entrada, x = 1, y = 1):
        self.grupo = grupo
        self.x = x
        self.y = y

    def paint(self):
        locate(self.x, self.y, "TIPO                      PU      Q        TOTAL")
        locate(self.x, self.y + 1, "===============================================")
        for indice, tipo in enumerate(TipoEntrada):
            locate(self.x,self.y + 3 + indice,f"{tipo.name:.<11s} (max: {tipo.value.edad_max:>2d})   {tipo.value.precio:5.2f}    {self.grupo.cantidad_entradas_por_tipo(tipo):2d}     {self.grupo.subtotal_tipo(tipo):7.2f}")
        locate(self.x, self.y + 7,"-----------------------------------------------")
        locate(self.x,self.y + 8,f"                                {self.grupo.num_entradas:3d}    {self.grupo.total:8.2f}")

class Vista_Entrada:
    def __init__(self, etiqueta: str,x,y):
        self.etiqueta = etiqueta
        self.x = x
        self.y = y 

    def paint(self):
        locate(self.x, self.y, self.etiqueta)
        value = Input()
     

if __name__ == "__main__":
    with Screen_manager:
        grupo = Grupo_entrada()
        grupo.add_entrada(2)
        grupo.add_entrada(6)
        grupo.add_entrada(15)

        vg = Vista_Grupo(grupo)
        vista_edad = Vista_Entrada("EDAD: ",1 , 10 )

        vg.paint()
        vista_edad.paint()
        
    
        Input("pulsa enter para acabar")
