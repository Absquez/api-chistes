from fastapi import FastAPI
import random

app = FastAPI()

# Lista de chistes
chistes = [
    "¿Por qué la computadora fue al médico? ¡Porque tenía un virus!",
    "¿Qué le dijo un pez a otro pez? ¡Nada!",
    "¿Por qué el libro de matemáticas estaba triste? ¡Porque tenía muchos problemas!",
    "¿Cuál es el café más peligroso del mundo? El ex-preso."
    "Hola, ¿está Agustín? No, estoy incómodo."
    "Están dos borrachos y uno le dice al otro: 'No sigas bebiendo que te estás poniendo borroso'"
    "¿Por qué las monjas no llevan sandalias? Porque son devotas."
    "¿Qué hace un perro con un taladro? Ta ladrando."
    "¿Qué le dice un techo a otro? «Techo de menos»."
    "¿Cuál es el animal que libera al mono? El salmonete."
    "¿Por qué los patos no tienen amigos? Porque son muy antipáticos"
]

@app.get("/chiste")
def obtener_chiste():
    return {"chiste": random.choice(chistes)}
