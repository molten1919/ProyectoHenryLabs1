# ProyectoHenryLabs1: Data Engineer

A a partir de cuatro archivos csv que contienen datos e información de cuatro servicios de streaming; Amazon, Disney, hulu, y Netflix, se realizó primero un trabajo de EDA y ETL con el fin de preparar y limpiar los datos. Se realizaron 5 transformaciones de esos archivos, cuyo método viene en el archivo 'Transformaciones.ipynb', utilizando python con sus librerías pandas, numpy, y matplotlib, con el objetivo de disponibilizar la información requerida por el departamento de análisis de datos, mediante una API que se diseñó posteriormente con el framework fastapi de python.

Se escribió el códidgo para las queries que irían en el desarrollo de la api, estas queries vienen en el archivo 'Consultas_Api.ipynb'. Este código se fué pasando al archivo 'main.py' donde se montó la api (usando fastapi) y Deta para hacer el deployment en la nube.

Se ha logró ejecutar correctamente las consultas en la api creada con la url proporcionada por Deta.

### Requisitos

- Una pc con conexión a internet.

### Uso

Hay cinco consultas que se pidieron, y cada una de ellas está en un endpoint diferente de la API, así, para ejecutar la primera consulta, a la dirección URL proporcionada se le añade la siguiente instrucción:

"/get_word_count/{plataforma}/{keyword}"

y se introduce la plataforma requerida (en {plataforma}) y el keyword que se quiere buscar (en {keyword}). Por ejemplo, si se quiere buscar en la plataforma Netflix cuantas veces aparece el keyword 'love', habría que pegar lo siguiente, completando la URL:

"/get_word_count/{Netflix}/{love}"


Con el objetivo de disponibilizar los datos mediante una API
En este proyecto se realizó un trabajo de EDA, ETL, y deployment de una API a partir de 4 archivos csv. Se realizaron 5 transformaciones de esos archivos, cuyo método viene en el archivo 'Transformaciones.ipynb'. 

Después se escribió el códidgo para las queries que irían en el desarrollo de la api, estas queries vienen en el archivo 'Consultas_Api.ipynb'. Este código se fué pasando al archivo 'main.py' donde se montó la api con el módulo fastapi de python y con Deta.

Se ha logrado correr las consultas en la api creada con la url especificada.
