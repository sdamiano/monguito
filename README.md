# 🚀 Mi Blog Mongo — Persistencia con Flask y MongoDB

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0%2B-brightgreen.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Este repositorio es un **ejemplo educativo de nivel profesional** diseñado para enseñar conceptos fundamentales de desarrollo web con Python, **Clean Architecture** en Flask y **Persistencia con MongoDB**.

---

## 🎯 Objetivos de Aprendizaje

Al estudiar este repositorio aprenderás:

1. **Clean Architecture & Application Factory**: Cómo estructurar una aplicación Flask escalable utilizando `create_app()` y **Blueprints**.
2. **Twelve-Factor App (Seguridad)**: Gestión centralizada de configuración y credenciales mediante variables de entorno (`python-dotenv` y `.env`).
3. **Modelado NoSQL (Documentos Embebidos)**: Manipulación de estructuras anidadas en MongoDB utilizando el operador `$push` de PyMongo.
4. **Persistencia con MongoDB**: Publicación de artículos de blog y comentarios dinámicos.

---

## 📐 Arquitectura del Proyecto

```text
mi-blog-mongo/
├── .env.example              # Plantilla de variables de entorno (sin credenciales)
├── .gitignore                # Reglas para excluir venv y archivos sensibles
├── requirements.txt          # Dependencias del proyecto con versiones fijas
├── app.py                    # Punto de entrada principal (Entrypoint)
└── app/                      # Paquete principal de la aplicación
    ├── __init__.py           # Application Factory (create_app)
    ├── config.py             # Carga centralizada de variables de entorno
    ├── database.py           # Cliente e instancia de MongoDB
    ├── routes/
    │   ├── __init__.py
    │   └── blog.py           # Blueprint: Rutas del Blog (MongoDB)
    └── templates/
        ├── index.html        # Vista principal del blog y comentarios
        └── edit.html         # Vista para editar artículos existentes
```

---

## ⚡ Guía de Instalación y Ejecución Local (con `venv`)

### 📋 Requisitos Previos

- **Python 3.10** o superior instalado en tu sistema.
- **MongoDB** ejecutándose localmente en el puerto `27017` (o mediante Docker).

---

### 🚀 Paso a Paso

#### 1. Clonar el repositorio
```bash
git clone https://github.com/sdamiano/monguito.git
cd monguito
```

#### 2. Crear y activar el entorno virtual (`venv`)
- **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **En Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

#### 4. Configurar las variables de entorno
Copia la plantilla `.env.example` para crear tu archivo `.env`:
```powershell
Copy-Item .env.example .env
```
Edita el archivo `.env` con tus credenciales locales:
```ini
MONGO_URI=mongodb://127.0.0.1:27017/
MONGO_DB_NAME=blog
```

#### 5. Ejecutar la aplicación
```bash
python app.py
```
Abre tu navegador e ingresa a: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 💡 Conceptos Teóricos Clave Explicados

### 1. Documentos Embebidos en MongoDB (`$push`)

En bases de datos relacionales tradicionales (SQL), los comentarios requerirían una tabla separada `comentarios` con una clave foránea `post_id`. En MongoDB, almacenamos los comentarios directamente dentro del documento del post como un **Array de Documentos Embebidos**:

```python
# Insertar un comentario de forma atómica usando $push en PyMongo
posts_collection.update_one(
    {"_id": ObjectId(post_id)},
    {"$push": {
        "comentarios": {
            "autor": autor,
            "texto": texto,
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
    }}
)
```

---

## 🛠️ Endpoints Disponibles

| Método | Ruta | Descripción | Motor |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Vista principal: Lista artículos y comentarios | MongoDB |
| `POST` | `/add` | Crea un nuevo artículo en el blog | MongoDB |
| `GET/POST` | `/edit/<post_id>` | Formulario y actualización de un artículo | MongoDB |
| `POST` | `/delete/<post_id>` | Elimina un artículo por su `ObjectId` | MongoDB |
| `POST` | `/comment/<post_id>` | Agrega un comentario embebido al artículo | MongoDB |

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

