class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    @staticmethod
    def getNumTV():
        return TV.numTV
        
    def setNumTV(self):
        self.numTV = TV.numTV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado and self.canal < 120:
            self.canal += 1

    def canalDown(self):
        if self.estado and self.canal > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.estado and self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control