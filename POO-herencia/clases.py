class persona:
    """
    nombre = ""
    apellidos = "" 
    altura = "" 
    edad = ""
    """
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos 
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad 
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    
    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "estoy hablando"

    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo" 

class informatico(persona):
    """
    lenguajes = ""
    Experiencia = ""
    """
    def __init__(self):
        self.lenguajes = "HTML, JAvaScript, CSS, Mondo"
        self.Experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes

    def aprenderLenguajes(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "estoy programando"
    
    def reparar(self):
        return "he reparado tu ordenador"

class tecnicoRedes(informatico):

    def __init__(self):
        super().__init__()
        self.auditoria = "experto"
        self.redes = "sisco"
    
    def getAuditoria(self):
        return self.auditoria

    def getRedes(self):
        return self.redes