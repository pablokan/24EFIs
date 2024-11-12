from nicegui import ui
import sqlite_functions

def formatFila(reserva):
    pagado = '✅' if reserva[7] else '❌'
    fila = {
        'id': reserva[0], 
        'cancha': reserva[1], 
        'fecha': reserva[2], 
        'hora': reserva[3], 
        'precio': f'$ {reserva[4]}', 
        'nombre': reserva[5], 
        'telefono': reserva[6], 
        'pagado': pagado
    }
    return fila

def clearInputs(cancha, fecha, horario, nombre, telefono):
    cancha.set_value(None)
    fecha.set_value(None)
    horario.set_value(None)
    nombre.set_value(None)
    telefono.set_value(None)

def loadInputs(msg, cancha, fecha, horario, nombre, telefono, pagado):
    precio = float(msg.args.get('precio')[1:])
    cancha.set_value(precio)

    fecha.set_value(msg.args.get('fecha'))
    horario.set_value(msg.args.get('hora'))
    nombre.set_value(msg.args.get('nombre'))
    telefono.set_value(msg.args.get('telefono'))
    
    pago = True if msg.args.get('pagado') == '✅' else False
    pagado.set_value(pago)

def confirmarReserva(dialog, fecha, horario, nombre, precio, telefono, pago):
    match precio.value:
        case 13.5:
            cancha = 'Adentro 1'
        case 11.5: 
            cancha = 'Adentro 2'
        case 9.5: 
            cancha = 'Afuera 1'
        case 8.5:
            cancha = 'Afuera 2'

    # Insertamos los datos en la base de datos
    sqlite_functions.insertRow(cancha, str(fecha.value), horario.value, precio.value, nombre.value, telefono.value, pago.value)
    # Buscamos el id de la reserva ingresada
    idRes = sqlite_functions.searchLastID()
    # Guardamos los datos en una lista
    nuevaFila = [idRes, cancha, str(fecha.value), horario.value, precio.value, nombre.value, telefono.value, pago.value]
    # Le damos formato y los insertamos en la tabla
    reservas.append(formatFila(nuevaFila))
    table.update()
    dialog.close()

def editarReserva(msg, dialog, fecha, horario, nombre, precio, telefono, pago):
    match precio.value:
        case 13.5:
            cancha = 'Adentro 1'
        case 11.5:
            cancha = 'Adentro 2'
        case 9.5: 
            cancha = 'Afuera 1'
        case 8.5:
            cancha = 'Afuera 2'

    # Guardamos los datos modificados en una lista
    filaModificada = [msg.args.get('id'), cancha, str(fecha.value), horario.value, precio.value, nombre.value, telefono.value, pago.value]
    # Le damos formato y los insertamos en la tabla
    reservas.insert(reservas.index(msg.args), formatFila(filaModificada))
    # Eliminamos la fila original
    reservas.pop(reservas.index(msg.args))
    # Actualizamos la base de datos
    sqlite_functions.updateFields(cancha, str(fecha.value), horario.value, precio.value, nombre.value, telefono.value, pago.value, msg.args.get('id'))
    table.update()
    dialog.close()

def borrarReserva(dialog, msg):
    # Eliminamos la fila de la base de datos
    sqlite_functions.deleteRow(msg.args.get('id'))
    # Tambien lo eliminamos de la lista para actualizar lo que se ve en la pagina
    reservas.pop(reservas.index(msg.args))
    table.update()
    dialog.close()

