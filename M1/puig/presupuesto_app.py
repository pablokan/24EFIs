from nicegui import ui
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, Color
from datetime import datetime
import os
import sqlite3

# Lista para almacenar los ítems de presupuesto
items = []
# Variable global para llevar el contador de presupuestos
PRESUPUESTO_COUNTER = 0
# Variable global para almacenar los productos de la base de datos
productos = []
# Definimos las dimensiones del logo como constantes al inicio del archivo
LOGO_WIDTH = 250
LOGO_HEIGHT = 100

def cargar_productos():
    """Carga los productos desde la base de datos"""
    global productos
    try:
        conn = sqlite3.connect('materiales.db')
        c = conn.cursor()
        c.execute('SELECT cod, descripcion, precio FROM materiales')
        productos = [{'cod': row[0], 'descripcion': row[1], 'precio': row[2]} for row in c.fetchall()]
        conn.close()
        return True
    except Exception as e:
        ui.notify(f'Error al cargar productos: {str(e)}', color='negative')
        return False

def actualizar_descripcion(e):
    """Actualiza el precio cuando se selecciona un producto"""
    selected_product = next((p for p in productos if p['descripcion'] == description_input.value), None)
    if selected_product:
        price_input.text = f'Precio Unitario: ${selected_product["precio"]:.2f}'

