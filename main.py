class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura  # implementación de la función con la forula de área de un rectángulo


class Circulo:
    pi = 3.141592653589793

    def __init__(self, radio):
        self.radio = radio  # inicialización de la variable radio

    def area(self):
        return self.pi * (self.radio ** 2)  # implementación de la función con la forula de área de un círculo