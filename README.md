# Proyecto Flask

Este proyecto es una aplicación web construida con Flask. A continuación se detallan los pasos para configurar y ejecutar el proyecto.

## Requisitos

Asegúrate de tener `python` y `pip` instalados en tu sistema.

## Configuración del Entorno

1. **Clona el repositorio** (si aún no lo has hecho):

    ```bash
    git clone <url-del-repositorio>
    cd <nombre-del-repositorio>
    ```

2. **Crea y activa un entorno virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar la Aplicación

1. **Inicia el servidor de desarrollo**:

    ```bash
    flask --app main run
    ```

2. **Abre tu navegador** y dirígete a `http://127.0.0.1:5000` para ver la aplicación en acción.

## Generar el archivo `requirements.txt`

Si necesitas actualizar o generar el archivo `requirements.txt` con las dependencias actuales, usa:

```bash
pip freeze > requirements.txt

