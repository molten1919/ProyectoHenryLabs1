from fastapi import FastAPI
import pandas as pd

# se instancia un objeto
app = FastAPI()

# endpoint 0
# @app.get("/")
# def read_root():
  #  return {"Prueba": "de deploy en local"}

# endpoint 1
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Comienza el proyecto

# cargamos los datos desde el repositorio en github

df_concatenado = pd.read_csv('https://github.com/molten1919/ProyectoHenryLabs1/blob/main/df_concatenado.csv')
keyword = ''
lista_plataformas = ['netflix', 'disney', 'hulu', 'amazon']

# endpoint 2
@app.get('/')
def index():
    return {'message':'Welcome to the API! ',
    'opcion 1': 'get_word_count',
    'opcion 2': 'get_score_count',   
    'opcion 3': 'get_second_score',
    'opcion 4': 'get_rating_count'}
    
    
# endpoint 3, Consulta 1: cuenta el numero de veces que aparece una entrada (keyword) en 
# el título
@app.get("/get_word_count/")
def get_word_count(plataforma, keyword):
    df_full = df_concatenado
    df_full = df_full[df_full['platform'] == plataforma]
    output = df_full[df_full['title'].str.contains(keyword, na=False)]
    if plataforma not in lista_plataformas:
        return print('La plataforma introducida no esta en nuestra base de datos')
    else:
        return len(output)
    
# Consulta 2
anio = int  
@app.get("/get_score_count/")
def get_score_count(plataforma, anio):
    df_full = df_concatenado
    df_full = df_full[df_full['platform'] == plataforma]
    if plataforma not in lista_plataformas:
        return print('La plataforma introducida no esta en nuestra base de datos')
    else:
        return len(df_full[(df_full.score > 20) & (df_full.release_year == anio)])
    

# Consulta 3
@app.get("/get_second_score/")
def get_second_score(plataforma):
    if plataforma not in lista_plataformas:
        return print('La plataforma introducida no esta en nuestra base de datos')
    else:
        df_full = df_concatenado
        df_full = df_full[df_full['platform'] == plataforma]
        by_score_alph = df_full.sort_values(['score', 'title'], ascending=[False, True])
        segundo_titulo = by_score_alph.iloc[1, 4]
        score = by_score_alph.iloc[1, 14]
        return print('La Segunda película con mayor score para la plataforma es: ', segundo_titulo , 'con un score de ', score )


# Consulta 4
@app.get("/get_longest/")
def get_longest(plataforma, duration_type, release_year):
    if plataforma not in lista_plataformas:
        return print('La plataforma introducida no esta en nuestra base de datos')
    else:
        df_full = df_concatenado
        df_full = df_full[df_full['platform'] == plataforma]
        df_full = df_full[df_full['duration_type'] == duration_type]
        df_full = df_full[df_full['release_year'] == release_year]
        titulo_dur_type = df_full.loc[df_full.duration_int.idxmax()]
        return print(titulo_dur_type['title'], int(titulo_dur_type['duration_int']), (titulo_dur_type['duration_type']))


# Consulta 5
@app.get("/get_second_score/")
def get_rating_count(rating):
    df_full = df_concatenado
    df_full = df_full[df_full['rating'] == rating]
    return print('rating: ', df_full.iloc[0, 9], ', cantidad: ', len(df_full))