Desarrollado con ❤️ para la comunidad de desarrolladores de Python y NoSQL.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0%2B-brightgreen.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Este repositorio es un **ejemplo educativo de nivel profesional** diseñado para enseñar conceptos fundamentales de desarrollo web con Python, **Clean Architecture** en Flask y **Persistencia Políglota** (*Polyglot Persistence*) combinando **MongoDB**.

---

## 🎯 Objetivos de Aprendizaje

Al estudiar este repositorio aprenderás:

1. **Clean Architecture & Application Factory**: Cómo estructurar una aplicación Flask escalable utilizando `create_app()` y **Blueprints** en lugar de scripts monolíticos.
2. **Twelve-Factor App (Seguridad)**: Gestión centralizada de configuración y credenciales mediante variables de entorno (`python-dotenv` y `.env`).
3. **Modelado NoSQL (Documentos Embebidos)**: Manipulación de estructuras anidadas en MongoDB utilizando el operador `$push` de PyMongo en lugar de JOINs relacionales.
4. **Persistencia Políglota**: Integración de dos motores NoSQL distintos para casos de uso específicos:
   - **MongoDB**: Publicación de artículos de blog y comentarios dinámicos.
  
---

## 📐 Arquitectura del Proyecto

```text
mi-blog-mongo/
├── .env.example              # Plantilla de variables de entorno (sin credenciales)
├── .gitignore                # Reglas para excluir venv y archivos sensibles
├── requirements.txt          # Dependencias del proyecto con versiones fijas
├── app.py                    # Punto de entrada principal (Entrypoint)
└── app/                      # Paquete principal de la aplicación
    ├── __init__.py           # Application Factory (create_app)
    ├── config.py             # Carga centralizada de variables de entorno
    ├── database.py           # Clientes e instancias de Mongo
    ├── routes/
    │   ├── __init__.py
    │   ├── blog.py           # Blueprint: Rutas del Blog (MongoDB)
    │  
    └── templates/
        ├── index.html        # Vista principal del blog y comentarios
        └── edit.html         # Vista para editar artículos existentes
```

---

## ⚡ Guía de Instalación y Ejecución Local (con `venv`)

### 📋 Requisitos Previos

- **Python 3.10** o superior instalado en tu sistema.
- **MongoDB** ejecutándose localmente en el puerto `27017` (o mediante Docker).

---

### 🚀 Paso a Paso

#### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/mi-blog-mongo.git
cd mi-blog-mongo
```

#### 2. Crear y activar el entorno virtual (`venv`)

- **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

- **En Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

#### 4. Configurar las variables de entorno
Copia la plantilla `.env.example` para crear tu archivo `.env`:

- **En Windows (PowerShell):**
  ```powershell
  Copy-Item .env.example .env
  ```
- **En Linux / macOS:**
  ```bash
  cp .env.example .env
  ```

Edita el archivo `.env` según tus credenciales locales:
```ini
MONGO_URI=mongodb://127.0.0.1:27017/
MONGO_DB_NAME=blog

```

#### 5. Ejecutar la aplicación
```bash
python app.py
```

Abre tu navegador e ingresa a: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 💡 Conceptos Teóricos Clave Explicados

### 1. Documentos Embebidos en MongoDB (`$push`)

En bases de datos relacionales tradicionales (SQL), los comentarios requerirían una tabla separada `comentarios` con una clave foránea `post_id`. En MongoDB, almacenamos los comentarios directamente dentro del documento del post como un **Array de Documentos Embebidos**:

```python
# Insertar un comentario de forma atómica usando $push en PyMongo
posts_collection.update_one(
    {"_id": ObjectId(post_id)},
    {"$push": {
        "comentarios": {
            "autor": autor,
            "texto": texto,
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
    }}
)
```

## 🛠️ Endpoints Disponibles

| Método | Ruta | Descripción | Motor |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Vista principal: Lista artículos y comentarios | MongoDB |
| `POST` | `/add` | Crea un nuevo artículo en el blog | MongoDB |
| `GET/POST` | `/edit/<post_id>` | Formulario y actualización de un artículo | MongoDB |
| `POST` | `/delete/<post_id>` | Elimina un artículo por su `ObjectId` | MongoDB |
| `POST` | `/comment/<post_id>` | Agrega un comentario embebido al artículo | MongoDB |

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

Desarrollado con ❤️ para la comunidad de desarrolladores de Python y NoSQL.
