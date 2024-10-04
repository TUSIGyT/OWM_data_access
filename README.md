# Open Weather Map API

Repositório con script para acceder a los datos meteorológicos usando [Open Weather Map API](https://openweathermap.org/api), a partir de del modulo python [meteostat](https://dev.meteostat.net/python/).

## Usando
Antes de usar el script es importante tener creado un usuario en [Open Weather Map](https://home.openweathermap.org/users/sign_up) y obtener una API Key, a ser [informada como variable de ambiente](#Definiendo-variables-de-ambiente).

### Creando ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Definiendo variables de ambiente
Para acceder a los datos meteorológicos es necesario definir las siguientes variables de ambiente:

* Latitud y Longitud del área que se está buscando información;
* Radio de búsqueda (en metros): Será usado para identificadar a las estaciones meteorológicas al rededor de la coordenada dentro del radio de búsqueda;
* Fecha de inicio y fin de la búsqueda; 

```bash
touch .env
echo OPENWEATHERMAP_API_KEY="your_api_key" > .env
echo LAT=-26.829269 > .env
echo LON=-54.848013 > .env
echo RADIUS=200000 > .env
echo START_DATE="2021-01-01" > .env
echo END_DATE="2021-12-31" > .env
```

### Ejecutando
Accesando el [script.py](script.py), podrás cambiar algunos parámetros como la variable de interés.

```python
VARIABLES = ["tavg", "tmin", "tmax", "prcp", "wspd", "pres", "tsun"]
VARIABLE = VARIABLES[3]
```
En `VARIABLE`, se fine el índice de la variable de interés en la lista `VARIABLES`.

Ejecutando:
```bash
python script.py
```

## Resultado
Un GPKG será creado en la raíz del proyecto con los datos meteorológicos de las estaciones encontradas en el radio de búsqueda.