def inputsReserva(accion, msg=''):
    with ui.dialog() as dialog, ui.card():
        precio = ui.radio([13.5, 11.5, 9.5, 8.5]).props('inline')
        precio.visible = False

        with ui.row(align_items = 'center'): 
            ui.label('Cancha')
            cancha = ui.radio({13.5: 'Adentro 1', 11.5: 'Adentro 2', 9.5: 'Afuera 1', 8.5: 'Afuera 2'}).props('inline color=light-green-14').bind_value(precio, 'value').classes('custom-radio')

        with ui.row(align_items = 'center'):    
            ui.label('Precio: $')
            ui.label().bind_text_from(precio, 'value')

        with ui.input('Fecha').bind_value(globals(), 'date') as date_input:
            date_input.props('color=light-green-14')
            with ui.menu() as menu:
                fecha = ui.date().bind_value(date_input).props('color=light-green-14')
            with date_input.add_slot('append'):
                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

        with ui.row(align_items = 'center'): 
            ui.label('Horario')
            horario = ui.radio(['08:00', '09:30', '11:00', '12:30', '14:00', '15:30', '17:00', '18:30', '20:00', '21:30']).props('inline color=light-green-14')

        with ui.row():
            nombre = ui.input('Nombre').props('color=light-green-14')
            telefono = ui.input('Teléfono').props('color=light-green-14')

        pagado = ui.switch('Pagado').classes('switch')

        if accion == 'Carga':
            clearInputs(cancha, fecha, horario, nombre, telefono)
            with ui.row():
                ui.button('Finalizar reserva', icon='done', color='#89CC04', on_click=lambda: confirmarReserva(dialog, fecha, horario, nombre, precio, telefono, pagado)).style('color: black')
                ui.button('Cancelar reserva', icon='close', color='#CC1B18', on_click=lambda: dialog.close()).style('color: black')
        elif accion == 'Edicion':
            loadInputs(msg, cancha, fecha, horario, nombre, telefono, pagado)
            with ui.row():
                ui.button('Editar reserva', icon='done', color='#89CC04', on_click=lambda: editarReserva(msg, dialog, fecha, horario, nombre, precio, telefono, pagado)).style('color: black')
                ui.button('Cancelar edicion', icon='close', color='#CC1B18', on_click=lambda: dialog.close()).style('color: black')
        elif accion == 'Borrado':
            loadInputs(msg, cancha, fecha, horario, nombre, telefono, pagado)
            
            cancha.disable()
            date_input.disable()
            horario.disable()
            nombre.disable()
            telefono.disable()
            pagado.disable()

            with ui.row():
                ui.button('Borrar reserva', icon='done', color='#89CC04', on_click=lambda: borrarReserva(dialog, msg)).style('color: black')
                ui.button('Cancelar borrado', icon='close', color='#CC1B18', on_click=lambda: dialog.close()).style('color: black')

    dialog.open()

#ESTADISTICAS
#Cancha con mas reservas
def demandaCancha(turnos):
    cantidadMax = 0
    #contar las reservas de cada cancha con un diccionario
    contadorReservas = {"Adentro 1": 0, "Adentro 2": 0, "Afuera 1":0, "Afuera 2":0} #todas las canchas inician en 0
    for turno in turnos:
        cancha = turno ["cancha"] #busca la cancha
        contadorReservas[cancha] += 1
        
        #comparativa de mayor cantidad de alquieres (esta medio al cuete esto)
        if contadorReservas[cancha] > cantidadMax:
            cantidadMax = contadorReservas[cancha]
            mayorDemanda = cancha
            
    return contadorReservas, mayorDemanda

#Horario con mas demanda
def demandaHorario(turnos):
    
    #contar reservas por horarios con diccionario
    contadorHorarios = {
    "08:00" : 0, "09:30" : 0, "11:00" : 0, "12:30" : 0, "14:00" : 0, "15:30" : 0, "17:00" : 0,  "18:30" : 0, "20:00" : 0, "21:30" : 0
    }    
    #todos los horarios inician en 0

    for turno in turnos:
        hora = turno["hora"]
        contadorHorarios[hora] += 1
    return contadorHorarios

#Reservas por dia/mes
def cantidadReservas(turnos):
    #diccionarios vacios
    reservasDia = {} #almacena reservas por dia (YYYY-MM-DD)
    reservasMes = {} #almacena reservas por mes (YYYY-MM)

    #recorre el diccionario de los turnos
    for turno in turnos:
        fecha = turno["fecha"]
        reservasDia[fecha] = reservasDia.get(fecha, 0) + 1  #el metodo .get() es una forma flexible de buscar un valor en un diccionario, permitiendo especificar un valor por defecto cuando la clave no existe.
        #recorta mes y ano
        mes = fecha[5:7] #(MM)
        reservasMes[mes] = reservasMes.get(mes, 0) + 1  #Inicializa en 0 si el mes no existe
    return reservasMes, reservasDia