def generate_pdf():
    if not items:
        ui.notify('Agregue al menos un ítem al presupuesto', color='warning')
        return
        
    if not name_input.value:
        ui.notify('Ingrese el nombre del cliente', color='warning')
        return

    # Incrementar el contador de presupuestos
    global PRESUPUESTO_COUNTER
    PRESUPUESTO_COUNTER += 1

    # Crear nombre del archivo con fecha y hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Crear directorio 'presupuestos' si no existe
    if not os.path.exists('presupuestos'):
        os.makedirs('presupuestos')
    
    filename = os.path.join('presupuestos', f"presupuesto_{timestamp}.pdf")
    
    # Crear el documento PDF
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    # Contenedor para los elementos del PDF
    elements = []
    
    # Estilos personalizados
    styles = getSampleStyleSheet()
    
    # Estilo para el título principal
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=5,
        alignment=0  # Alineado a la izquierda
    )

    # Estilo para subtítulos
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=13,
        textColor=HexColor('#2d3748'),
        spaceAfter=10,
        alignment=0,
        leading=18  # Alineado a la izquierda
    )

    # Estilo normal
    normal_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#2d3748'),
        spaceAfter=20,
        alignment=0  # Alineado a la izquierda
    )
    
    # Estilo para el número de presupuesto
    number_style = ParagraphStyle(
        'NumberStyle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=HexColor('#4a5568'),
        spaceAfter=5,
        alignment=0  # Alineado a la izquierda
    )
    
    # Estilo para la fecha
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#4a5568'),
        spaceAfter=20,
        alignment=0  # Alineado a la izquierda
    )

    # Crear tabla para el encabezado (título y logo)
    try:
        logo = Image('images/logo.png', width=LOGO_WIDTH/72*inch, height=LOGO_HEIGHT/72*inch)  # Convertimos px a inches
        header_data = [
            [
                # Columna izquierda con título y detalles
                Table([
                    [Paragraph("PRESUPUESTO", title_style)],
                    [Paragraph(f"Presupuesto N°: {PRESUPUESTO_COUNTER:04d}", number_style)],
                    [Paragraph(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", date_style)]
                ], colWidths=[4*inch]),
                # Columna derecha con logo
                logo
            ]
        ]
    except:
        # Si no encuentra el logo, usar solo el texto
        header_data = [
            [
                Table([
                    [Paragraph("PRESUPUESTO", title_style)],
                    [Paragraph(f"Presupuesto N°: {PRESUPUESTO_COUNTER:04d}", number_style)],
                    [Paragraph(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", date_style)]
                ], colWidths=[4*inch]),
                ""
            ]
        ]

    header_table = Table(header_data, colWidths=[4*inch, 3*inch])
    header_table.setStyle(TableStyle([
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),  # Alinear logo a la derecha
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Alineación vertical al centro
        ('LEFTPADDING', (0, 0), (-1, -1), 0),  # Sin padding izquierdo
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),  # Sin padding derecho
    ]))
    
    elements.append(header_table)
    elements.append(Spacer(1, 20))
    
    # Información del cliente en una tabla
    client_data = [
        [Paragraph("<b>INFORMACIÓN DEL CLIENTE</b>", subtitle_style)]
    ]
    
    client_info = []
    if name_input.value:
        client_info.append(f"<b>Cliente:</b> {name_input.value}")
    if address_input.value:
        client_info.append(f"<b>Dirección:</b> {address_input.value}")
    if phone_input.value:
        client_info.append(f"<b>Teléfono:</b> {phone_input.value}")
    
    client_data.append([Paragraph("<br/>".join(client_info), normal_style)])
    
    client_table = Table(client_data, colWidths=[7*inch])
    client_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#f7fafc')),
        ('BOX', (0, 0), (-1, -1), 1, HexColor('#e2e8f0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#2d3748')),
        ('PADDING', (0, 0), (-1, -1), [6, 4, 20, 6]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrar verticalmente
    ]))
    
    elements.append(client_table)
    elements.append(Spacer(1, 20))
    
    # Tabla de items con estilo moderno
    table_data = [['Descripción', 'Cantidad', 'Precio Unitario', 'Total']]  # Encabezado de la tabla
    for item in items:
        table_data.append([
            item['descripcion'],
            f"{item['cantidad']:.2f}",
            f"${item['precio_unitario']:.2f}",
            f"${item['total']:.2f}"
        ])
    
    # Calcular totales
    subtotal = sum(item['total'] for item in items)
    if vat_checkbox.value:
        iva = subtotal * 0.21
        total = subtotal + iva
    else:
        iva = 0
        total = subtotal
    
    # Agregar filas para Subtotal, IVA y Total
    table_data.append([None, None, 'Subtotal:', f"${subtotal:.2f}"])  # Usar None en lugar de ''
    if vat_checkbox.value:
        table_data.append([None, None, 'IVA (21%):', f"${iva:.2f}"])
    table_data.append([None, None, 'Total:', f"${total:.2f}"])

    
    # Crear tabla con estilo moderno
    table = Table(table_data, colWidths=[4*inch, 1*inch, 1.25*inch, 1.25*inch])
    # Aplica estilo específico para el encabezado y las filas de datos
    table.setStyle(TableStyle([
    # Estilo del encabezado
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#3b82f6')),  # Color azul para encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Texto blanco en el encabezado
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),  # Alinear el texto del encabezado
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Negrita en encabezado
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),

        # Estilo del cuerpo de la tabla (datos)
        ('TEXTCOLOR', (0, 1), (-1, -1), HexColor('#2d3748')),  # Texto oscuro en los datos
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),  # Centrar cantidad, precio unitario y total
        ('FONTNAME', (0, 1), (-1, -4), 'Helvetica'),  # Fuente normal
        ('FONTSIZE', (0, 1), (-1, -4), 10),  # Tamaño de fuente para los datos
        ('BOTTOMPADDING', (0, 1), (-1, -4), 7),  # Aumentar espacio vertical en filas de datos
        ('TOPPADDING', (0, 1), (-1, -4), 7),
        ('GRID', (0, 0), (-1, -4), 1, HexColor('#e2e8f0')),  # Cuadrícula para las filas de datos
        ('VALIGN', (0, 0), (-1, -4), 'MIDDLE'),  # Alineación vertical en el medio

        # Estilo para los totales
        ('ALIGN', (2, -3), (-1, -1), 'RIGHT'),  # Alinear texto de Subtotal, IVA y Total a la derecha
        ('FONTNAME', (2, -3), (-1, -1), 'Helvetica-Bold'),  # Negrita en totales
        ('FONTSIZE', (2, -3), (-1, -1), 10),  # Tamaño de fuente para los totales
        ('TEXTCOLOR', (2, -3), (-1, -1), HexColor('#2d3748')),  # Texto oscuro para totales
        ('BOTTOMPADDING', (0, -4), (-1, -1), 7),  # Aumentar espacio vertical entre filas
        ('TOPPADDING', (0, -4), (-1, -1), 7),  # Aumentar espacio vertical entre filas
        # Eliminar líneas para los totales
        ('LINEBELOW', (0, -4), (-1, -4), 1, HexColor('#e2e8f0')),  # Línea solo antes de los totales
        ('LINEBELOW', (0, -3), (-1, -1), 0, colors.white),  # Eliminar bordes de Subtotal, IVA y Total
    ]))

    elements.append(table)
    
    # Agregar nota al pie
    elements.append(Spacer(1, 30))
    footer_text = "Gracias por su preferencia. Este presupuesto tiene una validez de 30 días."
    elements.append(Paragraph(footer_text, normal_style))
    
    # Generar PDF
    doc.build(elements)
    
    # Notificar al usuario
    ui.notify(f'PDF generado como "presupuestos/presupuesto_{timestamp}.pdf"', 
              color='positive', 
              position='center', 
              close_button=True, 
              timeout=5000)

