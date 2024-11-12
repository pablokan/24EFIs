from soldados import *
# Clases de facciones

class Ejercito:
    def __init__(self, saludMaxima):
        self.salud = saludMaxima
        self.saludMaxima = saludMaxima

class Griego(Ejercito):
    def __init__(self, saludMaxima=40):
        super().__init__(saludMaxima)

        soldado1 = Soldado('Hoplita', 8)
        soldado2 = Soldado('Peltasta', 6)
        soldado3 = Soldado('Arquero', 7)
        soldado4 = Soldado('Jinete', 7)
        medico1 = Medico('Therapeutai', 8)
        apoyo1 = Apoyo('Pitagorico', 5, 2)
        self.listaSoldados = [soldado1, soldado2, soldado3, soldado4, medico1, apoyo1]

class Romano(Ejercito):
    def __init__(self, saludMaxima=40):
        super().__init__(saludMaxima)

        soldado1 = Soldado('Legionario', 8)
        soldado2 = Soldado('Pretoriano', 7)
        soldado3 = Soldado('Hastatus', 6)
        medico1 = Medico('Medici', 8)
        apoyo1 = Apoyo('Salvatore', 3, 3)
        apoyo2 = Apoyo('Aesculapius', 4, 2)
        self.listaSoldados = [soldado1, soldado2, soldado3, medico1, apoyo1, apoyo2]

class Vikingo(Ejercito):
    def __init__(self, saludMaxima=40):
        super().__init__(saludMaxima)

        soldado1 = Soldado('Berserker', 10)
        soldado2 = Soldado('Skjaldmeyjar', 7)
        soldado3 = Soldado('Huscarls', 9)
        apoyo1 = Apoyo('Valkiria', 5, 4)
        apoyo2 = Apoyo('Seior', 4, 3)
        self.listaSoldados = [soldado1, soldado2, soldado3, apoyo1, apoyo2]

class Persa(Ejercito):
    def __init__(self, saludMaxima=30):
        super().__init__(saludMaxima)

        soldado1 = Soldado('Inmortal', 7)
        soldado2 = Soldado('Lancero', 8)
        soldado3 = Soldado('Sparabara', 6)
        apoyo1 = Apoyo('Arquero Auxiliar', 1, 4)
        apoyo2 = Apoyo('Asuya', 5, 1)
        apoyo3 = Apoyo('Mogi-asuy', 3, 3)
        self.listaSoldados = [soldado1, soldado2, soldado3, apoyo1, apoyo2, apoyo3]