class Departamento:
    secuencia = 0
    departamentos = []

    def __init__(self,departamento):
        Departamento.secuencia += 1
        self.codigo = Departamento.secuencia
        self.descripcion = departamento
    
    def registro(self):
        return {"codigo":self.codigo,"departamento":self.descripcion}

