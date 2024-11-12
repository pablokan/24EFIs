from cruddb import Crud
#PRIMERO, NO TOCAR, SEGUNDO NOMBRES, TERCERO ALL INDICAR SLOT, CUARTO STOCK, QUINTO DESCRIPCION, SEXTO PRECIO, ULTIMO NO TOCAR
#***SOLO EJECUTAR UNA VEZ, SI YA HAY BASE DE DATOS NO USAR**
def cargadatos():
    #datos ram
    ram_datos = [
        ("RAM", "DDR3 4GB", "DDR3", 10, "Memoria RAM Crucial DDR3 4GB 1600MHZ", 16000, "link"),     
        ("RAM", "DDR3 8GB", "DDR3", 5, "Memoria RAM Hyperx Fury DDR3 8GB 1600MHZ", 25000, "link"),
        ("RAM", "DDR3 16GB", "DDR3", 3, "Memoria RAM Kingston DDR3 16GB 1333MHZ", 50000, "link"),
        ("RAM", "DDR4 8GB", "DDR4", 10, "Memoria RAM Apacer NOX RGB DDR4 8GB 2666MHZ", 55000, "link"),
        ("RAM", "DDR4 16GB", "DDR4", 5, "Memoria RAM Adata XPG Spectrix DDR4 16GB 3200MHZ", 86000, "link"),
        ("RAM", "DDR4 32GB", "DDR4", 3, "Memoria RAM Kingston Fury Beast RGB DDR4 32GB 3200MHZ", 130000, "link"),
    ]

    # Datos micros
    cpu_datos = [
        ("CPU", "AMD Ryzen 5 3600x", "AMD", 10, "Microprocesador AMD Ryzen 5 3600x", 180000, "link"),
        ("CPU", "AMD Ryzen 7 5700x", "AMD", 5, "Microprocesador AMD Ryzen 7 5700x", 350000, "link"),
        ("CPU", "AMD A6 7480", "AMD", 3, "Microprocesador AMD A6 7480", 85000, "link"),
        ("CPU", "AMD A4 6300", "AMD", 3, "Microprocesador AMD A4 6300", 60000, "link"),
        ("CPU", "Intel i5-11400F", "INTEL", 10, "Microprocesador Intel i5-11400F", 270000, "link"),
        ("CPU", "Intel i7-12700K ", "INTEL", 5, "Microprocesador Intel i7-12700K ", 400000, "link"),
        ("CPU", "Intel i3-4460", "INTEL", 3, "Microprocesador Intel i3-4460", 50000, "link"),
        ("CPU", "Intel i3-3220", "INTEL", 3, "Microprocesador Intel i3-3220", 40000, "link"),
    ]

    # Datos discos
    almacenamiento_datos = [
        ("Almacenamiento", "SSD 500GB", "SSD", 10, "SSD M.2 Kingston 500gb", 55000, "link"),
        ("Almacenamiento", "SSD 1TB", "SSD", 5, "SSD M.2 Western Digital Black 1TB", 150000, "link"),
        ("Almacenamiento", "HDD 1TB", "HDD", 10, "HDD Seagate Barracuda 1TB", 80000, "link"),
        ("Almacenamiento", "HDD 2TB", "HDD", 5, "HDD Seagate Barracuda 2TB", 100000, "link"),
        ("Almacenamiento", "SSD 240GB", "SDD", 3, "SSD SATA Western Digital Green 240gb", 30000, "link"),
        ("Almacenamiento", "SSD 480GB", "SSD", 2, "SSD SATA Kingston 480gb", 40000, "link"),
        ("Almacenamiento", "HDD 4TB", "HDD", 5, "HDD Western Digital Blue 4TB", 140000, "link"),
    ]

    # Datos placas
    gpu_datos = [
        ("GPU", "NVIDIA GT 710", "NVIDIA", 5, "Placa de Video MSI NVIDIA GT 710", 80000, "link"),
        ("GPU", "NVIDIA GT 1030", "NVIDIA", 5, "Placa de Video GIGABYTE NVIDIA GT 1030", 100000, "link"),
        ("GPU", "NVIDIA GTX 1660 SUPER", "NVIDIA", 5, "Placa de Video MSI GAMING X NVIDIA GTX 1660 SUPER", 380000, "link"),
        ("GPU", "NVIDIA RTX 3060 Ti", "NVIDIA", 3, "Placa de Video ASUS TUF GAMING NVIDIA RTX 3060Ti", 500000, "link"),
        ("GPU", "NVIDIA RTX 4070", "NVIDIA", 2, "Placa de Video GIGABYTE EAGLE OC NVIDIA RTX 4070", 1500000, "link"),
        ("GPU", "AMD RX 550", "AMD", 5, "Placa de Video ASROCK PHANTOM GAMING AMD RX 550", 118000, "link"),
        ("GPU", "AMD RX 580", "AMD", 5, "Placa de Video SAPPHIRE PULSE AMD RX 580", 260000, "link"),
        ("GPU", "AMD RX 7800 XT", "AMD", 3, "Placa de Video ASUS DUAL AMD RX 7800 XT", 930000, "link"),
        ("GPU", "AMD RX 6800 XT", "AMD", 2, "Placa de Video ASROCK PHANTOM GAMING AMD RX 6800 XT", 680000, "link"),
    ]

    # Datos fuentes
    fuente_datos = [
        ("Fuente", "Thermaltake Smart Black 500w", "all", 10, "Fuente de poder Thermaltake Smart Black 500w 80 Plus White", 90000, "link"),
        ("Fuente", "Corsair Rm850x Shift White 850w", "all", 5, "Fuente de poder Corsair Rm850x Shift White 850w 80 Plus Gold", 350000, "link"),
        ("Fuente", "Thermaltake Smart BX1 RGB 750w", "all", 3, "Fuente de poder Thermaltake Smart BX1 RGB 750w 80 Plus Bronze", 150000, "link"),
        ("Fuente", "Corsair Rm1000e Black 1000W", "all", 2, "Fuente de poder Corsair Rm1000e Black 1000w 80 Plus Gold", 500000, "link"),
    ]

    # Datos gabinetes
    gabinete_datos = [
        ("Gabinete", "Gabinete Gamer Aerocool Quantum ", "all", 4, "Gabinete Gamer Aerocool Quantum", 80000, "link"),
        ("Gabinete", "Gabinete Gamer Thermaltake H200 TG RGB White", "all", 5, "Gabinete Gamer Thermaltake H200 TG RGB White", 120000, "link"),
        ("Gabinete", "Gabinete Gamer Solarmax CM-W950-SF RGB", "all", 3, "Gabinete Gamer Solarmax CM-W950-SF RGB", 160000, "link"),
        ("Gabinete", "Gabinete Performance 6801", "all", 3, "Gabinete Performance 6801", 40000, "link"),
        ("Gabinete", "Gabinete Sentey G38", "all", 2, "Gabinete Sentey G38", 50000, "link"),
    ]

    # Datos mother
    motherboard_datos = [
        ("Motherboard", "Motherboard Aorus B450 Aorus Elite V2", "AMD", 5, "Motherboard Aorus B450 Aorus Elite V2 - AMD DDR4", 260000, "link"),
        ("Motherboard", "Motherboard Asus Rog Strix B550-f Gaming Wifi Ii", "AMD", 5, "Motherboard Asus Rog Strix B550-f Gaming Wifi Ii - AMD DDR4", 330000, "link"),
        ("Motherboard", "Motherboard Gigabyte B660m Ds3h", "INTEL", 5, "Motherboard Gigabyte B660m Ds3h - INTEL DDR4", 400000, "link"),
        ("Motherboard", "Motherboard Msi Pro H610M-G", "INTEL", 5, "Motherboard Msi Pro H610M-G - INTEL DDR4", 140000, "link"),
        ("Motherboard", "Motherboard Gigabyte F2A68HM-H", "AMD", 5, "Motherboard Gigabyte F2A68HM-H - AMD DDR3", 100000, "link"),
        ("Motherboard", "Motherboard MSI A68HM-E33 V2", "AMD", 5, "Motherboard MSI A68HM-E33 V2 - AMD DDR3", 90000, "link"),
        ("Motherboard", "Motherboard Gigabyte Z170-HD3", "INTEL", 5, "Motherboard Gigabyte Z170-HD3 - INTEL DDR3", 80000, "link"),
    ]

    #si existe elimina la tabla, y crea una nueva
    Crud.crear_tabla()
        
    # Agregar datos a la base de datos
    for ram in ram_datos:
        Crud.agregar(ram[0], ram[1],  ram[2], ram[3], ram[4], ram[5], ram[6])

    for cpu in cpu_datos:
        Crud.agregar(cpu[0], cpu[1], cpu[2], cpu[3], cpu[4], cpu[5], cpu[6])

    for almacenamiento in almacenamiento_datos:
        Crud.agregar(almacenamiento[0], almacenamiento[1], almacenamiento[2],  almacenamiento[3], almacenamiento[4], almacenamiento[5], almacenamiento[6])

    for gpu in gpu_datos:
        Crud.agregar(gpu[0], gpu[1],  gpu[2], gpu[3], gpu[4], gpu[5], gpu[6])

    for fuente in fuente_datos:
        Crud.agregar(fuente[0], fuente[1], fuente[2],  fuente[3], fuente[4], fuente[5], fuente[6])

    for gabinete in gabinete_datos:
        Crud.agregar(gabinete[0],gabinete[1], gabinete[2], gabinete[3],  gabinete[4], gabinete[5], gabinete[6])

    for mother in motherboard_datos:
        Crud.agregar(mother[0], mother[1], mother[2], mother[3],  mother[4], mother[5], mother[6])


cargadatos()
Crud.cerrar_db
print("=======================================")
print ("FIN, simplifier500 termino su tarea")
print("=======================================")