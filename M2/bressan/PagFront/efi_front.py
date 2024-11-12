import reflex as rx
from rxconfig import config


#frontend pagina principal
def index() -> rx.Component:
    page = rx.container(

        #configuración de la imagen de fondo
        rx.box(
        background_image="url('https://c.wallhere.com/photos/c1/e5/space_planet_galaxy_Milky_Way_Sun_digital_art-2288004.jpg!d')",  
        background_size="cover",  
        background_repeat="no-repeat",  
        background_position="center center",  
        filter="blur(3px)",  #desenfoque solo al fondo
        background_attachment="fixed",  
        position="absolute",  
        top="0",  
        left="0",  
        right="0",  
        bottom="0",  
        z_index="-1"  #coloca el fondo detrás
        ),

        #ajusta el brillo de la imagen de fondo 
        rx.box(
            background_color="rgba(0, 0, 0, 0.5)",  #opacidad
            position="absolute",  
            top="0",  
            left="0",  
            right="0",  
            bottom="0",  
            z_index="-1"  
        ),

        # Borde Superior y logo
        rx.box(
            rx.text(
                "iTec ", 
                color="black", 
                display="inline",
                font_size="3em",  #aumenta el tamaño de la fuente
                font_weight="bold"
            ),
            rx.text(
                "Store", 
                color="red", 
                display="inline",
                font_size="2.5em", 
                font_weight="bold"
            ),
            
            #boton admin
            rx.button("Admin", href="/admin", background_color="rgba(0, 0, 0, 0.7)", font_size="1em", padding="10px 20px", border_radius="10px", position="absolute", right="20px", top="40%", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),

            text_align="center",
            padding="10px 0",  
            width="100%",  
            border_bottom="8px solid red",  
            position="fixed",  
            top="0",  
            left="0",  
            z_index="1000",  
            background_color="rgba(255, 255, 255, 0.65)" 
        ),

        #contenedor principal del grid
        rx.container(
            rx.heading("ELIJA SUS COMPONENTES", text_align="center", margin_bottom="10px", color='black'),
            rx.divider(size="15px", width="100%", margin="0", border_width="2px", color='white', margin_bottom="10px"),  
            rx.grid(
                #boton Mother
                rx.button("Motherboard", href="/componente/motherboard", background_color="rgba(0, 0, 0, 0.7)", color="white", border_radius="10px", padding="20px", font_size="1em", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),

                #boton Disk SSD
                rx.button("Disk SSD", href="/componente/diskSSD", background_color="rgba(0, 0, 0, 0.7)", color="white", border_radius="10px", padding="20px", font_size="1em", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),

                #boton Disk HDD
                rx.button("Disk HDD", href="/componente/diskHDD", background_color="rgba(0, 0, 0, 0.7)", color="white", border_radius="10px", padding="20px", font_size="1em", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),

                #boton Processor
                rx.button("Processor", href="/componente/processor", background_color="rgba(0, 0, 0, 0.7)", color="white", border_radius="10px", padding="20px", font_size="1em", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),

                #boton RAM
                rx.button("Memory RAM", href="/componente/RAM", background_color="rgba(0, 0, 0, 0.7)", color="white", border_radius="10px", padding="20px", font_size="1em", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),

                #boton GPU
                rx.button("GPU", href="/componente/gpu", background_color="rgba(0, 0, 0, 0.7)", color="white", border_radius="10px", padding="20px", font_size="1em", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),

                #Boton Fuente de poder
                rx.button("Power supply", href="/componente/supplypow", background_color="rgba(0, 0, 0, 0.7)", color="white", border_radius="10px", padding="20px", font_size="1em", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),

                #boton Gabinete
                rx.button("Computer Case", href="/componente/Casecomp", background_color="rgba(0, 0, 0, 0.7)", color="white", border_radius="10px", padding="20px", font_size="1em", _hover={"background_color": "rgba(0, 0, 0, 0.9)"}),
                
                columns="2",
                spacing="4",
                width="100%",
                padding="20px",
                background_color="rgba(255, 255, 255, 0.8)",
                border_radius="15px",
            ),
            background_color="rgba(255, 255, 255, 0.8)",
            border_radius="15px",
            width="80%",
            margin="80px auto",
            box_shadow="0px 4px 8px rgba(16, 3, 4, 0.15)"
        ),

        #Slogan
        rx.box(
            rx.text(
                " Tu universo, Tu nave, Tu PC ", 
                color="white", 
                font_size="1em",  #tamaño de la fuente
                font_weight="light",  #fuente fina
                text_align="center",
                letter_spacing="10px",
                padding="20px 0"
            ),
            width="100%",
            position="absolute",
            top="15%",  #ajustar posicion vertical
            left="0",
            z_index="1000"
        ),

        display="flex",
        justify_content="center",
        align_items="center",
        min_height="100vh",  #altura mínima para centrar verticalmente

    )
    return page

app = rx.App()
app.add_page(index)
app._compile
