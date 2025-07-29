# API de Chistes con FastAPI, Render y ToolJet

Este proyecto es una API sencilla que devuelve chistes aleatorios en formato JSON.  
Fue creada usando **FastAPI**, desplegada en **Render** y conectada a una app visual en **ToolJet**.

---

## 1. Requisitos

- Python 3.13.5
- Git
- Cuenta en GitHub
- Cuenta en Render
- Cuenta en ToolJet

---

## 2. Estructura del proyecto

```
api-chistes/
├── app.py
├── requirements.txt
├── Procfile
└── .gitignore
```

### app.py
```python
from fastapi import FastAPI
import random

app = FastAPI()

chistes = [
    "¿Por qué la computadora fue al médico? Porque tenía un virus.",
    "¿Qué le dijo un 0 a un 8? Bonito cinturón.",
    "¿Por qué los programadores prefieren el invierno? Porque hay menos bugs."
]

@app.get("/chiste")
def obtener_chiste():
    return {"chiste": random.choice(chistes)}
```

### requirements.txt
```
fastapi
uvicorn
```

### Procfile
```
web: uvicorn app:app --host 0.0.0.0 --port 10000
```

### .gitignore
```
venv/
__pycache__/
```

---

## 3. Subir a GitHub

1. Crear un repositorio en [GitHub](https://github.com/new)  
2. Desde la carpeta del proyecto ejecutar:

```bash
git init
git add .
git commit -m "Subir API de chistes"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/api-chistes.git
git push -u origin main
```

---

## 4. Desplegar en Render

1. Crear cuenta en [Render](https://render.com)  
2. Crear **New Web Service** → conectar con GitHub  
3. Seleccionar el repo `api-chistes`  
4. Render detecta automáticamente `requirements.txt`  
5. **Build Command**: dejar vacío o `pip install -r requirements.txt`  
6. **Start Command**: dejar vacío (Render usa `Procfile`)  
7. Hacer Deploy y copiar la URL pública

Ejemplo:  
```
https://api-chistes.onrender.com/chiste
```

---

## 5. Conectar en ToolJet

### Crear app
1. Ingresar a [ToolJet](https://tooljet.com)  
2. Crear **Nueva App → Blan**

### Conectar API
1. En **Data Sources** → **Add new data source**  
2. Elegir **REST API**  
3. Poner como Base URL:
```
https://api-chistes.onrender.com
```
4. Guardar

### Crear Query
1. Ir a **Queries / Actions → Add query**  
2. Seleccionar `ChistesAPI`  
3. Método: GET  
4. Endpoint: `/chiste`  
5. Probar con **Run**

### Mostrar en interfaz
- Arrastrar un **Text Widget**
- En propiedad Text escribir:
```
{{queries.query1.data.chiste}}
```
*(Reemplazar `query1` con el nombre real de la query)*

### Botón para refrescar
- Arrastrar un **Button**
- Configurar acción **Run query** para la query de chistes

---

## 6. Resultado

Una API de chistes funcionando en Render y conectada a ToolJet para mostrar datos en una interfaz visual.

---

## 7. Recursos

- [FastAPI](https://fastapi.tiangolo.com/)  
- [Render](https://render.com/docs)  
- [ToolJet](https://docs.tooljet.com)  
