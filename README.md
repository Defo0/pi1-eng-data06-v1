
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

¡Bienvenidos a mi primer proyecto individual de la etapa de labs! En esta ocasión, voy a estar situandome en el rol de un ***Data Engineer***.  

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

`Application Programming Interface`  es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles que permiten por ejemplo, crear pipelines facilitando mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy voy a estar utilizando **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

## Rol a desarrollar

Como parte del equipo de data de una empresa, el área de análisis de datos me solicitó ciertos requerimientos para el óptimo desarrollo de sus actividades. voy a tener que  *transformar* y disponibilizar los datos mediante la *elaboración y ejecución de una API*.



## **Propuesta de trabajo**

**`Transformaciones`**:  El analista de datos requiere estas, ***y solo estas***, transformaciones para sus datos: (yo hice un par más para trabajar mas cómodo y para corregir un par de errores que fueron surgiendo en el camino, espero no sea eso un problema, Señor Analista)


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:  Para disponibilizar los datos la empresa usé el framework ***FastAPI*** para responder a las siguientes consultas:

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating
<br/>


**`Deployment`**: En este caso el deployement lo voy a realizar con DETA, ya que es muy sencillo de utilizar y tiene todas las herramientas que necesito para poder
cumplir con el trabajo de manera eficiente.
El enlace a donde está alojado el proyecto es https://hohn97.deta.dev/
A modo de ejemplo voy a detallar las siguientes consultas segun lo requerido: 

+ Cantidad de veces que aparece, por ejemplo, la palabra love en el título de peliculas/series, en la plataforma netflix.
        https://hohn97.deta.dev/get_word_count/?keyword=love&platform=netflix

+ Cantidad de películas en amazon con un puntaje mayor a 99 en 2020
        https://hohn97.deta.dev/get_score_count/?platform=amazon&score=99&year=2020

+ La segunda película con mayor score en hulu, según el orden alfabético de los títulos.
        https://hohn97.deta.dev/get_second_score/?platform=hulu

+ Película con mas duración en 2018, en amazon.
        https://hohn97.deta.dev/get_longest/?platform=amazon&duration_type=min&year=2018

+ Cantidad de series y películas catalogadas como +18 entre todas las plataformas.
        https://hohn97.deta.dev/get_rating_count/?rating=18%2B

<br/>

<br/>

**`Video`**: He realizado un video realizando las transformaciones y explicando como realizar las consultas desde la API


https://youtu.be/oSdyokbRH4w



<br/>



<br/>

## **Fuente de datos**

+ Podrán encontrar los archivos con datos en la carpeta Datasets, en este mismo repositorio.<sup>*</sup>
<br/>



## `Disclaimer`
De parte del equipo de Henry se aclara y remarca que el fin de los proyectos propuestos es exclusivamente pedagógico, con el objetivo de realizar simular un entorno laboral, en el cual se trabajan diversas temáticas ajustadas a la realidad. No reflejan necesariamente la filosofía y valores de la organización. Además, Henry no alienta ni tampoco recomienda a los alumnos y/o cualquier persona leyendo los repositorios (y entregas de proyectos) que tomen acciones con base a los datos que pudieran o no haber recabado. Toda la información expuesta y resultados obtenidos en los proyectos nunca deben ser tomados en cuenta para la toma real de decisiones (especialmente en la temática de finanzas, salud, política, etc.).
