
'''AQUI SE DEFINEN LAS RUTAS RELACIONADAS CON LAS PELICULAS... PODEMOS TENER VARIAS :)'''


#Librerias necesarias
import pandas as pd
from fastapi import APIRouter, HTTPException
from typing import List, Union
#importamos el esquema/estructura para poder trabajar con los datos
from schemas.movies import Movies, Cantidad_Peliculas


'''
--------- IDEAS PARA CONSULTAS :D --------- 
1) Todas las pelis indistintamente la plataforma
2) Peliculas por plataforma
3) Peliculas que superen el promedio del score
4) peliculas por plataforma, estreno, pais
5) Cantidad de peliculas por plataforma
'''


#Cargamos los csv
df_amazon = pd.read_csv(r'Datasets/amazon_movies.csv', 
        usecols= ['show_id', 'type', 'title', 'country', 'release_year', 'description', 'score'])
df_amazon.columns= ['id', 'tipo', 'titulo', 'pais', 'estreno', 'descripcion', 'score']
df_amazon['plataforma'] = 'Amazon'
df_amazon['id'].fillna('Sin Definir', inplace=True)
df_amazon['tipo'].fillna('Sin Definir', inplace=True)
df_amazon['titulo'].fillna('Sin Definir', inplace=True)
df_amazon['pais'].fillna('Sin Definir', inplace=True)
df_amazon['pais'] = df_amazon['pais'].apply(lambda x: str(x).lower())
df_amazon['estreno'].fillna(-1, inplace=True)
df_amazon['descripcion'].fillna('Sin Definir', inplace=True)
df_amazon['score'].fillna(-1, inplace=True)

df_disney = pd.read_csv(r'Datasets/disney_plus_movies.csv', 
        usecols= ['show_id', 'type', 'title', 'country', 'release_year', 'description', 'score'])
df_disney.columns= ['id', 'tipo', 'titulo', 'pais', 'estreno', 'descripcion', 'score']
df_disney['plataforma'] = 'Disney'
df_disney['id'].fillna('Sin Definir', inplace=True)
df_disney['tipo'].fillna('Sin Definir', inplace=True)
df_disney['titulo'].fillna('Sin Definir', inplace=True)
df_disney['pais'].fillna('Sin Definir', inplace=True)
df_disney['pais'] = df_disney['pais'].apply(lambda x: str(x).lower())
df_disney['estreno'].fillna(-1, inplace=True)
df_disney['descripcion'].fillna('Sin Definir', inplace=True)
df_disney['score'].fillna(-1, inplace=True)

df_hulu = pd.read_csv(r'Datasets/hulu_movies.csv', 
        usecols= ['show_id', 'type', 'title', 'country', 'release_year', 'description', 'score'])
df_hulu.columns= ['id', 'tipo', 'titulo', 'pais', 'estreno', 'descripcion', 'score']
df_hulu['plataforma'] = 'Hulu'
df_hulu['id'].fillna('Sin Definir', inplace=True)
df_hulu['tipo'].fillna('Sin Definir', inplace=True)
df_hulu['titulo'].fillna('Sin Definir', inplace=True)
df_hulu['pais'].fillna('Sin Definir', inplace=True)
df_hulu['pais'] = df_hulu['pais'].apply(lambda x: str(x).lower())
df_hulu['estreno'].fillna(-1, inplace=True)
df_hulu['descripcion'].fillna('Sin Definir', inplace=True)
df_hulu['score'].fillna(-1, inplace=True)

df_netflix = pd.read_csv(r'Datasets/netflix_movies.csv', 
        usecols= ['show_id', 'type', 'title', 'country', 'release_year', 'description', 'score'])
df_netflix.columns= ['id', 'tipo', 'titulo', 'pais', 'estreno', 'descripcion', 'score']
df_netflix['plataforma'] = 'Netflix'
df_netflix['id'].fillna('Sin Definir', inplace=True)
df_netflix['tipo'].fillna('Sin Definir', inplace=True)
df_netflix['titulo'].fillna('Sin Definir', inplace=True)
df_netflix['pais'].fillna('Sin Definir', inplace=True)
df_netflix['pais'] = df_netflix['pais'].apply(lambda x: str(x).lower())
df_netflix['estreno'].fillna(-1, inplace=True)
df_netflix['descripcion'].fillna('Sin Definir', inplace=True)
df_netflix['score'].fillna(-1, inplace=True)


