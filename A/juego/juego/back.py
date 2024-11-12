import reflex as rx

#back del juego



class Vida(rx.State):
    #creamos un estado para la vida del enemigo
    vid : int = 100
    msg: str = "SIGUES JUGANDO"
    
    def perderVida(self, ata: int):#funcion para perder vida
        self.vid = self.vid - ata
        if self.vid <= 0:
            self.vid = 0
            self.msg = "PERDISTE"
    def reiniciar(self):#funcion para reiniciar la vida
        self.vid = 100
        self.msg = "SIGUES JUGANDO"
  


class Vida2(rx.State):
    #creamos un estado para la vida del enemigo
    vid : int = 100
    msg: str = "SIGUES JUGANDO"
    
    def perderVida(self, ata: int):#funcion para perder vida
        self.vid = self.vid - ata
        if self.vid <= 0:
            self.vid = 0
            self.msg = "PERDISTE"
    def reiniciar(self):#funcion para reiniciar la vida
        self.vid = 100
        self.msg = "SIGUES JUGANDO"
  
