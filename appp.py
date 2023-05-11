import streamlit as st
import pandas as pd


df= pd.read_csv('./moviesetl.csv')

def peliculas_mes(mes):
    '''
    The input is the month's name. The function returns the number of movies that were released that month historically.
    '''
    # Transformar el nombre del mes en su número correspondiente
    mes_n = mes
    
    if mes_n == 'Mes no válido':
        return 'Mes no válido'
    else:
        # Convertir la columna 'release_date' a tipo datetime
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        
        # Filtrar por el mes dado y luego contar
        respuesta = df[df['release_date'].dt.month == mes_n]['title'].count()
        return {'mes': mes, 'cantidad': respuesta}

# Interfaz de Streamlit
st.title('Consulta de películas por mes')

# Meses predefinidos
meses = {
    'Enero': 1,
    'Febrero': 2,
    'Marzo': 3,
    'Abril': 4,
    'Mayo': 5,
    'Junio': 6,
    'Julio': 7,
    'Agosto': 8,
    'Septiembre': 9,
    'Octubre': 10,
    'Noviembre': 11,
    'Diciembre': 12
}

# Obtener el mes seleccionado por el usuario
mes_seleccionado = st.selectbox('Seleccione un mes:', list(meses.keys()))

# Llamar a la función peliculas_mes y mostrar el resultado
if st.button('Consultar Mes'):
    resultado = peliculas_mes(meses[mes_seleccionado])
    if resultado == 'Mes no válido':
        st.error('Mes no válido. Por favor, seleccione un mes válido.')
    else:
        st.success(f"En el mes de {resultado['mes']} se estrenaron {resultado['cantidad']} películas.")


def peliculas_dia(dia):
    '''
    The input is the day of the week. The function returns the number of movies that were released that day historically.
    '''
    # Transformar el nombre del día en su número correspondiente
    dia_n = dia
    
    if dia_n == 'Día no válido':
        return 'Día no válido'
    else:
        # Convertir la columna 'release_date' a tipo datetime
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        
        # Filtrar por el día dado y luego contar
        respuesta = df[df['release_date'].dt.dayofweek == dia_n]['title'].count()
        return {'dia': dia, 'cantidad': respuesta}

# Interfaz de Streamlit
st.title('Consulta de películas por día de la semana')

# Días de la semana predefinidos
dias = {
    'Lunes': 0,
    'Martes': 1,
    'Miércoles': 2,
    'Jueves': 3,
    'Viernes': 4,
    'Sábado': 5,
    'Domingo': 6
}

# Obtener el día seleccionado por el usuario
dia_seleccionado = st.selectbox('Seleccione un día de la semana:', list(dias.keys()))

# Llamar a la función peliculas_dia y mostrar el resultado
if st.button('Consultar Dia'):
    resultado = peliculas_dia(dias[dia_seleccionado])
    if resultado == 'Día no válido':
        st.error('Día no válido. Por favor, seleccione un día válido.')
    else:
        st.success(f"En el día {resultado['dia']} se estrenaron {resultado['cantidad']} películas.")


def franquicia(franquicia):
    '''
    The input is the franchise, returning the number of movies, total and average profit
    '''
    # Nombres de las colecciones
    collection_names = df['collection'].unique()
    
    # Verificar si la franquicia es una entrada válida
    if franquicia in collection_names:
        franquicia = franquicia
    elif (franquicia + ' Collection') in collection_names:
        franquicia = (franquicia + ' Collection')
    else:
        return 'Colección no encontrada'
    
    # Calcular los resultados
    n_pelis = df[df['collection'] == franquicia]['title'].count()
    ganancia_total = df[df['collection'] == franquicia]['revenue'].sum()
    ganancia_promedio = df[df['collection'] == franquicia]['revenue'].mean()
    
    return {'franquicia': franquicia, 'cantidad': n_pelis, 'ganancia_total': round(ganancia_total, 0), 'ganancia_promedio': round(ganancia_promedio, 0)}

# Interfaz de Streamlit
st.title('Consulta de franquicias de películas')

# Colecciones disponibles
collection_names = df['collection'].unique()

# Obtener la franquicia seleccionada por el usuario
franquicia_seleccionada = st.selectbox('Seleccione una franquicia:', collection_names)

