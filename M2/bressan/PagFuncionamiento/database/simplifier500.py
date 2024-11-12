from cruddb import Crud

#***SOLO EJECUTAR UNA VEZ, SI YA HAY BASE DE DATOS NO USAR**
def cargadatos():
    #datos ram
    ram_datos = [
        ("RAM", "DDR3 8GB", "all", 10, "Memoria RAM DDR3 8GB", 80000, "link"),     
        ("RAM", "DDR3 16GB", "all", 5, "Memoria RAM DDR3 16GB", 150000, "link"),
        ("RAM", "DDR3 32GB", "all", 3, "Memoria RAM DDR3 32GB", 300000, "link"),
        ("RAM", "DDR4 8GB", "all", 10, "Memoria RAM DDR4 8GB", 80000, "link"),
        ("RAM", "DDR4 16GB", "all", 5, "Memoria RAM DDR4 16GB", 150000, "link"),
        ("RAM", "DDR4 32GB", "all", 3, "Memoria RAM DDR4 32GB", 300000, "link"),
    ]

    # Datos micros
    cpu_datos = [
        ("CPU", "AMD Ryzen 5", "AM4", 10, "Microprocesador AMD Ryzen 5", 250000, "link"),
        ("CPU", "AMD Ryzen 7", "AM4", 5, "Microprocesador AMD Ryzen 7", 350000, "link"),
        ("CPU", "AMD Ryzen 9", "AM4", 3, "Microprocesador AMD Ryzen 9", 500000, "link"),
        ("CPU", "Intel i5", "LGA 1151", 10, "Microprocesador Intel i5", 250000, "link"),
        ("CPU", "Intel i7", "LGA 1151", 5, "Microprocesador Intel i7", 350000, "link"),
        ("CPU", "Intel i9", "LGA 1151", 3, "Microprocesador Intel i9", 500000, "link"),
    ]

    # Datos discos
    ssd_hdd_datos = [
        ("Almacenamiento", "SSD 500GB", "all", 10, "SSD 500GB", 120000, "link"),
        ("Almacenamiento", "SSD 1TB", "all", 5, "SSD 1TB", 200000, "link"),
        ("Almacenamiento", "HDD 1TB", "all", 10, "HDD 1TB", 50000, "link"),
        ("Almacenamiento", "HDD 2TB", "all", 5, "HDD 2TB", 80000, "link"),
        ("Almacenamiento", "SSD 2TB", "all", 3, "SSD 2TB", 300000, "link"),
        ("Almacenamiento", "SSD 4TB", "all", 2, "SSD 4TB", 600000, "link"),
    ]

    # Datos placas
    gpu_datos = [
        ("GPU", "NVIDIA GTX 1660", "all", 5, "Placa de Video NVIDIA GTX 1660", 200000, "link"),
        ("GPU", "NVIDIA RTX 2060", "all", 3, "Placa de Video NVIDIA RTX 2060", 350000, "link"),
        ("GPU", "NVIDIA RTX 3060", "all", 2, "Placa de Video NVIDIA RTX 3060", 600000, "link"),
        ("GPU", "AMD RX 580", "all", 5, "Placa de Video AMD RX 580", 200000, "link"),
        ("GPU", "AMD RX 590", "all", 3, "Placa de Video AMD RX 590", 350000, "link"),
        ("GPU", "AMD RX 6800", "all", 2, "Placa de Video AMD RX 6800", 600000, "link"),
    ]

    # Datos fuentes
    fuente_datos = [
        ("Fuente", "580W", "all", 10, "Fuente de Poder 580W", 80000, "link"),
        ("Fuente", "650w", "all", 5, "Fuente de Poder 650W", 100000, "link"),
        ("Fuente", "750W", "all", 3, "Fuente de Poder 750W", 120000, "link"),
        ("Fuente", "850W", "all", 2, "Fuente de Poder 850W", 150000, "link"),
    ]

    # Datos gabinetes
    gabinete_datos = [
        ("Gabinete", "Gabinete ATX", "all", 5, "Gabinete ATX para PC", 60000, "link"),
        ("Gabinete", "Gabinete Micro ATX", "all", 5, "Gabinete Micro ATX", 50000, "link"),
        ("Gabinete", "Gabinete Mini ITX", "all", 3, "Gabinete Mini ITX", 70000, "link"),
        ("Gabinete", "Gabinete con Ventanas", "all", 4, "Gabinete con Ventanas", 80000, "link"),
    ]

    # Datos mother
    motherboard_datos = [
        ("Motherboard", "Motherboard AM4 DDR3", "AM4", 5, "Motherboard compatible con AMD y DDR3", 150000, "link"),
        ("Motherboard", "Motherboard AM4 DDR3", "AM4", 5, "Motherboard compatible con AMD y DDR3", 150000, "link"),
        ("Motherboard", "Motherboard AM4 DDR3", "AM4", 5, "Motherboard compatible con AMD y DDR3", 150000, "link"),
        ("Motherboard", "Motherboard Intel DDR4", "LGA 1151", 5, "Motherboard compatible con Intel y DDR4", 200000, "link"),
        ("Motherboard", "Motherboard Intel DDR4", "LGA 1151", 5, "Motherboard compatible con Intel y DDR4", 200000, "link"),
        ("Motherboard", "Motherboard Intel DDR4", "LGA 1151", 5, "Motherboard compatible con Intel y DDR4", 200000, "link"),
    ]

    #crea la tabla
    Crud.crear_tabla()
        
    # Agregar datos a la base de datos
    for tipo, nombre, socket, stock, descripcion, precio, enlace in ram_datos:
        Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)

    for tipo, nombre, socket, stock, descripcion, precio, enlace in cpu_datos:
        Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)

    for tipo, nombre, socket, stock, descripcion, precio, enlace in ssd_hdd_datos:
        Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)

    for tipo, nombre, socket, stock, descripcion, precio, enlace in gpu_datos:
        Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)

    for tipo, nombre, socket, stock, descripcion, precio, enlace in fuente_datos:
        Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)

    for tipo, nombre, socket, stock, descripcion, precio, enlace in gabinete_datos:
        Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)

    for tipo, nombre, socket, stock, descripcion, precio, enlace in motherboard_datos:
        Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)


cargadatos()
Crud.cerrar_db
print("=======================================")
print ("FIN, simplifier500 termino su tarea")
print("=======================================")