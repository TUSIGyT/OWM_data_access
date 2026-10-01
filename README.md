# Open Weather Map API

Repositório con script para acceder a datos meteorológicos mensuales a partir del modulo python [meteostat](https://dev.meteostat.net/python/). No es necesario tener cuenta ni API Key de Open Weather Map.

## Usando

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
cat > .env <<EOF
LAT=-26.829269
LON=-54.848013
RADIUS=200000
START_DATE=2021-01-01
END_DATE=2021-12-31
EOF
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
Un GPKG será creado en la raíz del proyecto con los datos meteorológicos de las estaciones encontradas en el radio de búsqueda. Cada mes del período es una columna nombrada `AAAA-MM` (por ejemplo, `2021-01`).

## América del Sur
El script [south_america.py](south_america.py) descarga la temperatura media mensual (`tavg`) de 2021 para todas las estaciones de Meteostat en América del Sur. No usa el `.env`: los países, el período y la variable están definidos al inicio del script.

```bash
python south_america.py
```

Genera `south_america.gpkg` (capa `tavg_2021`) con unas 420 estaciones y una columna por mes (`2021-01` … `2021-12`). Los meses sin dato quedan vacíos. La descarga tarda unos minutos.

Se usa 2021 porque Meteostat no tiene datos mensuales de América del Sur posteriores a 2022, y 2021 es el año con más estaciones. Incluye estaciones insulares, como Isla de Pascua (Chile) y Fernando de Noronha (Brasil).
