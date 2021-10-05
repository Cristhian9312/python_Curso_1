from automovil import Coche

carro = Coche("azul","ferrari","antiguo",500,20,10)
print(carro.getColor(), carro.getCaballaje(), carro.getMarca(), carro.getModelo(), carro.getPlazas(), carro.getvelocidad())
print(carro.getInfo())

cuatrimoto = Coche("verde","golf","nuevo",900,600,10)
print(cuatrimoto.getColor(), cuatrimoto.getMarca(), cuatrimoto.getModelo(), cuatrimoto.getPlazas(), cuatrimoto.getCaballaje(), cuatrimoto.getvelocidad())

#carro = "hola mundo"

if type(carro) == Coche:
    print("Es un objeto")
else:
    print("no es un objeto")

print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())