import sqlite3

from pregs import Pregunta

conn = sqlite3.connect('preguntas.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS preguntas(
          id INTEGER PRIMARY KEY,
          pregunta TEXT NOT NULL,
          r1 TEXT NOT NULL,
          r2 TEXT NOT NULL,
          r3 TEXT NOT NULL,
          rc TEXT NOT NULL  ) """)

p1 = Pregunta(1,'¿Cuál es el país más grande del mundo en superficie?', 'Canadá', 'China', 'Estados Unidos', 'Rusia')
p2 = Pregunta(2,'¿Quién pintó la famosa obra "La última cena"?', 'Vincent van Gogh', 'Miguel Ángel', 'Pablo Picasso', 'Leonardo da Vinci')
p3 = Pregunta(3,'¿Cuál es el planeta más cercano al Sol?', 'Venus', 'Tierra', 'Marte', 'Mercurio')
p4 = Pregunta(4,'¿En qué país se encuentra la Torre Eiffel?', 'Alemania', 'Italia', 'España', 'Francia')
p5 = Pregunta(5,'¿Quién escribió "Cien años de soledad"?', 'Mario Vargas Llosa', 'Julio Cortázar', 'Isabel Allende', 'Gabriel García Márquez')
p6 = Pregunta(6,'¿Cuál es el elemento químico representado por la letra "O"?', 'Oro', 'Hidrógeno', 'Oxalato', 'Oxígeno')
p7 = Pregunta(7,'¿Qué país es conocido como la cuna del Renacimiento?', 'Francia', 'España', 'Grecia', 'Italia')
p8 = Pregunta(8,'¿Cuál es la capital de Australia?', 'Sídney', 'Melbourne', 'Brisbane', 'Canberra')
p9 = Pregunta(9,'¿Cuál es el océano más grande del mundo?', 'Océano Atlántico', 'Océano Índico', 'Océano Ártico', 'Océano Pacífico')
p10 = Pregunta(10,'¿En qué año llegó el hombre a la Luna por primera vez?', '1965', '1972', '1963', '1969')
p11 = Pregunta(11,'¿Cuál es la moneda oficial de Japón?', 'Won', 'Yuan', 'Dólar', 'Yen')
p12 = Pregunta(12,'¿Qué es el Everest?', 'Un volcán', 'Un río', 'Una isla', 'Una montaña')
p13 = Pregunta(13,'¿Quién escribió "Don Quijote de la Mancha"?', 'Federico García Lorca', 'Juan Rulfo', 'Pablo Neruda', 'Miguel de Cervantes')
p14 = Pregunta(14,'¿Qué país ganó la Copa Mundial de Fútbol en 2018?', 'Brasil', 'Argentina', 'España', 'Francia')
p15 = Pregunta(15,'¿Cuál es el río más largo del mundo?', 'Nilo', 'Yangtsé', 'Misisipi', 'Amazonas')
p16 = Pregunta(16,'¿Qué continente es conocido como "la cuna de la humanidad"?', 'Asia', 'Europa', 'América', 'África')
p17 = Pregunta(17,'¿Quién es el dios principal de la mitología griega?', 'Apolo', 'Ares', 'Poseidón', 'Zeus')
p18 = Pregunta(18,'¿Cuál es el idioma más hablado en el mundo?', 'Inglés', 'Francés', 'Español', 'Mandarín')
p19 = Pregunta(19,'¿Cuál es el órgano más grande del cuerpo humano?', 'Hígado', 'Corazón', 'Cerebro', 'Piel')
p20 = Pregunta(20,'¿Qué país es conocido por ser el lugar de origen del tango?', 'Chile', 'Perú', 'Uruguay', 'Argentina')



list_preguntas = [
    (p1.id, p1.preg, p1.rta1, p1.rta2, p1.rta3, p1.rta_c),
    (p2.id, p2.preg, p2.rta1, p2.rta2, p2.rta3, p2.rta_c),
    (p3.id, p3.preg, p3.rta1, p3.rta2, p3.rta3, p3.rta_c),
    (p4.id, p4.preg, p4.rta1, p4.rta2, p4.rta3, p4.rta_c),
    (p5.id, p5.preg, p5.rta1, p5.rta2, p5.rta3, p5.rta_c),
    (p6.id, p6.preg, p6.rta1, p6.rta2, p6.rta3, p6.rta_c),
    (p7.id, p7.preg, p7.rta1, p7.rta2, p7.rta3, p7.rta_c),
    (p8.id, p8.preg, p8.rta1, p8.rta2, p8.rta3, p8.rta_c),
    (p9.id, p9.preg, p9.rta1, p9.rta2, p9.rta3, p9.rta_c),
    (p10.id, p10.preg, p10.rta1, p10.rta2, p10.rta3, p10.rta_c),
    (p11.id, p11.preg, p11.rta1, p11.rta2, p11.rta3, p11.rta_c),
    (p12.id, p12.preg, p12.rta1, p12.rta2, p12.rta3, p12.rta_c),
    (p13.id, p13.preg, p13.rta1, p13.rta2, p13.rta3, p13.rta_c),
    (p14.id, p14.preg, p14.rta1, p14.rta2, p14.rta3, p14.rta_c),
    (p15.id, p15.preg, p15.rta1, p15.rta2, p15.rta3, p15.rta_c),
    (p16.id, p16.preg, p16.rta1, p16.rta2, p16.rta3, p16.rta_c),
    (p17.id, p17.preg, p17.rta1, p17.rta2, p17.rta3, p17.rta_c),
    (p18.id, p18.preg, p18.rta1, p18.rta2, p18.rta3, p18.rta_c),
    (p19.id, p19.preg, p19.rta1, p19.rta2, p19.rta3, p19.rta_c),
    (p20.id, p20.preg, p20.rta1, p20.rta2, p20.rta3, p20.rta_c),

]

p21 = Pregunta(21, '¿Cuál es el animal terrestre más rápido del mundo?', 'León', 'Caballo', 'Elefante', 'Guepardo')
p22 = Pregunta(22, '¿Cuál es la moneda de Reino Unido?', 'Euro', 'Dólar', 'Franco', 'Libra')
p23 = Pregunta(23, '¿Cuál es el metal más caro del mundo?', 'Plata', 'Platino', 'Cobre', 'Rodio')
p24 = Pregunta(24, '¿Qué es el Kilimanjaro?', 'Un río', 'Un volcán', 'Un océano', 'Una montaña')
p25 = Pregunta(25, '¿Cuál es el país más poblado del mundo?', 'India', 'Estados Unidos', 'Indonesia', 'China')
p26 = Pregunta(26, '¿Qué océano está al oeste de América?', 'Índico', 'Ártico', 'Antártico', 'Pacífico')
p27 = Pregunta(27, '¿En qué país se encuentra Machu Picchu?', 'México', 'Colombia', 'Brasil', 'Perú')
p28 = Pregunta(28, '¿Cuál es el órgano que bombea sangre en el cuerpo humano?', 'Pulmón', 'Estómago', 'Riñón', 'Corazón')
p29 = Pregunta(29, '¿Cuál es el elemento químico del agua?', 'CO2', 'O2', 'N2', 'H2O')
p30 = Pregunta(30, '¿Cuál es el deporte más popular del mundo?', 'Baloncesto', 'Tenis', 'Béisbol', 'Fútbol')
p31 = Pregunta(31, '¿Cuál es el país más pequeño del mundo?', 'Luxemburgo', 'Mónaco', 'San Marino', 'Vaticano')
p32 = Pregunta(32, '¿En qué ciudad se encuentra el Coliseo?', 'Atenas', 'Nápoles', 'París', 'Roma')
p33 = Pregunta(33, '¿Cuál es el principal gas de la atmósfera terrestre?', 'Oxígeno', 'Dióxido de carbono', 'Hidrógeno', 'Nitrógeno')
p34 = Pregunta(34, '¿Quién fue el primer hombre en el espacio?', 'Neil Armstrong', 'John Glenn', 'Buzz Aldrin', 'Yuri Gagarin')
p35 = Pregunta(35, '¿Qué planeta es conocido como el planeta rojo?', 'Júpiter', 'Saturno', 'Urano', 'Marte')
p36 = Pregunta(36, '¿Cuál es el país con más islas?', 'Brasil', 'Canadá', 'Noruega', 'Suecia')
p37 = Pregunta(37, '¿Qué animal es conocido por su memoria?', 'León', 'Gato', 'Tigre', 'Elefante')
p38 = Pregunta(38, '¿Qué es el Amazonas?', 'Un desierto', 'Un lago', 'Una sabana', 'Un río')
p39 = Pregunta(39, '¿Cuál es el país de origen de la pizza?', 'Francia', 'España', 'Portugal', 'Italia')
p40 = Pregunta(40, '¿Qué tipo de animal es un delfín?', 'Ave', 'Reptil', 'Anfibio', 'Mamífero')
p41 = Pregunta(41, '¿Cuál es el idioma oficial de Brasil?', 'Español', 'Inglés', 'Francés', 'Portugués')
p42 = Pregunta(42, '¿Qué deporte practica Cristiano Ronaldo?', 'Baloncesto', 'Natación', 'Tenis', 'Fútbol')
p43 = Pregunta(43, '¿En qué país se encuentra el desierto del Sahara?', 'Australia', 'China', 'Argentina', 'África')
p44 = Pregunta(44, '¿Quién pintó "La noche estrellada"?', 'Miguel Ángel', 'Pablo Picasso', 'Leonardo da Vinci', 'Vincent van Gogh')
p45 = Pregunta(45, '¿Cuál es el animal más grande del mundo?', 'Elefante', 'Cocodrilo', 'Rinoceronte', 'Ballena azul')
p46 = Pregunta(46, '¿Qué instrumento mide la temperatura?', 'Barómetro', 'Odómetro', 'Reloj', 'Termómetro')
p47 = Pregunta(47, '¿En qué año comenzó la Segunda Guerra Mundial?', '1936', '1929', '1945', '1939')
p48 = Pregunta(48, '¿Qué gas respiran las plantas?', 'Nitrógeno', 'Ozono', 'Oxígeno', 'Dióxido de carbono')
p49 = Pregunta(49, '¿Cuál es el continente con más habitantes?', 'África', 'Europa', 'América', 'Asia')
p50 = Pregunta(50, '¿Cuál es la ciencia que estudia las estrellas?', 'Geología', 'Ecología', 'Meteorología', 'Astronomía')
p51 = Pregunta(51, '¿Cuál es la capital de Canadá?', 'Toronto', 'Vancouver', 'Montreal', 'Ottawa')
p52 = Pregunta(52, '¿Qué es un tsunami?', 'Un huracán', 'Un deslizamiento de tierra', 'Un incendio', 'Un maremoto')
p53 = Pregunta(53, '¿Qué fruta es conocida por su alto contenido de potasio?', 'Manzana', 'Pera', 'Uva', 'Banana')
p54 = Pregunta(54, '¿Quién descubrió América?', 'Magallanes', 'Colón', 'Marco Polo', 'Cristóbal Colón')
p55 = Pregunta(55, '¿Cuál es el color del semáforo que indica "detenerse"?', 'Verde', 'Amarillo', 'Azul', 'Rojo')
p56 = Pregunta(56, '¿Cuál es el animal símbolo de WWF?', 'León', 'Tigre', 'Elefante', 'Panda')
p57 = Pregunta(57, '¿Qué planeta tiene anillos visibles?', 'Marte', 'Júpiter', 'Venus', 'Saturno')
p58 = Pregunta(58, '¿Qué ciudad es famosa por el carnaval y el Cristo Redentor?', 'Lima', 'Caracas', 'Montevideo', 'Río de Janeiro')
p59 = Pregunta(59, '¿Cuál es el inventor del teléfono?', 'Newton', 'Einstein', 'Edison', 'Bell')
p60 = Pregunta(60, '¿Qué gas necesitamos para respirar?', 'Nitrógeno', 'Helio', 'Metano', 'Oxígeno')

# Crear la lista list_preguntas2 con las nuevas preguntas
list_preguntas2 = [
    (p21.id, p21.preg, p21.rta1, p21.rta2, p21.rta3, p21.rta_c),
    (p22.id, p22.preg, p22.rta1, p22.rta2, p22.rta3, p22.rta_c),
    (p23.id, p23.preg, p23.rta1, p23.rta2, p23.rta3, p23.rta_c),
    (p24.id, p24.preg, p24.rta1, p24.rta2, p24.rta3, p24.rta_c),
    (p25.id, p25.preg, p25.rta1, p25.rta2, p25.rta3, p25.rta_c),
    (p26.id, p26.preg, p26.rta1, p26.rta2, p26.rta3, p26.rta_c),
    (p27.id, p27.preg, p27.rta1, p27.rta2, p27.rta3, p27.rta_c),
    (p28.id, p28.preg, p28.rta1, p28.rta2, p28.rta3, p28.rta_c),
    (p29.id, p29.preg, p29.rta1, p29.rta2, p29.rta3, p29.rta_c),
    (p30.id, p30.preg, p30.rta1, p30.rta2, p30.rta3, p30.rta_c),
    (p31.id, p31.preg, p31.rta1, p31.rta2, p31.rta3, p31.rta_c),
    (p32.id, p32.preg, p32.rta1, p32.rta2, p32.rta3, p32.rta_c),
    (p33.id, p33.preg, p33.rta1, p33.rta2, p33.rta3, p33.rta_c),
    (p34.id, p34.preg, p34.rta1, p34.rta2, p34.rta3, p34.rta_c),
    (p35.id, p35.preg, p35.rta1, p35.rta2, p35.rta3, p35.rta_c),
    (p36.id, p36.preg, p36.rta1, p36.rta2, p36.rta3, p36.rta_c),
    (p37.id, p37.preg, p37.rta1, p37.rta2, p37.rta3, p37.rta_c),
    (p38.id, p38.preg, p38.rta1, p38.rta2, p38.rta3, p38.rta_c),
    (p39.id, p39.preg, p39.rta1, p39.rta2, p39.rta3, p39.rta_c),
    (p40.id, p40.preg, p40.rta1, p40.rta2, p40.rta3, p40.rta_c),
    (p41.id, p41.preg, p41.rta1, p41.rta2, p41.rta3, p41.rta_c),
    (p42.id, p42.preg, p42.rta1, p42.rta2, p42.rta3, p42.rta_c),
    (p43.id, p43.preg, p43.rta1, p43.rta2, p43.rta3, p43.rta_c),
    (p44.id, p44.preg, p44.rta1, p44.rta2, p44.rta3, p44.rta_c),
    (p45.id, p45.preg, p45.rta1, p45.rta2, p45.rta3, p45.rta_c),
    (p46.id, p46.preg, p46.rta1, p46.rta2, p46.rta3, p46.rta_c),
    (p47.id, p47.preg, p47.rta1, p47.rta2, p47.rta3, p47.rta_c),
    (p48.id, p48.preg, p48.rta1, p48.rta2, p48.rta3, p48.rta_c),
    (p49.id, p49.preg, p49.rta1, p49.rta2, p49.rta3, p49.rta_c),
    (p50.id, p50.preg, p50.rta1, p50.rta2, p50.rta3, p50.rta_c),
    (p51.id, p51.preg, p51.rta1, p51.rta2, p51.rta3, p51.rta_c),
    (p52.id, p52.preg, p52.rta1, p52.rta2, p52.rta3, p52.rta_c),
    (p53.id, p53.preg, p53.rta1, p53.rta2, p53.rta3, p53.rta_c),
    (p54.id, p54.preg, p54.rta1, p54.rta2, p54.rta3, p54.rta_c),
    (p55.id, p55.preg, p55.rta1, p55.rta2, p55.rta3, p55.rta_c),
    (p56.id, p56.preg, p56.rta1, p56.rta2, p56.rta3, p56.rta_c),
    (p57.id, p57.preg, p57.rta1, p57.rta2, p57.rta3, p57.rta_c),
    (p58.id, p58.preg, p58.rta1, p58.rta2, p58.rta3, p58.rta_c),
    (p59.id, p59.preg, p59.rta1, p59.rta2, p59.rta3, p59.rta_c),
    (p60.id, p60.preg, p60.rta1, p60.rta2, p60.rta3, p60.rta_c),
]
# c.executemany("INSERT INTO preguntas VALUES (?, ?, ?, ?, ?, ?)", list_preguntas2)

conn.commit()


conn.close()