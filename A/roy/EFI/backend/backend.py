import reflex as rx

class PasswordState(rx.State): #Cambiamos el estado del password en el input
    verPassword: bool = False

    def verContraseña(self):
        self.verPassword = not self.verPassword #devuelve el valor opuesto
        
        
class ColorsState(rx.State):  #Cambiamos el color del header en la pagina principal
    colors:list[str] = [
       "red", "green","blue","pink","orange", "purple","brown","coral",
       "gold","magenta","tan","turquoise","yellow","navy",
    ]
    colorElegido : str  #almacena el color que se va a usar en la lista colors para despues aplicarlo en el header en el background
    