#Intanciamos el objeto que guardará las rutas
movies = APIRouter()

#Bienvenida ruta inicial
@movies.get('/', tags=['Bienvenida'])
async def bienvenida():
    return 'Bienvenid@ a nuestra API para más información vaya a la documentación'


#Obtenemos todas las peliculas
@movies.get('/peliculas', tags=['Peliculas'], response_model=List[Movies], description='Obtenemos todas las peliculas (se que no todo son peliculas xD)')
async def peliculas_todas():
    peliculas = pd.concat([df_amazon, df_disney, df_hulu, df_netflix], axis=0)
    lista_pelis = []
    peliculas = peliculas.tail(30)
    for elemento in peliculas.values:
        diccionario ={}
        diccionario['id'] = elemento[0]
        diccionario['plataforma'] = elemento[7]
        diccionario['tipo'] = elemento[1]
        diccionario['titulo'] = elemento[2]
        diccionario['pais'] = elemento[3]
        diccionario['estreno'] = elemento[4]
        diccionario['descripcion'] = elemento[5]
        diccionario['score'] = elemento[6]
        lista_pelis.append(diccionario)
    
    #lista_pelis = [] #para probar jajaja 

    if (len(lista_pelis) == 0): 
        raise HTTPException(status_code=404, detail="No se encontraron peliculas")
    else:
        return lista_pelis

#Obtenemos todas las peliculas por plataforma
@movies.get('/peliculas/{plataforma}', tags=['Peliculas'], response_model=List[Movies], description='Obtenemos todas las peliculas por plataforma (Amazon, Disney, Hulu, Netflix)')
async def peliculas_por_plataforma(plataforma:str):

    #Amazon
    if (plataforma.lower() == 'amazon'):
        lista_pelis = []
        peliculas = df_amazon.tail(50)
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)
        
        #lista_pelis = [] #para probar jajaja 

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma {plataforma}')
        else:
            return lista_pelis
    
    #Disney 
    elif (plataforma.lower() == 'disney'):
        lista_pelis = []
        peliculas = df_disney.tail(50)
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)
        
        #lista_pelis = [] #para probar jajaja 

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma {plataforma}')
        else:
            return lista_pelis
    
    #Hulu
    elif (plataforma.lower() == 'hulu'):
        lista_pelis = []
        peliculas = df_hulu.tail(50)
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)
        
        #lista_pelis = [] #para probar jajaja 

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma {plataforma}')
        else:
            return lista_pelis
    
    #Netflix
    elif (plataforma.lower() == 'netflix'):
        lista_pelis = []
        peliculas = df_netflix.tail(50)
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)
        
        #lista_pelis = [] #para probar jajaja 

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma {plataforma}')
        else:
            return lista_pelis
    else:
        raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma {plataforma}')


