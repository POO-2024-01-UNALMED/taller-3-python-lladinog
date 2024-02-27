class Marca:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre


class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        TV.numTV += 1

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_canal(self):
        return self.__canal

    def set_canal(self, canal):
        if self.__estado and 1 <= canal <= 120:
            self.__canal = canal

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_volumen(self):
        return self.__volumen

    def set_volumen(self, volumen):
        if self.__estado and 0 <= volumen <= 7:
            self.__volumen = volumen

    def turn_on(self):
        self.__estado = True

    def turn_off(self):
        self.__estado = False

    def canal_up(self):
        if self.__estado and self.__canal < 120:
            self.__canal += 1

    def canal_down(self):
        if self.__estado and self.__canal > 1:
            self.__canal -= 1

    def volumen_up(self):
        if self.__estado and self.__volumen < 7:
            self.__volumen += 1

    def volumen_down(self):
        if self.__estado and self.__volumen > 0:
            self.__volumen -= 1


class Control:
    def __init__(self):
        self.__tv = None

    def turn_on(self):
        if self.__tv:
            self.__tv.turn_on()

    def turn_off(self):
        if self.__tv:
            self.__tv.turn_off()

    def canal_up(self):
        if self.__tv:
            self.__tv.canal_up()

    def canal_down(self):
        if self.__tv:
            self.__tv.canal_down()

    def volumen_up(self):
        if self.__tv:
            self.__tv.volumen_up()

    def volumen_down(self):
        if self.__tv:
            self.__tv.volumen_down()

    def set_canal(self, canal):
        if self.__tv:
            self.__tv.set_canal(canal)

    def set_volumen(self, volumen):
        if self.__tv:
            self.__tv.set_volumen(volumen)

    def enlazar(self, tv):
        self.__tv = tv
        tv.set_control(self)

    def get_tv(self):
        return self.__tv

    def set_tv(self, tv):
        self.__tv = tv
