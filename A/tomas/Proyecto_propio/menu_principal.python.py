from funciones_menu_principal import Base_datos
class Banco_organos():
    def __init__(self):
        self.db=Base_datos()
        
    def menu_principal(self): 
        seguir = True
        while seguir:
            print("")
            print("<---------| Menu Principal |--------->")
            print("""
            1- Menu Pacientes
            2- Menu Donantes 
            3- Salir
                """)
            
            pregunta = input("-------> Elija una opcion: ")
        
            if pregunta == "1":
                self.menu_paciente()
            elif pregunta == "2":
                self.menu_donantes()
            elif pregunta== "3":
                print("Saliendo...")
                seguir = False
            else:
                print("ERROR: Opcion no valida...")
                
    def menu_paciente(self):
        seguir = True
        while seguir:
            print("")
            print("<---------| Menu Pacientes |--------->")
            print("""
            1- Cargar Paciente
            2- Eliminar Paciente
            3- Ver Lista Pacientes
            4- Buscar Paciente
            5- Volver Atras
                """)
            
            pregunta = input("-------->Elija una Opcion: ")
            
            if pregunta == "1":
                self.db.cargar_en_tablas("pacientes")
            elif pregunta == "2":
                self.db.eliminar_de_tabla("pacientes")
            elif pregunta == "3":
                self.db.mostrar_tabla("pacientes")
            elif pregunta == "4":
                self.db.buscar_en_tabla("pacientes")
            elif pregunta == "5":
                self.db.cerrar_conexion()
                seguir = False
            else:
                print("Opcion no valida...")
    
    def menu_donantes(self):
        seguir = True
        while seguir:
            print("")
            print("<---------| Menu Donantes |--------->")
            print("""
            1- Cargar Donante
            2- Eliminar Donante
            3- Ver Lista Donantes
            4- Buscar Donante
            5- Volver Atras
                """)
            
            pregunta = input("-------->Elija una Opcion: ")
            
            if pregunta == "1":
                self.db.cargar_en_tablas("donantes")
            elif pregunta == "2":
                self.db.eliminar_de_tabla("donantes")
            elif pregunta == "3":
                self.db.mostrar_tabla("donantes")
            elif pregunta == "4":
                self.db.buscar_en_tabla("donantes")
            elif pregunta == "5":
                self.db.cerrar_conexion()
                seguir = False
            else:
                print("Opcion no valida...")
                