#Ingresos totales
def ingresosTotales(turnos):
    ingMes = {}
    
    for turno in turnos:
        precio = float(turno["precio"][1:])
        fecha = turno["fecha"]  #formato YYYY-MM-DD
        mes = fecha[5:7] #(MM)
        pago = turno["pagado"]
        
        #Verificar si el cliente pago o no pago para luego sumarlo al total ingresado
        if pago == True:
            #Sumar el precio al total del mes correspondiente
            if mes in ingMes:
                ingMes[mes] += precio  #Suma el precio si el mes ya está en el diccionario
            else:
                ingMes[mes] = precio  
        else:
            pass
        
    #Ingreso total anual
    totalAnual = sum(ingMes.values())
    return ingMes, totalAnual

ui.add_css('''
            .switch .q-toggle__inner--truthy .q-toggle__track {
                background-color: #8ACE00;
            }
            .switch .q-toggle__inner--truthy .q-toggle__thumb::after {
                background-color: #8ACE00;
            }
''')

ui.dark_mode().enable()
ui.tab.default_style('color: #8ACE00')
ui.page_title('Turnero Canchas de Paddle')

with ui.tabs() as tabs:
    ui.tab('r', label='Reservas', icon='view_list')
    ui.tab('e', label='Estadisticas', icon='analytics')
