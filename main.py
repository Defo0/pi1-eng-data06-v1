from fastapi import FastAPI
import pandas as pd 
import numpy as np

app= FastAPI() 

df=pd.read_csv("Datasets/final_df.csv") 


#configuramos un pequeño index para que no quede vacio
@app.get("/")
async def index():
    return "Hola! esto es un indice, para mas indormacion ir a /docs"
    


#consigna número 1:  Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

@app.get("/get_word_count/")
async def get_word_count(keyword: str, platform:str=None):
    if platform:
        df1 = df[df['platform'] == platform]
        count = df1['title'].str.count(keyword).sum()
        return f"La palabra {keyword} se repite {count} veces en la plataforma {platform}"
    else:
        count = df['title'].str.count(keyword).sum()
        return f"La palabra {keyword} se repite {count} veces en todas las plataformas"

"""
El código anterior usa el método str.count() de las columnas del dataframe
para contar la cantidad de veces que aparece una palabra clave en los títulos.
La funcion nos pide como parametro un string para la 'keyword'y opcionalmente un string para la plataforma.
"""        


#consigna número 2 Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

@app.get("/get_score_count/")
async def get_score_count(platform:str, score:int, year:int):

    filtered_df = df[(df['score'] > score) & (df['release_year'] == year) & (df['platform'] == platform)]
    if filtered_df.shape[0] == 0:
        return f"No hay peliculas en la plataforma {platform} con un puntaje de {score} en el año {year}."
    grouped_df = filtered_df.groupby('platform')
    result = grouped_df.size().reset_index(name='count')
    message = f"La cantidad de peliculas en {platform} con un puntaje de {score} en el año {year} fue de {result['count'].iloc[0]}"
    return message


"""
El código anterior se encarga de contar cuantas peliculas hay en una plataforma
 específica con un puntaje mayor a un valor específico y en un año específico.

Primero se filtra el dataframe para obtener solo las filas
que cumplen con los criterios especificados
Si no hay filas que cumplan con esos criterios
se devuelve un mensaje indicando que no hay películas
en la plataforma con ese puntaje en ese año.
En caso contrario, se agrupan las filas resultantes 
por plataforma y se cuenta la cantidad de películas en cada plataforma.
La funcion nos pide como parametro un string para definir la plataforma, un numero entero para el score
y un numero entero para el año de lanzamiento de la pelicula
"""

#Consigna número 3 La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

@app.get("/get_second_score/")
async def get_second_score(platform:str):
       
    filtered_df = df[(df['platform'] == platform) & (df['type'] == 'movie')]
    sorted_df = filtered_df.sort_values(by=['score','title'],ascending=[False,True])
    result = sorted_df.iloc[1]
    message = f"La segunda película con mayor puntaje para la plataforma {platform} es {result['title']} con un puntaje de {result['score']} "
    return message


"""
El código anterior se encarga de encontrar la segunda película con el puntaje más alto en una plataforma específica.

Primero, se filtran las filas del dataframe para obtener solo las películas en la plataforma específica.
Luego, se ordenan las filas resultantes por puntaje y título.
Finalmente, se selecciona la segunda fila (índice 1) y se devuelve un mensaje con el título y el puntaje de esa película.
"""

#consigna número 4 Película que más duró según año, plataforma y tipo de duración

@app.get("/get_longest/")
async def get_longest(platform:str, duration_type:str, year:int):
   
    filtered_df = df[(df['release_year'] == year) & (df['platform'] == platform) & (df['duration_type'] == duration_type)]
    max_index = filtered_df['duration_int'].idxmax()
    title = df.loc[max_index, 'title']
    duration = df.loc[max_index, 'duration_int']
    type_ = df.loc[max_index, 'type']
    if type_ == "movie":
        type_text = "La película"
    else:
        type_text = "La serie"
    message = f"{type_text} que más duró en el año {year} en la plataforma {platform} con tipo de duración {duration_type} fue de {title} con una duracion de {duration} {duration_type}"
    return message

"""
El código anterior se encarga de encontrar la película o serie con la duración máxima en una plataforma específica,
en un año específico y con un tipo de duración específico.
Primero, se filtran las filas del dataframe para obtener solo las películas o series que cumplen con los criterios
especificados: en una plataforma específica, en un año específico y con un tipo de duración específico.
Luego se busca el indice de la fila con la duración máxima, se extraen el título,
la duración y el tipo de la película o serie de esa fila y se devuelve un mensaje con esa información.
"""

#consigna número 5 Cantidad de series y películas por rating


@app.get("/get_rating_count/")
async def get_rating_count(rating:str):
    
    grouped_df = df.groupby(['rating', 'type']).size().reset_index(name='count')
    filtered_df = grouped_df[grouped_df['rating'] == rating]
    if filtered_df.empty:
        return f"No hay series o peliculas con el rating {rating}."
    else:
        total = filtered_df['count'].sum()
        return f"El total de series y peliculas con rating {rating} es de {total}."

"""
El codigo anterior se encarga de contar la cantidad de películas y series con un rating específico.

Primero, se agrupa el dataframe por rating y tipo, y se cuenta el número de películas
y series con cada combinación de rating y tipo. Luego se filtran las filas con el
rating específico y se suma el total de películas y series con ese rating.

En caso de no haber películas o series con ese rating,
se devuelve un mensaje indicando que no hay ninguna con ese rating,
de lo contrario, se devuelve el total de películas y series con ese rating.
"""
