from fastapi import FastAPI, Query
import random

app = FastAPI(title="AnMeCa", description="API de chistes buenos y malos con búsqueda", version="2.0")

# ----------------------------
# 1. Datos: 20 chistes buenos y 20 malos
# ----------------------------

chistes_buenos = [
    "¿Por qué la computadora fue al médico? Porque tenía un virus.",
    "¿Qué le dijo un 0 a un 8? Bonito cinturón.",
    "¿Por qué los programadores prefieren el invierno? Porque hay menos bugs.",
    "¿Por qué el libro de matemáticas estaba triste? Porque tenía muchos problemas.",
    "¿Por qué la impresora estaba molesta? Porque siempre la dejaban en espera.",
    "¿Por qué la red se cayó? Porque se cansó de tanto tráfico.",
    "¿Qué hace una abeja en el gimnasio? Zumba.",
    "¿Por qué el café se fue al psiquiatra? Porque estaba molido.",
    "¿Cuál es el colmo de un programador? Que su hijo se llame Java y su perro Python.",
    "¿Por qué los peces nunca usan Facebook? Porque ya están en la red.",
    "¿Qué le dijo el teclado a la computadora? ¡No me toques las teclas!",
    "¿Por qué la calculadora se deprimió? Porque siempre la usaban para resolver problemas.",
    "¿Qué hace una vaca con los ojos cerrados? Leche concentrada.",
    "¿Por qué el sol nunca fue a la universidad? Porque ya tenía demasiados rayos.",
    "¿Por qué los pájaros no usan WhatsApp? Porque ya tienen Twitter.",
    "¿Cuál es el café más peligroso del mundo? El ex-preso.",
    "¿Por qué la bicicleta no podía mantenerse en pie? Porque estaba dos-tirada.",
    "¿Por qué las plantas odian las matemáticas? Porque les dan raíces cuadradas.",
    "¿Por qué el programador confundió Halloween con Navidad? Porque OCT 31 = DEC 25.",
    "¿Por qué la escoba llegó tarde? Porque se barrió."
]

chistes_malos = [
    "¿Por qué el pollo cruzó la carretera? Para llegar al otro lado.",
    "¿Qué le dice una impresora a otra? ¿Esa hoja es tuya o es impresión mía?",
    "¿Por qué los pájaros no usan el metro? Porque prefieren volar.",
    "¿Qué le dice una cebolla a otra? No mires, me estoy desnudando.",
    "¿Por qué la luna fue al gimnasio? Para ponerse en cuarto creciente.",
    "¿Por qué el semáforo nunca peleaba? Porque siempre estaba en rojo.",
    "¿Qué hace un pez en el cine? Nada.",
    "¿Por qué el pan fue al médico? Porque estaba crudo.",
    "¿Qué le dijo una pared a otra pared? Nos vemos en la esquina.",
    "¿Por qué la escoba estaba cansada? Porque había barrido mucho.",
    "¿Qué hace una abeja en el gimnasio? Zumba (otra vez, pero peor).",
    "¿Por qué el reloj fue al médico? Porque se le paró el corazón.",
    "¿Por qué la vaca fue al espacio? Para ver la Vía Láctea.",
    "¿Por qué el tomate se sonrojó? Porque vio al pepino desnudo.",
    "¿Por qué el lápiz se deprimió? Porque siempre lo usaban para borrar.",
    "¿Por qué el perro ladró a la computadora? Porque tenía un mouse.",
    "¿Qué hace una taza en la universidad? Toma clases.",
    "¿Por qué el cinturón fue arrestado? Por sostener los pantalones.",
    "¿Por qué el libro de historia estaba aburrido? Porque siempre se repetía.",
    "¿Por qué el zapato fue al médico? Porque tenía suela rota."
]

# ----------------------------
# 2. Endpoint raíz
# ----------------------------

@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a la API de chistes AnMeCa",
        "endpoints": ["/chistes", "/chiste-random"]
    }

# ----------------------------
# 3. Endpoint chistes (lista y búsqueda)
# ----------------------------

@app.get("/chistes")
def obtener_chistes(
    categoria: str = Query(None, description="bueno o malo"),
    buscar: str = Query(None, description="texto a buscar en los chistes")
):
    # Seleccionar la lista según categoría
    if categoria == "bueno":
        lista = chistes_buenos
    elif categoria == "malo":
        lista = chistes_malos
    else:
        lista = chistes_buenos + chistes_malos

    # Filtrar por búsqueda
    if buscar:
        lista = [c for c in lista if buscar.lower() in c.lower()]

    if not lista:
        return {"mensaje": "No se encontraron chistes con esos parámetros."}

    return {"chistes": lista, "total": len(lista)}

# ----------------------------
# 4. Endpoint chiste aleatorio
# ----------------------------

@app.get("/chiste-random")
def chiste_random(categoria: str = None):
    if categoria == "bueno":
        return {"chiste": random.choice(chistes_buenos)}
    elif categoria == "malo":
        return {"chiste": random.choice(chistes_malos)}
    else:
        return {"chiste": random.choice(chistes_buenos + chistes_malos)}
