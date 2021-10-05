#programacion orientada a objetos 

#definir una clase - molde para crear ojetos 

class Coche():
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

#aca voy a colocar metodos set y get para extraer y mandar nueva info

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getvelocidad(self):
        return self.velocidad

# aca finlaiza la clase 
print("--------- coche 1 --------------")
Coche1 = Coche()
Coche1.setColor("Negro")
Coche1.setModelo("Renault")
print(Coche1.marca, Coche1.getColor(), Coche1.getModelo())
print("la velocidad del coche es de:" ,Coche1.velocidad)

Coche1.acelerar()
Coche1.acelerar()
Coche1.acelerar()
Coche1.acelerar()
Coche1.acelerar()
Coche1.frenar()

print(Coche1.velocidad)

# voy a crear mas objetos 
print("------ coche 2 --------")
coche2 = Coche()
coche2.setColor("Azul metalizado")
print(coche2.getColor())