#Obtenemos cantidad de peliculas por plataformas o todas
@movies.get('/cantidad_peliculas', tags=['Peliculas'], response_model=Cantidad_Peliculas, description='Obtenemos la cantidad total de peliculas')
async def peliculas_cantidad(plataforma:Union[str, None]='Todas'):
    
    #Todas
    if (plataforma.lower() == 'todas'):        
        peliculas = pd.concat([df_amazon, df_disney, df_hulu, df_netflix], axis=0)
        cantidad = peliculas.shape[0]

        if (cantidad == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas')
        else:
            dict_cantidad = {'cantidad': cantidad}
            return dict_cantidad 

    #Amazon
    elif (plataforma.lower() == 'amazon'):
        cantidad = df_amazon.shape[0]

        if (cantidad == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma de {plataforma}')
        else:
            dict_cantidad = {'cantidad': cantidad}
            return dict_cantidad 
              
    
    #Disney 
    elif (plataforma.lower() == 'disney'):

        cantidad = df_disney.shape[0]

        if (cantidad == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma de {plataforma}')
        else:
            dict_cantidad = {'cantidad': cantidad}
            return dict_cantidad  
    
    #Hulu
    elif (plataforma.lower() == 'hulu'):
        cantidad = df_hulu.shape[0]

        if (cantidad == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma de {plataforma}')
        else:
            dict_cantidad = {'cantidad': cantidad}
            return dict_cantidad 
      
    
    #Netflix
    elif (plataforma.lower() == 'netflix'):
        cantidad = df_netflix.shape[0]
        if (cantidad == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma de {plataforma}')
        else:
            dict_cantidad = {'cantidad': cantidad}
            return dict_cantidad 
    else:
        raise HTTPException(status_code=404, detail=f'No se encontraron peliculas en la plataforma de {plataforma}')


#Obtenemos todas las peliculas que superen el score
@movies.get('/peliculas_score', tags=['Peliculas'], response_model=List[Movies], description='Obtenemos todas las peliculas que superen el promedio del score')
async def peliculas_mayor_score():
    peliculas = pd.concat([df_amazon, df_disney, df_hulu, df_netflix], axis=0)
    lista_pelis = []
    peliculas = peliculas[peliculas['score'] > round(peliculas['score'].mean(), 2)]
    print(round(peliculas['score'].mean(), 2))
    peliculas = peliculas.head(50)
    for elemento in peliculas.values:
        diccionario ={}
        diccionario['id'] = elemento[0]
        diccionario['plataforma'] = elemento[7]
        diccionario['tipo'] = elemento[1]
        diccionario['titulo'] = elemento[2]
        diccionario['pais'] = elemento[3]
        diccionario['estreno'] = elemento[4]
        diccionario['descripcion'] = elemento[5]
        diccionario['score'] = elemento[6]
        lista_pelis.append(diccionario)   

    if (len(lista_pelis) == 0): 
        raise HTTPException(status_code=404, detail="No se encontraron peliculas")
    else:
        return lista_pelis


#Obtenemos peliculas por plataforma, año de estreno y pais
@movies.get('/peliculas_filtro', tags=['Peliculas'], response_model=List[Movies], description='Obtenemos todas las peliculas por plataforma, año de estreno y pais')
async def peliculas_filtro_avanzado(plataforma:Union[str, None]='', estreno:Union[int, None]=2021, pais:Union[str, None]='United States'):
    
    #Todas
    if (plataforma.lower() == ''):
        lista_pelis = []
        peliculas = pd.concat([df_amazon, df_disney, df_hulu, df_netflix], axis=0)
        peliculas = peliculas[(peliculas['estreno']==estreno) & (peliculas['pais']==pais.lower())]
        peliculas = peliculas.head(30)
        print(pais.lower())
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas')
        else:
            return lista_pelis


    #Amazon
    if (plataforma.lower() == 'amazon'):
        lista_pelis = []
        peliculas = df_amazon[(df_amazon['estreno']==estreno) & (df_amazon['pais']==pais)]
        peliculas = peliculas.head(30)
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)
        
        #lista_pelis = [] #para probar jajaja 

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas')
        else:
            return lista_pelis
    
    #Disney 
    elif (plataforma.lower() == 'disney'):
        lista_pelis = []
        peliculas = df_disney[(df_disney['estreno']==estreno) & (df_disney['pais']==pais)]
        peliculas = peliculas.head(30)
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)
        
        #lista_pelis = [] #para probar jajaja 

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas')
        else:
            return lista_pelis
    
    #Hulu
    elif (plataforma.lower() == 'hulu'):
        lista_pelis = []
        peliculas = df_hulu[(df_hulu['estreno']==estreno) & (df_hulu['pais']==pais)]
        peliculas = peliculas.head(30)
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)
        
        #lista_pelis = [] #para probar jajaja 

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas')
        else:
            return lista_pelis
    
    #Netflix
    elif (plataforma.lower() == 'netflix'):
        lista_pelis = []
        peliculas = df_netflix[(df_netflix['estreno']==estreno) & (df_netflix['pais']==pais)]
        peliculas = peliculas.head(30)
        for elemento in peliculas.values:
            diccionario ={}
            diccionario['id'] = elemento[0]
            diccionario['plataforma'] = elemento[7]
            diccionario['tipo'] = elemento[1]
            diccionario['titulo'] = elemento[2]
            diccionario['pais'] = elemento[3]
            diccionario['estreno'] = elemento[4]
            diccionario['descripcion'] = elemento[5]
            diccionario['score'] = elemento[6]
            lista_pelis.append(diccionario)
        
        #lista_pelis = [] #para probar jajaja 

        if (len(lista_pelis) == 0): 
            raise HTTPException(status_code=404, detail=f'No se encontraron peliculas')
        else:
            return lista_pelis
    else:
        raise HTTPException(status_code=404, detail=f'No se encontraron peliculas')





#3) Peliculas que superen el promedio del score
# 5) Cantidad de peliculas por plataforma