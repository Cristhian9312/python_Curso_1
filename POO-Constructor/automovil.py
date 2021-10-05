class Coche():
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "soy un atributo publico"
    __soy_privado = "soy un atributo privado"
#este es el constructor

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

#aca voy a colocar metodos set y get para extraer y mandar nueva info

    def getPrivado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca 
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def getvelocidad(self):
        return self.velocidad

    def setCaballaje(self, caballaje):
        self.caballaje = caballaje

    def getCaballaje(self):
        return self.caballaje

    def setPlazas(self, plazas):
        self.plazas = plazas

    def getPlazas(self):
        return self.plazas

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getInfo(self):
        info = "------ informacion del coche -----"
        info += "\n Color: " + self.color
        info += "\n Marca: " + self.marca
        info += "\n Modelo: " + self.modelo
        info += "\n Velocidad: " + str(self.velocidad)
        info += "\n caballaje: " + str(self.caballaje)
        info += "\n Plazas: " + str(self.plazas) + "\n"

        return info





