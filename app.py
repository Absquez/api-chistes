from fastapi import FastAPI
import random

app = FastAPI()

# Lista de chistes
chistes = [
    "¿Por qué la computadora fue al médico? ¡Porque tenía un virus!",
    "¿Qué le dijo un pez a otro pez? ¡Nada!",
    "¿Por qué el libro de matemáticas estaba triste? ¡Porque tenía muchos problemas!",
    "¿Cuál es el café más peligroso del mundo? El ex-preso."
]

@app.get("/chiste")
def obtener_chiste():
    return {"chiste": random.choice(chistes)}
