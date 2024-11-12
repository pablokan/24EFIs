from nicegui import ui
import json
import os

# Archivo para almacenar los datos
DATA_FILE = 'datos_futbol.json'     # Si no existe lo crea

# Datos por defecto
DEFAULT_DATA = {
    'patrimonio': 5000000,
    'jugadores': [
        {'ID': "01", 'name': 'Rodrigo Salazar', 'age': "22/05/1998", 'sueldo': 36000, 'situacion': "Libre", 'posicion': 'defensor', 'precio': 100000},
        {'ID': "02", 'name': 'Castolo Juan', 'age': "18/10/1998", 'sueldo': 55000, 'situacion': "Libre", 'posicion': 'delantero', 'precio': 545000},
        {'ID': "03", 'name': 'Rodriguez Julian', 'age': "03/06/1996", 'sueldo': 42000, 'situacion': 'En equipo', 'posicion': 'medio', 'precio': 330000},
        {'ID': "04", 'name': 'Pechi Lionel', 'age': "12/02/1987", 'sueldo': 45000, 'situacion': 'En equipo', 'posicion': 'arquero', 'precio': 100000},
        {'ID': "05", 'name': 'Lopez Nicolas', 'age': "27/09/1994", 'sueldo': 23000, 'situacion': 'En equipo', 'posicion': 'delantero', 'precio': 810000},
        {'ID': "06", 'name': 'Liam Neeson', 'age': "14/05/2000", 'sueldo': 22000, 'situacion': 'En equipo', 'posicion': 'delantero', 'precio': 152000},
        {'ID': "07", 'name': 'Carlos Perez', 'age': "23/04/1993", 'sueldo': 54000, 'situacion': 'En equipo', 'posicion': 'delantero', 'precio': 100000},
        {'ID': "08", 'name': 'Tomas Garcia', 'age': "30/08/1992", 'sueldo': 38500, 'situacion': 'En equipo', 'posicion': 'medio', 'precio': 390000},
        {'ID': "09", 'name': 'Mario Gutierrez', 'age': "05/07/1990", 'sueldo': 33000, 'situacion': 'En equipo', 'posicion': 'defensor', 'precio': 100000},
        {'ID': "10", 'name': 'Martin Bravo', 'age': "28/03/1995", 'sueldo': 49000, 'situacion': 'En equipo', 'posicion': 'medio', 'precio': 168500},
        {'ID': "11", 'name': 'Pedro Alvarado', 'age': "01/11/1989", 'sueldo': 45000, 'situacion': 'Libre', 'posicion': 'arquero', 'precio': 47000},
        {'ID': "12", 'name': 'Juan Lopez', 'age': "19/12/1991", 'sueldo': 35000, 'situacion': 'Libre', 'posicion': 'delantero', 'precio': 99000},
        {'ID': "13", 'name': 'Esteban Martinez', 'age': "07/09/1998", 'sueldo': 37000, 'situacion': 'Libre', 'posicion': 'defensor', 'precio': 67000},
        {'ID': "14", 'name': 'Fernando Gonzalez', 'age': "17/01/2007", 'sueldo': 39000, 'situacion': 'Libre', 'posicion': 'enganche', 'precio': 160000},
        {'ID': "15", 'name': 'Miguel Herrera', 'age': "29/11/1990", 'sueldo': 41000, 'situacion': 'Libre', 'posicion': 'defensor', 'precio': 40000},
        {'ID': "16", 'name': 'Daniel Ortega', 'age': "11/04/1999", 'sueldo': 53000, 'situacion': 'Libre', 'posicion': 'enganche', 'precio': 425000},
    ]
}

# Variables globales
table_general = None
table_vender = None
table_comprar = None
label_patrimonio = None
Jugadores = []
patrimonio = 0

def cargar_datos():
    """Carga los datos desde el archivo JSON o usa los valores por defecto"""
    global Jugadores, patrimonio
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                data = json.load(file)
                Jugadores = data['jugadores']
                patrimonio = data['patrimonio']
        else:
            Jugadores = DEFAULT_DATA['jugadores']
            patrimonio = DEFAULT_DATA['patrimonio']
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        Jugadores = DEFAULT_DATA['jugadores']
        patrimonio = DEFAULT_DATA['patrimonio']

