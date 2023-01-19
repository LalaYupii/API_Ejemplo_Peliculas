
'''AQUI DEFINIMOS LOS TIPOS DE DATOS CON LOS QUE VAMOS A TRABAJAR PARA VALIDACIONES'''

#Librerias 
from pydantic import BaseModel
from typing import Optional, Text

class Movies (BaseModel):
    id: Optional[str] = 'Sin Definir'
    tipo: Optional[str] = 'Sin Definir'
    titulo: Optional[str] = 'Sin Definir'
    pais: Optional[str] = 'Sin Definir'
    estreno: Optional[int] = -1
    descripcion: Optional[Text] = 'Sin Definir'
    score: Optional[int] = -1
    plataforma: str
    
class Cantidad_Peliculas (BaseModel):
    cantidad: int