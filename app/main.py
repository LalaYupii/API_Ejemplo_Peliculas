
#Hacemos las importaciones necesarias
from fastapi import FastAPI
from routes.movies import movies

#Creamos el ejecutable
app = FastAPI(
    title='Ejemplo de uso FastAPI',
    description='Explicación sencilla de uso aunque todos ya lo tienen controlado :D',
    version='0.0.5'
)


#Diferenciar: get, post, put, delete, async por uvicorn que es un servidor asincrono asi que por eso se recomienda
#muy importante lo del modo asincrono cuando se recibe muchas peticiones

#Agregamos las rutas a nuestro archivo principal asi trabajamos de manera modular
app.include_router(movies)