def guardar_datos():
    """Guarda los datos actuales en el archivo JSON"""
    try:
        data = {
            'jugadores': Jugadores,
            'patrimonio': patrimonio
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        ui.notify('Error al guardar los datos')

def actualizar_patrimonio():
    label_patrimonio.set_text(f'Patrimonio: ${patrimonio:,}')
    guardar_datos()

def actualizar_listas():
    global Vender, Comprar, Jugadores
    # Filtrar jugadores que no estén eliminados
    Jugadores = [j for j in Jugadores if j['situacion'] != 'Eliminado']
    Vender = [j for j in Jugadores if j['situacion'] == 'En equipo']
    Comprar = [j for j in Jugadores if j['situacion'] == 'Libre']
    
    # Actualizar todas las tablas
    if table_general:
        table_general.rows = Jugadores
    if table_vender:
        table_vender.rows = Vender
    if table_comprar:
        table_comprar.rows = Comprar
    
    guardar_datos()

def vender_jugador(table):
    global patrimonio
    selected = table.selected
    if not selected:
        ui.notify('Ningún jugador seleccionado para vender.')
        return
    
    jugador = selected[0]
    # Encontrar el jugador en la lista principal y marcarlo como "Eliminado"
    for j in Jugadores:
        if j['ID'] == jugador['ID']:
            j['situacion'] = 'Eliminado'
            patrimonio += j['precio']
            break
    
    actualizar_listas()
    actualizar_patrimonio()
    ui.notify(f'Jugador vendido: {jugador["name"]}')

def comprar_jugador(table):
    global patrimonio
    selected = table.selected
    if not selected:
        ui.notify('Ningún jugador seleccionado para comprar.')
        return
    
    jugador = selected[0]
    if patrimonio < jugador['precio']:
        ui.notify(f'No hay suficiente patrimonio para comprar a {jugador["name"]}.')
        return

    for j in Jugadores:
        if j['ID'] == jugador['ID']:
            j['situacion'] = 'En equipo'
            patrimonio -= j['precio']
            break
    
    actualizar_listas()
    actualizar_patrimonio()
    ui.notify(f'Jugador comprado: {jugador["name"]}')

# Cargar datos al inicio
cargar_datos()
# Inicializar las listas
actualizar_listas()

with ui.row().classes('justify-end'):
    label_patrimonio = ui.label(f'Patrimonio: ${patrimonio:,}').classes('text-2xl mb-4 mr-4')

with ui.tabs() as tabs:
    ui.tab('General', icon='sports_soccer')
    ui.tab('Vender', icon='sell')
    ui.tab('Comprar', icon='shopping_cart')

with ui.tab_panels(tabs, value='General'):
    with ui.tab_panel('General'):
        with ui.card().classes('w-full'):
            ui.label('Lista de Jugadores').classes('text-2xl mb-4')
            table_general = ui.table(
                columns=[
                    {'name': 'ID', 'label': 'ID', 'field': 'ID', 'align': 'left', 'sortable': True},
                    {'name': 'name', 'label': 'Nombre', 'field': 'name', 'align': 'left', 'sortable': True},
                    {'name': 'age', 'label': 'Fecha Nac', 'field': 'age', 'align': 'left', 'sortable': True},
                    {'name': 'sueldo', 'label': 'Sueldo', 'field': 'sueldo', 'align': 'right', 'sortable': True},
                    {'name': 'situacion', 'label': 'Situación', 'field': 'situacion', 'align': 'left', 'sortable': True},
                    {'name': 'posicion', 'label': 'Posicion', 'field': 'posicion', 'align': 'left', 'sortable': True},
                    {'name': 'precio', 'label': 'Precio', 'field': 'precio', 'align': 'left', 'sortable': True},
                ],
                rows=Jugadores,
                row_key='ID',
                pagination=5,
                selection=None
            )
            ui.input('Buscar jugador...').bind_value(table_general, 'filter')

    with ui.tab_panel('Vender'):
        with ui.card().classes('w-full'):
            ui.label('Vender jugadores').classes('text-2xl mb-4')
            table_vender = ui.table(
                columns=[
                    {'name': 'ID', 'label': 'ID', 'field': 'ID', 'align': 'left', 'sortable': True},
                    {'name': 'name', 'label': 'Nombre', 'field': 'name', 'align': 'left', 'sortable': True},
                    {'name': 'age', 'label': 'Edad', 'field': 'age', 'align': 'left', 'sortable': True},
                    {'name': 'sueldo', 'label': 'Sueldo', 'field': 'sueldo', 'align': 'right', 'sortable': True},
                    {'name': 'situacion', 'label': 'Situación', 'field': 'situacion', 'align': 'left', 'sortable': True},
                    {'name': 'posicion', 'label': 'Posicion', 'field': 'posicion', 'align': 'left', 'sortable': True},
                    {'name': 'precio', 'label': 'Precio', 'field': 'precio', 'align': 'left', 'sortable': True},
                ],
                rows=Vender,
                row_key='ID',
                pagination=5,
                selection='single'
            )
            ui.input('Buscar jugador...').bind_value(table_vender, 'filter')
            ui.button('Vender jugador').on('click', lambda: vender_jugador(table_vender))

    with ui.tab_panel('Comprar'):
        with ui.card().classes('w-full'):
            ui.label('Comprar jugadores').classes('text-2xl mb-4')
            table_comprar = ui.table(
                columns=[
                    {'name': 'ID', 'label': 'ID', 'field': 'ID', 'align': 'left', 'sortable': True},
                    {'name': 'name', 'label': 'Nombre', 'field': 'name', 'align': 'left', 'sortable': True},
                    {'name': 'age', 'label': 'Edad', 'field': 'age', 'align': 'left', 'sortable': True},
                    {'name': 'sueldo', 'label': 'Sueldo', 'field': 'sueldo', 'align': 'right', 'sortable': True},
                    {'name': 'situacion', 'label': 'Situación', 'field': 'situacion', 'align': 'left', 'sortable': True},
                    {'name': 'posicion', 'label': 'Posicion', 'field': 'posicion', 'align': 'left', 'sortable': True},
                    {'name': 'precio', 'label': 'Precio', 'field': 'precio', 'align': 'left', 'sortable': True},
                ],
                rows=Comprar,
                row_key='ID',
                pagination=5,
                selection='single'
            )
            ui.input('Buscar jugador...').bind_value(table_comprar, 'filter')
            ui.button('Comprar jugador').on('click', lambda: comprar_jugador(table_comprar))

ui.run()