# Agregado de items usando base de datos
def add_item():
    try:
        # Validar que los campos no estén vacíos
        if not description_input.value or not quantity_input.value:
            ui.notify('Por favor, complete todos los campos', color='negative')
            return

        # Buscar el producto seleccionado
        selected_product = next((p for p in productos if p['descripcion'] == description_input.value), None)
        if not selected_product:
            ui.notify('Por favor, seleccione un producto válido', color='negative')
            return

        # Crear un diccionario para el ítem
        item = {
            'descripcion': selected_product['descripcion'],
            'cantidad': float(quantity_input.value),
            'precio_unitario': selected_product['precio'],
            'total': float(quantity_input.value) * selected_product['precio']
        }
        
        # Agregar el ítem a la lista
        items.append(item)
        
        # Actualizar la tabla
        items_table.rows = items
        
        # Limpiar los campos de entrada
        description_input.value = ''
        quantity_input.value = None
        price_input.value = None
        
        # Actualizar el total
        update_total()
        
        ui.notify('Ítem agregado correctamente', color='positive')
        
    except ValueError:
        ui.notify('Por favor, ingrese una cantidad válida', color='negative')

def clear_all():
    if items:
        items.clear()
        items_table.rows = []
        update_total()
        ui.notify('Todos los ítems han sido eliminados', color='info')
    else:
        ui.notify('No hay ítems para eliminar', color='warning')

def clear_user_data():
    # Limpiar todos los campos de usuario
    name_input.value = ''
    address_input.value = ''
    phone_input.value = ''
    vat_checkbox.value = False
    ui.notify('Datos del cliente eliminados', color='info')

def update_total():
    total = sum(item['total'] for item in items)
    total_label.text = f'Total sin IVA: ${total:.2f}'
    if vat_checkbox.value:
        total_with_vat_label.text = f'Total con IVA (21%): ${total * 1.21:.2f}'
    else:
        total_with_vat_label.text = ''

def on_vat_change(e):
    update_total()

# Interfaz de usuario
with ui.card().classes('max-w-3xl mx-auto p-4 m-4'):
    # Cargar productos al inicio
    if not cargar_productos():
        ui.label('Error al cargar productos de la base de datos').classes('text-red-500')
    
    # Encabezado con logo y título
    with ui.row().classes('w-full items-center justify-between mb-4'):
        ui.label('Generador de Presupuestos').classes('text-2xl font-bold')
        ui.image('images/logo.png').style(f'height: {LOGO_HEIGHT}px; width: {LOGO_WIDTH}px; margin-left: auto; display: block; margin-right: 0;')

    # Sección de datos del cliente
    with ui.row().classes('w-full gap-4 mb-4'):
        with ui.column().classes('flex-1'):
            name_input = ui.input('Nombre del cliente').classes('w-full')
            address_input = ui.input('Dirección').classes('w-full')
        with ui.column().classes('flex-1'):
            phone_input = ui.input('Teléfono').classes('w-full')
            vat_checkbox = ui.checkbox('Incluir IVA (21%)', on_change=on_vat_change)
    
    # Botón para limpiar datos del usuario
    with ui.row().classes('w-full justify-end mb-4'):
        ui.button('Limpiar Datos del Cliente', on_click=clear_user_data).classes('bg-yellow-500 text-white')
    
    # Línea separadora visual
    ui.element('span').classes('block w-full border-t border-gray-200 my-4')
    
    # Sección de ingreso de ítems
    with ui.row().classes('w-full gap-4'):
        # Uso de select para la descripción
        description_input = ui.select(
            label='Producto',
            options=[p['descripcion'] for p in productos],
            on_change=actualizar_descripcion
        ).classes('flex-1')
        quantity_input = ui.number('Cantidad', min=0, format='%.2f').classes('w-32')
        price_input = ui.label('Precio Unitario: $0.00').classes('w-32')
        ui.button('Agregar Ítem', on_click=add_item).classes('bg-blue-500 text-white')

    # Tabla de ítems
    columns = [
        {'name': 'descripcion', 'label': 'Descripción', 'field': 'descripcion', 'align': 'left'},
        {'name': 'cantidad', 'label': 'Cantidad', 'field': 'cantidad', 'align': 'right'},
        {'name': 'precio_unitario', 'label': 'Precio Unitario', 'field': 'precio_unitario', 'align': 'right'},
        {'name': 'total', 'label': 'Total', 'field': 'total', 'align': 'right'}
    ]
    
    items_table = ui.table(
        columns=columns,
        rows=[],
        row_key='descripcion',
        pagination={'no-data-label': 'No hay datos', 'rows-per-page-label': 'Filas por página'}
    ).classes('w-full mt-4')

    # Botones de acción
    with ui.row().classes('w-full gap-4 mt-4'):
        ui.button('Generar PDF', on_click=generate_pdf).classes('bg-green-500 text-white')
        ui.button('Limpiar Todo', on_click=clear_all).classes('bg-red-500 text-white')

    # Sección de totales
    with ui.row().classes('w-full mt-4 justify-end gap-4'):
        total_label = ui.label('Total sin IVA: $0.00').classes('text-lg')
        total_with_vat_label = ui.label('').classes('text-lg font-bold')

ui.run()