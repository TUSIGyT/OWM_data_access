import logging
from meteostat import Stations, Monthly
from geopandas import GeoDataFrame, points_from_xy
import pandas as pd
from decouple import config
from datetime import datetime

OWM_KEY = config("OPENWEATHER_KEY")
LAT = config("LAT", cast=float)
LON = config("LON", cast=float)
RADIUS = config("RADIUS", cast=int)
START_DATE = datetime.strptime(config("START_DATE"), "%Y-%m-%d")
END_DATE = datetime.strptime(config("END_DATE"), "%Y-%m-%d")
VARIABLES = ["tavg", "tmin", "tmax", "prcp", "wspd", "pres", "tsun"]
VARIABLE = VARIABLES[3]

# Acceso a las estaciones meteorológicas
station = Stations()
# Identificando aquellas más cercanas, acorde un radio de búsqueda
station = station.nearby(LAT, LON, RADIUS)
station = station.fetch()
# transforma en DataFrame
station = pd.DataFrame(station)
# Convertiendo a GeoDataFrame
station = GeoDataFrame(
    station, geometry=points_from_xy(station["longitude"], station["latitude"])
)

weather_data = pd.DataFrame()
for i in station.index:
    # i = station.index[1]
    data = Monthly(i, START_DATE, END_DATE)
    # confirma si el dato esta completo
    coverage = data.coverage()
    if not coverage:
        logging.warning(
            f"Datos no están completos. Ocupando función <normalize> para rellenar ausencia de datos."
        )
        data = data.normalize()
    data = data.fetch()
    data = data.reset_index()
    data.time = data.time.dt.strftime("%b")
    data = data.set_index("time")
    data = pd.DataFrame(data)[VARIABLE].to_frame().T
    data["id"] = i
    data = data.set_index("id")

    weather_data = pd.concat([weather_data, data])

station = station.join(weather_data)
station.to_file("./stations.gpkg", layer="stations", driver="GPKG")
