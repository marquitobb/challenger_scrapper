# Proyecto de Scraping y Procesamiento de Datos

Este proyecto contiene dos desafíos principales: scraping de productos desde una página web y procesamiento de datos JSON para generar un archivo CSV.



## Requisitos

- Python 3.9 o superior
- Docker (opcional, para ejecutar el servicio FastAPI en un contenedor)

## Instalación

### Challenger One

1. Navega al directorio `challenger_one`:
    ```sh
    cd challenger_one
    ```

2. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

3. Ejecuta el script principal:
    ```sh
    python main.py
    ```

4. Verifica que se haya creado el archivo `products.csv` en el directorio `challenger_one`.

### Challenger Two

1. Navega al directorio `challenger_two`:
    ```sh
    cd challenger_two
    ```

2. Construye la imagen de Docker:
    ```sh
    docker build -t challengetwo .
    ```

3. Ejecuta el contenedor:
    ```sh
    docker run -d -p 8000:8000 --name scraper_container challengetwo
    ```

4. Abre tu navegador y navega a `http://localhost:8000/docs` para ver la documentación interactiva de la API.

### Usando Docker

1. Navega al directorio `challenger_two`:
    ```sh
    cd challenger_two
    ```

2. Construye la imagen de Docker:
    ```sh
    docker build -t scraper-api .
    ```

3. Ejecuta el contenedor:
    ```sh
    docker run -p 8000:8000 scraper-api
    ```

4. Abre tu navegador y navega a `http://localhost:8000` para ver la documentación interactiva de la API.

## Descripción de los Scripts

### Challenger One

- `main.py`: Este script descarga un archivo JSON desde una URL, extrae atributos personalizados y guarda los datos formateados en un archivo CSV.

### Challenger Two

- `filter_selenium.py`: Contiene la clase `JumboScraper` que utiliza Selenium para hacer scraping de productos desde una página web.
- `main.py`: Define un servicio FastAPI con un endpoint para hacer scraping de productos utilizando `JumboScraper`.

## Endpoints de la API

### `GET /`

Devuelve un mensaje de bienvenida.

### `POST /scrape-products/`

Realiza scraping de productos desde una URL proporcionada.

#### Ejemplo de solicitud

```json
{
    "url": "https://www.tiendasjumbo.co/supermercado/despensa/aceite"
}
```