with ui.tab_panels(tabs, value='r').classes('w-full').style('background-color: #89CC04'):
    with ui.tab_panel('r'):
        with ui.row(align_items='end').classes('w-full'):
            ui.space()
            ui.button('Cargar Reserva', icon='add_circle_outline', color='black', on_click=lambda: inputsReserva('Carga')).style('color: #89CC04')
        
        datos = sqlite_functions.readRows()

        columnas = [
            {'name': 'id', 'label': 'Nº Reserva', 'field': 'id'},
            {'name': 'cancha', 'label': 'Cancha', 'field': 'cancha', 'sortable': True},
            {'name': 'fecha', 'label': 'Fecha', 'field': 'fecha', 'sortable': True},
            {'name': 'hora', 'label': 'Horario', 'field': 'hora', 'sortable': True},
            {'name': 'nombre', 'label': 'Nombre', 'field': 'nombre'},
            {'name': 'precio', 'label': 'Precio', 'field': 'precio'},
            {'name': 'telefono', 'label': 'Contacto', 'field': 'telefono'},
            {'name': 'pagado', 'label': 'Pagado', 'field': 'pagado', 'sortable': True}
        ]
        reservas = []

        for reserva in datos:
            reservas.append(formatFila(reserva))
        
        with ui.table(columns=columnas, rows=reservas).classes('w-full') as table:
            table.add_slot('header', r'''
                <q-tr :props="props">
                    <q-th v-for="col in props.cols" :key="col.name" :props="props">
                        {{ col.label }}
                    </q-th>
                    <q-th auto-width />
                </q-tr>
            ''')
            table.add_slot('body', r'''
                <q-tr :props="props">
                    <q-td v-for="col in props.cols" :key="col.name" :props="props">
                        {{ col.value }}
                    </q-td>
                    <q-td auto-width>
                        <q-btn @click="$parent.$emit('editar', props.row)" icon="edit" flat dense color='blue'/>
                        <q-btn @click="$parent.$emit('borrar', props.row)" icon="delete" flat dense color='red'/>
                    </q-td>
                </q-tr>
            ''')
            table.on('editar', lambda msg: inputsReserva('Edicion', msg))
            table.on('borrar', lambda msg: inputsReserva('Borrado', msg))
        
    with ui.tab_panel('e'):
        reservasPorCancha, canchaMasUsada = demandaCancha(reservas) #Llama la funcion

        #Grafico para cancha
        ui.label('Demanda segun la cancha')
        columns = [ #1: clave, 2: titulo,
            {'name': 'cancha', 'label': 'CANCHA', 'field': 'cancha', 'align': 'left'},
            {'name': 'reservas', 'label': 'RESERVAS', 'field': 'reservas', 'sortable': True},
        ]
        rows = [{'cancha': cancha, 'reservas': cantidad} for cancha, cantidad in reservasPorCancha.items()]

        def updateReservas():
            rows.clear()  # Limpiar las filas antes de actualizarlas
            rows.extend([{'cancha': cancha, 'reservas': cantidad} for cancha, cantidad in reservasPorCancha.items()])

        ui.table(columns=columns, rows=rows, row_key='cancha')

        totalMes, totalDias = cantidadReservas(reservas)
        #Grafico para demada dias xmes
        totalReservasDias = [{"dia": dia, "cantidad": cantidad} for dia, cantidad in totalDias.items()]
        graficoDias = ui.echart({
            'title': {
                'text': 'Demanda según los días',
                'left': 'center'
            },
            'xAxis': {'type': 'category', 
                    'data': [d ["dia"] for d in totalReservasDias]}, #Dias en el eje X
            'yAxis': {'type': 'value'}, #Reservas en el eje Y
            'legend': {'textStyle': {'color': 'gray'}},
            'series': [
                {
                'name': 'Cantidad de reservas',
                'type': 'bar',
                'data': [c ["cantidad"] for c in totalReservasDias]
                }
            ],
        }).classes('w-full h-80')

        def updateDias():
            graficoDias.options['xAxis']['data'] = [dia for dia, cantidad in totalDias.items()]
            graficoDias.options['series'][0]['data'] = [cantidad for dia, cantidad in totalDias.items()]
            graficoDias.update() 
            
        graficoDias.options['title'] = {
            'text': f'Demanda segun los dias',
            'left': 'center'
        }

        ui.button('Actualizar datos', on_click=updateReservas)

        horarios = demandaHorario(reservas) #Llama la funcion
        #Grafico para horarios
        datosHorarios = [{"hora": hora, "reservas": cantidad} for hora, cantidad in horarios.items()]
        graficoHorarios = ui.echart({
            'title': {
                'text': 'Demanda según los horarios',
                'left': 'center'
            },
            'xAxis': {'type': 'category', 
                    'data': [h ["hora"] for h in datosHorarios]}, #Horarios en el eje X
            'yAxis': {'type': 'value'}, #Reservas en el eje Y
            'legend': {'textStyle': {'color': 'gray'}},
            'series': [
                {
                'name': 'Cantidad de reservas',
                'type': 'bar',
                'data': [c ["reservas"] for c in datosHorarios]
                }
            ],
        }).classes('w-full h-80')

        def updateHorarios():
            graficoHorarios.options['xAxis']['data'] = [hora for hora, cantidad in horarios.items()]
            graficoHorarios.options['series'][0]['data'] = [cantidad for hora, cantidad in horarios.items()]
            graficoHorarios.update() 

        ui.button('Actualizar horarios', on_click=updateHorarios)

        ingresosMes, ingresoAnual = ingresosTotales(reservas)
        #Grafico para los ingresos
        datosIngresos = [{"mes": mes, "cantidad": cantidad} for mes, cantidad in ingresosMes.items()]
        graficoIngresos = ui.echart({
            'xAxis': {'type': 'category', 'data': [m ["mes"] for m in datosIngresos]}, #Ingresos en el eje X
            'yAxis': {'type': 'value'}, #Reservas en el eje Y
            'legend': {'textStyle': {'color': 'gray'}},
            'series': [
                {
                'type': 'bar',
                'data': [c ["cantidad"] for c in datosIngresos]
                }
            ],
        }).classes('w-full h-80')

        #total anual al gráfico de ingresos
        graficoIngresos.options['title'] = {
            'text': f'Total Anual: ${ingresoAnual}',
            'subtext': 'Ingresos acumulados',
            'left': 'center'
        }

        def updateIngresos():
            rows.clear()  #Limpiar las filas antes de actualizarlas
            rows.extend([{"mes": mes, "cantidad": cantidad} for mes, cantidad in ingresosMes.items()])

        ui.button('Actualizar Ingresos', on_click=updateIngresos)

ui.run()