# Llamar a la función franquicia y mostrar el resultado
if st.button('Consultar'):
    resultado = franquicia(franquicia_seleccionada)
    if resultado == 'Colección no encontrada':
        st.error('Colección no encontrada. Por favor, seleccione una franquicia válida.')
    else:
        st.success(f"Franquicia: {resultado['franquicia']}")
        st.write(f"Cantidad de películas: {resultado['cantidad']}")
        st.write(f"Ganancia total: {resultado['ganancia_total']}")
        st.write(f"Ganancia promedio: {resultado['ganancia_promedio']}")







# Crear un conjunto vacío para almacenar los países únicos
unique_country = set()

# Iterar sobre cada fila en la columna con listas
for row in df['production_countries_name']:
    # Convertir los caracteres individuales en una lista de países
    countries = [c.lower() for c in eval(row)]
    # Actualizar el conjunto con los países únicos
    unique_country.update(set(countries))

# Define la función para obtener la cantidad de películas producidas en un país
def peliculas_pais(pais):
    pais_low = pais.lower()
    # Validar la entrada
    if pais_low in unique_country:
        # Crear una máscara booleana que sea Verdadera para las filas donde aparece pais en 'production_countries_name'
        mask = df['production_countries_name'].apply(lambda x: pais_low in [c.lower() for c in eval(x)])
        # Utilizar la máscara booleana para filtrar el dataframe
        n_films = df[mask]['title'].count()
        return {'pais': pais, 'cantidad': n_films}
    else:
        return 'País no válido'

# Crea una interfaz de usuario en Streamlit
st.title("Contador de películas por país")
pais = st.selectbox("Selecciona un país:", list(unique_country))
if pais:
    resultado = peliculas_pais(pais)
    if resultado == 'País no válido':
        st.write(resultado)
    else:
        st.write("En", resultado["pais"], "se han producido", resultado["cantidad"], "películas.")











# create an empty set to hold unique companies
unique_company = set()

# Iterar sobre cada fila en la columna con listas
for row in df['production_companies_name']:
    # Convertir los caracteres individuales en una lista de compañías
    company = [c.lower() for c in eval(row)]
    # Actualizar el conjunto con las compañías únicas
    unique_company.update(set(company))

# convert the set back to a list and set names to lowercase
unique_company = [company.lower() for company in list(unique_company)]

# Create a SelectBox for selecting the production company
selected_productora = st.selectbox('Selecciona una productora', unique_company, index=0)

def productoras(productora):
    '''
    The input is the production company, returning the total profit and the number of movies they produced.
    '''
    productora_low = productora.lower()
    #Validate input
    if productora_low in unique_company:
        # create a boolean mask that is True for rows where productora appears in 'production_companies_name'
        mask = df['production_companies_name'].apply(lambda x: productora_low in [p.lower() for p in eval(x)])
        # use the boolean mask to filter the dataframe
        n_films = df[mask]['title'].count()
        total_revenue = df[mask]['revenue'].sum()
        return {'productora':productora, 'ganancia_total':total_revenue, 'cantidad':n_films}
    else:
        return 'Productora no válida'

# Call the function with the selected production company
result = productoras(selected_productora)
# Interfaz de Streamlit
st.title('Consulta de productora')
# Display the result
if isinstance(result, str):
    st.write(result)
else:
    st.write('Productora:', result['productora'])
    st.write('Ganancia total:', result['ganancia_total'])
    st.write('Cantidad de películas:', result['cantidad'])







def retorno(pelicula):
    '''
    The input is the movie's title, it returns the investment, the profit, the return and the year in which it was released
    '''
    try:
        peli_low = pelicula.lower()
        indx = df[df['title'].apply(lambda x: x.lower()) == peli_low].index
        inversion = int(df.loc[indx,'budget'])
        ganancia = int(df.loc[indx,'revenue'])
        retorno = int(df.loc[indx,'return'])
        anio = int(df.loc[indx,'release_year'])
        return {'pelicula':pelicula, 'inversion':inversion, 'ganancia':ganancia, 'retorno':retorno, 'anio':anio}
    except:
        return 'Película no válida'

# Get the list of movie titles
movie_titles = df['title'].tolist()

# Create a SelectBox for selecting the movie
selected_movie = st.selectbox('Selecciona una película', movie_titles)

# Call the function with the selected movie
result = retorno(selected_movie)

# Display the result
# Interfaz de Streamlit
st.title('Consulta informacion de películas')
if isinstance(result, str):
    st.write(result)
else:
    st.write('Película:', result['pelicula'])
    st.write('Inversión:', result['inversion'])
    st.write('Ganancia:', result['ganancia'])
    st.write('Retorno:', result['retorno'])
    st.write('Año de lanzamiento:', result['anio'])
