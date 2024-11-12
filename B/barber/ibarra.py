from nicegui import ui
import sqlite3

#INTEGRANTES = Garay Santiago, Villavicencio Jonatan y Ibarra Matías


DB_NAME = 'barberia.db'

def crear_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT NOT NULL,
                Apellido TEXT NOT NULL,
                Celular TEXT,
                Correo TEXT,
                Personal TEXT,
                Trabajo TEXT,
                Fecha TEXT,
                Hora TEXT,
                Consultas TEXT
            )
        ''')
        conn.commit()

crear_db()

BACKGROUND_IMAGE_URL = 'https://joseppons.com/formacion/wp-content/uploads/2020/11/servicios-salon-barberia.jpeg'

staff = ['Jonatan Villavicencio', 'Matias Ibarra', 'Santiago Garay']

user_id = None

@ui.page('/')
def login_page():
    with ui.row().style(f'''
        background-image: url('{BACKGROUND_IMAGE_URL}');
        background-size: cover;
        height: 100vh;
        display: flex;
        width: 100vw;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
    '''):
        def tipo_usuario(nombre, apellido):
            usuario = f"{nombre} {apellido}"
            if usuario in staff:
                ui.navigate(staff_page())
            else:
                ui.navigate(main_page())
    
            nombre_input.value = ''
            apellido_input.value = ''

        with ui.element('div').style('background-color: rgba(0, 0, 5, 0.7); border-radius: 10px; padding: 20px;'):
            ui.markdown('**Iniciar Sesión**').style('font-size: 36px; font-weight: bold;')
            with ui.element('div').style('background-color: rgba(245, 245, 245); border-radius: 10px; padding: 20px;'):
                nombre_input = ui.input('Nombre')
                apellido_input = ui.input('Apellido')
                ui.button('Entrar', on_click=lambda: tipo_usuario(nombre_input.value, apellido_input.value))
                ui.notify('Esta siendo redireccionado')

@ui.page('/cliente')
def main_page():
    global user_id

    with ui.row().style(f'''
        background-image: url('{BACKGROUND_IMAGE_URL}');
        background-size: cover;
        height: 100vh;
        display: flex;
        width: 100vw;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
    '''):
        with ui.element('div').style('background-color: rgba(0, 0, 5, 0.7); border-radius: 10px; padding: 20px;'):
            ui.markdown('**Registro de Usuario**').style('font-size: 36px; font-weight: bold;')
            with ui.element('div').style('background-color: rgba(245, 245, 245); border-radius: 10px; padding: 20px;'):
                nombre_input = ui.input('Nombre')
                apellido_input = ui.input('Apellido')
                celular_input = ui.input('Celular')
                correo_input = ui.input('Correo')

            ui.button('Registrar', on_click=lambda: registrar_usuario(
                nombre_input.value, 
                apellido_input.value,
                celular_input.value,
                correo_input.value,
            ))

            ui.label("\r") 
            ui.markdown('**Gestión de Barbería**').style('font-size: 36px; font-weight: bold;').classes('text-brand')
            ui.label("\r") 
            ui.label('Selecciona una opción:').style('font-size: 18px;')
            
            radio2 = ui.radio({1: 'Turnos Online', 2: 'Consultas', 3: 'Ubicación'}).props('inline')
            ui.button('Seleccionar', on_click=lambda: seleccionar_radio(radio2.value))
            ui.separator()
            ui.separator()

            turnos_container = ui.element('div').style('display: none;')
            consultas_container = ui.element('div').style('display: none;')
            ubicacion_container = ui.element('div').style('display: none;')
            personal_trabajo_container = ui.element('div').style('display: none;')

            def seleccionar_radio(value):
                turnos_container.style('display: none;')
                consultas_container.style('display: none;')
                ubicacion_container.style('display: none;')

                if value == 1:
                    turnos_container.style('display: block;')
                    manejar_turnos(turnos_container)
                elif value == 2:
                    consultas_container.style('display: block;')
                    manejar_consultas(consultas_container)
                elif value == 3:
                    ubicacion_container.style('display: block;')
                    manejar_ubicacion(ubicacion_container)

            def registrar_usuario(nombre, apellido, celular, correo):
                if not nombre or not apellido or not celular or not correo:
                    ui.notify('Por favor, completa todos los campos.')
                    return

                with sqlite3.connect(DB_NAME) as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute('INSERT INTO usuarios (Nombre, Apellido, Celular, Correo) VALUES (?, ?, ?, ?)', 
                                       (nombre, apellido, celular, correo))
                        global user_id
                        user_id = cursor.lastrowid
                        conn.commit()
                        ui.notify(f'Usuario {nombre} {apellido} registrado con éxito!')
                    except Exception as e:
                        ui.notify(f'Error al registrar usuario: {e}')
                        print(f'Error: {e}')

            def manejar_turnos(container):
                container.clear()  
                ui.notify('Seleccionaste: Turnos Online')
                
                with container:
                    with ui.element('div').style('background-color: rgba(245, 245, 245); border-radius: 10px; padding: 20px;'):
                        with ui.input('Fecha') as date:
                            with ui.menu().props('no-parent-event') as menu:
                                with ui.date().bind_value(date):
                                    with ui.row().classes('justify-end'):
                                        ui.button('Aceptar', on_click=menu.close).props('flat')
                        with date.add_slot('append'):
                            ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
                    ui.separator()
                    with ui.element('div').style('background-color: rgba(245, 245, 245); border-radius: 10px; padding: 20px;'):
                        with ui.input('Hora') as time:
                            with ui.menu().props('no-parent-event') as menu:
                                with ui.time().bind_value(time):
                                    with ui.row().classes('justify-end'):
                                        ui.button('Aceptar', on_click=menu.close).props('flat')
                        with time.add_slot('append'):
                            ui.icon('access_time').on('click', menu.open).classes('cursor-pointer')
                    ui.separator()
                    ui.button('Confirmar', on_click=lambda: guardar_turno(
                        date.value,
                        time.value
                    ))

            def guardar_turno(fecha, hora):
                if not fecha or not hora:
                    ui.notify('Por favor, completa la fecha y la hora.')
                    return
            
                from datetime import datetime
                try:
                    fecha_formateada = datetime.strptime(fecha, '%Y-%m-%d').date()
                    hora_formateada_str = datetime.strptime(hora, '%H:%M').time().strftime('%H:%M:%S')
                except ValueError:
                    ui.notify('Error en el formato de fecha u hora. Por favor, verifica.')
                    return
            
                with sqlite3.connect(DB_NAME) as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute('UPDATE usuarios SET Fecha = ?, Hora = ? WHERE id = ?', 
                                       (fecha_formateada, hora_formateada_str, user_id))
                        conn.commit()
                        ui.notify(f'Turno registrado para el día {fecha_formateada} y hora {hora_formateada_str}')
                        mostrar_seleccion_personal_trabajo()
                    except Exception as e:
                        ui.notify(f'Error al registrar el turno: {e}')

            def mostrar_seleccion_personal_trabajo():
                personal_trabajo_container.clear()
                personal_trabajo_container.style('display: block;')
                ui.notify("Por favor, selecciona el personal y el trabajo.")

                with personal_trabajo_container:
                    with ui.element('div').style('background-color: rgba(245, 245, 245); border-radius: 10px; padding: 20px;'):
                        personal = ui.select(["Jonatan", "Matias", "Santiago"], label="Seleccionar Personal")
                        trabajo = ui.select(["Corte", "Afeitado", "Tintura", "Corte + Afeitado", "Corte + Tintura", "Afeitado + Tintura"], label="Seleccionar Trabajo")
                        ui.button('Guardar Selección', on_click=lambda: guardar_personal_trabajo(personal.value, trabajo.value))

            def guardar_personal_trabajo(personal, trabajo):
                if not personal or not trabajo:
                    ui.notify('Por favor, selecciona el personal y el trabajo.')
                    return

                with sqlite3.connect(DB_NAME) as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute('UPDATE usuarios SET Personal = ?, Trabajo = ? WHERE id = ?', 
                                       (personal, trabajo, user_id))
                        conn.commit()
                        ui.notify(f'Selección de personal y trabajo guardada exitosamente: {personal} - {trabajo}')
                    except Exception as e:
                        ui.notify(f'Error al guardar selección: {e}')

            def manejar_consultas(container):
                container.clear() 
                ui.notify('Seleccionaste: Consultas')
                with container:
                    with ui.element('div').style('background-color: rgba(245, 245, 245); border-radius: 10px; padding: 20px;'):
                        with ui.row().classes('text-4xl'):
                            ui.icon('chat').style('background-color: #33d17a')
                            consulta_input = ui.input('Consultas...').style('font-size: 20px;')
                            ui.button('Enviar', on_click=lambda: enviar_consulta(consulta_input.value))

            def enviar_consulta(consulta):
                if not consulta:
                    ui.notify('Por favor, escribe tu consulta.')
                    return

                with sqlite3.connect(DB_NAME) as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute('UPDATE usuarios SET Consultas = ? WHERE id = ?', (consulta, user_id))
                        conn.commit()
                        ui.notify('La consulta ha sido enviada con éxito!')
                    except Exception as e:
                        ui.notify(f'Error al enviar consulta: {e}')

            def manejar_ubicacion(container):
                container.clear()  
                ui.notify('Seleccionaste: Ubicación')
                with container:
                    ui.label('Wenceslao Tejerina Nte. 783').style('font-size: 18px;')
                    m = ui.leaflet(center=(-33.100982, -64.367903))
                    marker = m.marker(latlng=m.center)
                    ui.button('Move marker', on_click=lambda: marker.move(-33.100982, -64.367903))

@ui.page('/Staff_page')
def staff_page():
    with ui.row().style(f'''
        background-image: url('{BACKGROUND_IMAGE_URL}');
        background-size: cover;
        height: 100vh;
        display: flex;
        width: 100vw;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
    '''):
        with ui.element('div').style('background-color: rgba(0, 0, 5, 0.7); border-radius: 10px; padding: 20px;'):
            ui.markdown('**Bienvenido!**').style('font-size: 36px; font-weight: bold;')
            with ui.element('div').style('background-color: rgba(245, 245, 245); border-radius: 10px; padding: 20px;'):
                ui.label.default_style('color: tomato')('Esto es lo que tenemos para hoy!')
                
                echart = ui.echart({
                    'xAxis': {'type': 'category', 'data': []},
                    'yAxis': {'type': 'value'},
                    'legend': {'textStyle': {'color': 'gray'}},
                    'series': [
                        {'type': 'bar', 'name': 'Corte', 'data': []},
                        {'type': 'bar', 'name': 'Afeitado', 'data': []},
                        {'type': 'bar', 'name': 'Tintura', 'data': []}
                    ],
                })

                def actualizar_grafico():
                    with sqlite3.connect(DB_NAME) as conn:
                        cursor = conn.cursor()
                        
                        cursor.execute('''
                            SELECT Fecha,
                                   SUM(CASE WHEN Trabajo = 'Corte' THEN 1 ELSE 0 END) AS Corte,
                                   SUM(CASE WHEN Trabajo = 'Afeitado' THEN 1 ELSE 0 END) AS Afeitado,
                                   SUM(CASE WHEN Trabajo = 'Tintura' THEN 1 ELSE 0 END) AS Tintura
                            FROM usuarios
                            WHERE Trabajo IS NOT NULL AND Fecha IS NOT NULL
                            GROUP BY Fecha
                            ORDER BY Fecha
                        ''')
                        resultados = cursor.fetchall()

                        fechas = [fila[0] for fila in resultados]
                        cortes = [fila[1] for fila in resultados]
                        afeitados = [fila[2] for fila in resultados]
                        tinturas = [fila[3] for fila in resultados]

                        echart.options['xAxis']['data'] = fechas
                        echart.options['series'][0]['data'] = cortes
                        echart.options['series'][1]['data'] = afeitados
                        echart.options['series'][2]['data'] = tinturas
                        echart.update()

                ui.button('Actualizar Datos', on_click=actualizar_grafico)

ui.run()