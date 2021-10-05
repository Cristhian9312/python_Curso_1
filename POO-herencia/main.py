import clases

print("------- persona -------")

Persona = clases.persona()
Persona.setNombre("cristhian")
Persona.setApellidos("carrero")
Persona.setEdad("27 años ")
Persona.setAltura("180 cm")

print(f"la persona es {Persona.getNombre()} {Persona.getApellidos()} y tiene {Persona.getEdad()}")
print(Persona.hablar())

print("------- informatico -------")

informatico = clases.informatico()
informatico.setNombre("Santiago")
informatico.setApellidos("marino")
informatico.setEdad("23 años")
print(informatico.lenguajes)

print(f"el informativo proooooo y traqueto se llama {informatico.getNombre()} {informatico.getApellidos()} y sabe de todo")

print("------- redes -------")

redes = clases.tecnicoRedes()
print(redes.getLenguajes())
print(redes.getRedes(),"\n", redes.getAuditoria())
print(redes.hablar())