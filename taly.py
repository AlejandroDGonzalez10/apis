import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from plotly.subplots import make_subplots
from streamlit_folium import folium_static
import re

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
menu=('Incio', 'Dashboard', 'TalyIA','Dashboard interno','Back End','Contactanos', )
seleccion=st.sidebar.selectbox('TALENTIA Menu', menu )


if seleccion == "Incio":
    
    st.image("talentia.jpeg", use_column_width=True, caption="")
    st.markdown("<h1 style='text-align: center;'>TALENTIA</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><h2 style='color: #FF8C00;'>¿QUIENES SOMOS?</h2></div>", unsafe_allow_html=True)        
    st.write('')
    st.markdown("<div style='text-align: center;'><h5>En TalentIA somos una consultora de talento que te ayuda a encontrar los perfiles que necesitas de forma eficiente y efectiva. Nuestra tecnología de Inteligencia Artificial nos permite estandarizar las características de los candidatos para que puedas recibir recomendaciones precisas y acordes a tus necesidades. Además, nos enfocamos en ofrecer un servicio personalizado y de calidad, donde nos aseguramos de entender tus requerimientos y objetivos para poder brindarte las soluciones más adecuadas. En TalentIA estamos comprometidos con la excelencia y la satisfacción de nuestros clientes. ¡Déjanos ayudarte a encontrar el talento que necesitas para llevar tu empresa al siguiente nivel! 🚀</h5></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><h2 style='color: #FF8C00;'>Misión, Visión y Valores de TALENTIA</h2></div>", unsafe_allow_html=True)
    
    st.write('')
    st.markdown('##### Misión')
    st.markdown('**En TALENTIA, nuestra misión es ser la consultora de talento líder en soluciones innovadoras para la búsqueda y selección de perfiles.**')
    st.markdown('##### Visión')
    st.markdown('**Nuestra visión es transformar el proceso de reclutamiento y selección de personal, a través de la implementación de tecnologías de vanguardia y la optimización de los procesos de búsqueda y selección estandarizando los recursos optimos para nuestros socios.**')
    st.markdown('##### Valores')
    st.markdown('**En TALENTIA, nuestros valores son:**')
    st.markdown('- ***Compromiso*** : Estamos comprometidos con nuestros Socios, brindando un servicio eficiente y de excelencia.')
    st.markdown('- ***Innovación***: Buscamos siempre soluciones innovadoras para mejorar nuestros procesos y servicios.')
    st.markdown('- ***Integridad***: Actuamos con transparencia y honestidad en todas nuestras relaciones, manteniendo un alto nivel de ética profesional.')
    st.markdown('- ***Trabajo en equipo***: Fomentamos un ambiente de colaboración y trabajo en equipo, para lograr los mejores resultados.')
    st.markdown('- ***Pasión***: Nos apasiona lo que hacemos y nos esforzamos cada día por brindar el mejor servicio a nuestros clientes y candidatos.')
    
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<div style='text-align: center;'><h1 style='color: #002366;'>SITUACION ACTUAL DE LAS EMPRESAS Y RECLUTADORAS</h1></div>", unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    st.markdown('##### - En un mercado laboral cada vez más competitivo, es esencial contar con el equipo adecuado que pueda llevar a su empresa o reclutadora al éxito. En nuestra consultora de recursos humanos, nos apasiona la innovación y la excelencia en todo lo que hacemos. Con más de XX años de experiencia en la industria, nuestro equipo de expertos en recursos humanos ha ayudado a innumerables clientes a superar los desafíos de contratación más difíciles, desde la disminución en las contrataciones deseadas hasta los altos costos de contratación.')
    st.markdown('##### - Nos enorgullece brindar soluciones únicas y personalizadas que superan las expectativas de nuestros clientes. Somos innovadores y estamos a la vanguardia de las últimas tendencias y tecnologías de la industria, lo que nos permite ofrecer un servicio de alta calidad y personalizado para cada cliente.')
    st.markdown('##### - Además, nos comprometemos a brindar soluciones efectivas y únicas. Contamos con una amplia red de contactos y un sistema avanzado de recomendación que nos permite encontrar a los candidatos adecuados para cada puesto y ayudar a nuestros clientes a tomar decisiones de contratación informadas y acertadas.')
    st.markdown('##### - Confíe en nosotros para brindarle soluciones de recursos humanos únicas y efectivas que lo ayuden a superar los desafíos de contratación más difíciles y a encontrar al candidato perfecto para cada puesto. En nuestra consultora, nos apasiona la excelencia y estamos dedicados a ayudar a nuestros clientes a alcanzar el éxito en un mercado laboral cada vez más competitivo.')
    
    st.write('')
    st.write('')
    st.write('')
    
    problematicas = {
        "Disminucion en contrataciones deseadas": "📉",
        "Bajo atractivo de la vacante ofertadas": "🙅‍♂️",
        "Perdida de tiempo en permanencia de los colaboradores": "🚫",
        "Largos periodos en tiempo promedio de contratacion": "⏳",
        "Altos costos de contratacion": "💸"
    }


    st.markdown("<div style='text-align: center;'><h1 style='color: #002366;'>PROBLEMAS A SOLUCIONAR</h1></div>", unsafe_allow_html=True)


    st.write('')
    st.write('')
    st.write('')
    st.write('')

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        st.metric("CONTRATACIONES", str(problematicas["Disminucion en contrataciones deseadas"]) , delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Disminucion en contrataciones deseadas</h5></p>", unsafe_allow_html=True)

    with col2:
        st.metric("BAJO ATRACTIVO", str(problematicas["Bajo atractivo de la vacante ofertadas"]) , delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Bajo atractivo de la vacante ofertadas</h5></p>", unsafe_allow_html=True)

    with col3:
        st.metric("PERDIDA", str(problematicas["Perdida de tiempo en permanencia de los colaboradores"]) , delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Perdida de tiempo en permanencia de los colaboradores</h5></p>", unsafe_allow_html=True)

    with col4:
        st.metric("LARGOS PERIODOS", str(problematicas["Largos periodos en tiempo promedio de contratacion"]) , delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Largos periodos en tiempo promedio de contratacion</h5></p>", unsafe_allow_html=True)

    with col5:
        st.metric("COSTOS ALTOS", str(problematicas["Altos costos de contratacion"]) , delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Altos costos de contratacion</h5></p>", unsafe_allow_html=True)




    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.markdown("<div style='text-align: center;'><h1 style='color: #FF8C00;'>¿QUE BENEFICIOS TIENES CON TALY?</h1></div>", unsafe_allow_html=True)
    
    st.write('')
    st.write('') 

    st.markdown('##### ¿Estás buscando una forma efectiva de encontrar y contratar el mejor talento para tu empresa? ¿Te gustaría contar con un servicio personalizado y de calidad que te permita obtener recomendaciones precisas y acordes a tus necesidades? Si es así, estás en el lugar correcto. En TalentIA somos una consultora de talento especializada en la búsqueda y selección de los perfiles más adecuados para cada empresa. Nos respalda una tecnología de Inteligencia Artificial que nos permite estandarizar las características de los candidatos, agilizando el proceso de selección y optimizando los resultados.')
    
    st.write('')
    st.write('') 

    st.markdown('##### En TalentIA nos enfocamos en entender tus requerimientos y objetivos para brindarte soluciones personalizadas que se adapten a tus necesidades específicas. Nos comprometemos a ofrecerte un servicio de calidad, donde la excelencia y la satisfacción de nuestros clientes son nuestra prioridad. Trabajamos con empresas de todos los tamaños y sectores, y contamos con un equipo de expertos en consultoría de talento que te guiará en todo momento para que tomes las mejores decisiones.')
    
    st.write('')
    st.write('')

    st.markdown('##### Además, en TalentIA creemos que la contratación de talento debe ser un proceso justo e inclusivo, por lo que nos aseguramos de fomentar la diversidad y la igualdad de oportunidades en todas nuestras búsquedas. Estamos comprometidos con la construcción de un mercado laboral más equitativo y justo para todos.')
    
    st.write('')
    st.write('')
    

    kpis = {
        "Aumento de las contrataciones un": 20,
        "Aumento de atractivo de la vacante en": 15,
        "Mejora en el tiempo de permanencia de los colaboradores": 10,
        "Reducción de en el tiempo promedio de contratacion": 15,
        "Reduccion de costos de contratacion": 50
    }


    st.markdown("<div style='text-align: center;'><h1 style='color: #FF8C00;'>BENEFICIO DE NUESTRO SERVICIOS</h1></div>", unsafe_allow_html=True)

    st.write('')
    st.write('')
    st.write('')
    st.write('')

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        st.metric("BENEFICIOS EN UN", str(kpis["Aumento de las contrataciones un"]) + "%", delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Aumento de las contrataciones</h5></p>", unsafe_allow_html=True)

    with col2:
        st.metric("BENEFICIOS EN UN", str(kpis["Aumento de atractivo de la vacante en"]) + "%", delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Aumento de atractivo en la vacante</h5></p>", unsafe_allow_html=True)

    with col3:
        st.metric("BENEFICIOS EN UN", str(kpis["Mejora en el tiempo de permanencia de los colaboradores"]) + "%", delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Mejora en el tiempo de permanencia de los colaboradores</h5></p>", unsafe_allow_html=True)

    with col4:
        st.metric("BENEFICIOS EN UN", str(kpis["Reducción de en el tiempo promedio de contratacion"]) + "%", delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Reducción de en el tiempo promedio de contratación</h5></p>", unsafe_allow_html=True)

    with col5:
        st.metric("BENEFICIOS EN UN", str(kpis["Reduccion de costos de contratacion"]) + "%", delta_color="inverse")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Reducción de costos de contratación</h5></p>", unsafe_allow_html=True)


    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.markdown("<div style='text-align: center;'><h1 style='color: #002366;'>SISTEMA DE RECOMENDACIÓN</h1></div>", unsafe_allow_html=True)
    
    st.write('')
    st.write('')
    st.write('')

    st.subheader('Con nuestro modelo de Machine Learning de estandarización de perfiles, nos enfocamos en maximizar las posibilidades de crecimiento con el mínimo esfuerzo y obtener resultados óptimos al comprender las características de tu vacante a cubrir, recomendándote el perfil más adecuado para satisfacer tus necesidades.')


    st.write('')
    st.write('')
    st.write('')


    st.markdown("<div style='text-align: center;'><h2 style='color: #007000;'> Esto es un ejemplo de como medimos el avance con nuestros socios</h2</div>", unsafe_allow_html=True)

    st.write('')
    st.write('')
    st.write('')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:# Creamos una casilla con el número de empleos totales y su variación respecto al mes anterior
        st.metric("CONTRATACIONES", "10", delta="2 (+20%)", delta_color="normal")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Contrataciones totales por mes </h5></p>", unsafe_allow_html=True)

    with col2:
        st.metric("ASPIRANTES ", "30", delta="4 (+15%)", delta_color="normal")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Aspirantes adecuados en entrevistas</h5></p>", unsafe_allow_html=True)

    with col3:
        st.metric("PERMANENCIA ANUAL", "20", delta="4 (+20%)", delta_color="normal")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Mas tiempo de permanencia de los colaboradores en periodo anual</h5></p>", unsafe_allow_html=True)

    with col4:
        st.metric("TIEMPO EN MESES", "3", delta="2.5 (+15%)", delta_color="normal")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Duracion de 3 meses a 2 meses en contratacion</h5></p>", unsafe_allow_html=True)

    with col5:
        st.metric("COSTOS", "1000 usd", delta="500 (-50%)", delta_color="normal")
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>Reduccion en los costos a la mitad segun valores del mercado</h5></p>", unsafe_allow_html=True)


    
    
    

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<div style='text-align: center;'><h1 style='color: #002366;'>TE MOSTRAMOS NUESTRO ENFOQUE Y ANALISIS DEL CONTEXTO LABORAL EN EL SECTOR IT DE LATAM</h1></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><h3>Nuestro análisis abarca los países de Latino América mostrandote el crecimiento de tendecia laboral de los ultimos años del sector IT, en el siguiente grafico puedes ver y elegir el país observando el crecimiento de la tendencia de cada uno desde el 2016 a la actualidad.</h3></div>", unsafe_allow_html=True)


    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    # Generamos las fechas
    fechas = pd.date_range(start='2016-01-01', end=pd.Timestamp.today(), freq='Q')

    # Creamos un DataFrame vacío con las fechas como índice
    df = pd.DataFrame(index=fechas)

    # Creamos un diccionario con los países y sus datos aleatorios progresivos
    datos = {'Argentina': np.cumsum(np.random.randint(low=50, high=300, size=len(fechas))),
            'Brazil': np.cumsum(np.random.randint(low=200, high=500, size=len(fechas))),
            'Chile': np.cumsum(np.random.randint(low=100, high=3500, size=len(fechas))),
            'Colombia': np.cumsum(np.random.randint(low=150, high=400, size=len(fechas))),
            'Mexico': np.cumsum(np.random.randint(low=170, high=600, size=len(fechas))),
            'Peru': np.cumsum(np.random.randint(low=80, high=300, size=len(fechas))),
            'Uruguay': np.cumsum(np.random.randint(low=20, high=100, size=len(fechas))),
            'Bolivia': np.cumsum(np.random.randint(low=50, high=200, size=len(fechas))),
            'Paraguay': np.cumsum(np.random.randint(low=30, high=150, size=len(fechas))),
            'Guatemala': np.cumsum(np.random.randint(low=70, high=250, size=len(fechas))),
            'Panama': np.cumsum(np.random.randint(low=90, high=400, size=len(fechas))),
            'Costa Rica': np.cumsum(np.random.randint(low=60, high=300, size=len(fechas)))}

    # Creamos el DataFrame a partir del diccionario
    df = pd.DataFrame(datos, fechas)

    # Creamos el título del dashboard
    st.markdown("<div><h2 style='color: #007000;'>Gráfico de tendencia de vacantes laborales en el sector IT en Latinoamérica</h2></div>", unsafe_allow_html=True)


    # Creamos un filtro para seleccionar el país
    paises = df.columns.tolist()
    pais_seleccionado = st.selectbox('Seleccione un país', paises)

    # Filtramos el dataframe por país
    df_filtrado = df[[pais_seleccionado]]

    # Creamos las columnas para colocar el gráfico y el mapa
    
    # Creamos el gráfico de tendencia con Plotly Express y lo mostramos en la primera columna
    fig1 = px.line(df_filtrado, x=df_filtrado.index, y=pais_seleccionado, title=f'Promedio de vacantes laborales de {pais_seleccionado} del sector IT')
    fig1.update_layout( xaxis_title="Años",)
  

    # Leemos los datos para el mapa
    df_mapa = pd.read_csv('2014_world_gdp_with_codes.csv')

    # Filtramos el dataframe para obtener los datos del país seleccionado
    df_mapa_filtrado = df_mapa[df_mapa['COUNTRY'] == pais_seleccionado]


    # Creamos el mapa del país seleccionado con Plotly y lo mostramos en la segunda columna
    fig2 = px.choropleth(df_mapa_filtrado, locations='CODE', color='GDP (BILLIONS)', 
                        hover_name='COUNTRY', projection='mercator',
                        color_continuous_scale='Oranges')
    fig2.update_geos(fitbounds='locations', visible=False)
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig1)
    col2.plotly_chart(fig2)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')


    st.markdown("<div style='text-align: center;'><h1 style='color: #002366;'>OFERTA LABORALES EN EL ÁREA DE DATA</h1></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><h3>En princpio TALY se enfoca en el area de DATA por eso nos especializamos en los tres perfiles principales como ser DATA ANLAYTIC, DATA ENGINEER Y DATA SCIENCE es así que confiamos en nuestra excelencia en la especialización y análisis de estos perfiles para que tu empresa pueda tener los mejores talentos.</h3></div>", unsafe_allow_html=True)


    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')


    # Cargamos los datos de cada archivo CSV
    dataa = pd.read_csv("linkedin_DA_empleos.csv")
    datae = pd.read_csv("linkedin_DI_empleos.csv")
    datas = pd.read_csv("linkedin_DS_empleos.csv")

    # Creamos los gráficos de barras con Plotly Express
    fig1 = go.Figure(go.Histogram(x=dataa["localidad"], name="DA"))
    fig2 = go.Figure(go.Histogram(x=datae["localidad"], name="DI"))
    fig3 = go.Figure(go.Histogram(x=datas["localidad"], name="DS"))

    # Creamos una figura con subplots
    fig = sp.make_subplots(rows=1, cols=3)

    # Añadimos cada gráfico al subplot correspondiente
    fig.add_trace(fig1.data[0], row=1, col=1)
    fig.add_trace(fig2.data[0], row=1, col=2)
    fig.add_trace(fig3.data[0], row=1, col=3)

    # Configuramos el diseño del gráfico
    fig.update_layout(
        title="   DATA ANALYTIC                                                                                 DATA ENGINEER                                                                                   DATA SCIENCE",
        xaxis_title="Localidad",
        yaxis_title="Cantidad de puestos de trabajo",
        font=dict(size=14),
        showlegend=False,
        width=1000,
        height=400,
    )

    # Mostramos el gráfico en Streamlit
    st.plotly_chart(fig)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')


    st.markdown("<div style='text-align: center;'><h1 style='color: #002366;'>MODALIDAD DE TRABAJO POR LOCALIDAD</h1></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><h3>Aquí observamos los porsentajes de la modalidad de trabajo que oferta el mercado en los distintos perfiles y podemos seleccionar el pais de Lationo América para tener una mejor descripción </h3></div>", unsafe_allow_html=True)


    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')



    # Cargamos los datos de cada archivo CSV
    dataa = pd.read_csv("linkedin_DA_empleos.csv")
    datae = pd.read_csv("linkedin_DI_empleos.csv")
    datas = pd.read_csv("linkedin_DS_empleos.csv")
    # Concatenar los tres dataframes en uno solo
    data = pd.concat([dataa, datae, datas], ignore_index=True)
    # Ordenar el dataframe por la columna de localidad
    data = data.sort_values(by='localidad')
    # Reiniciar los índices del dataframe
    data = data.reset_index(drop=True)

    # Creamos el título del dashboard
    st.header('Porcentaje de ofertas laborales por modealidad de cada pais en los perfiles DATA')

    # Creamos un filtro para seleccionar el país
    paises = data.groupby('localidad')
    pais_seleccionado = st.selectbox('Seleccione un pais', list(paises.groups.keys()))
    # Filtramos los datos basado en la selección del usuario
    dataa_filtrado = dataa.loc[dataa['localidad'] == pais_seleccionado]
    datae_filtrado = datae.loc[datae['localidad'] == pais_seleccionado]
    datas_filtrado = datas.loc[datas['localidad'] == pais_seleccionado]

    colores = ["#FFA07A", "#20B2AA", "#9370DB"]

    # Creamos los gráficos de dona con Plotly Express
    fig1 = px.pie(dataa_filtrado, names="modalidad", title="Modalidad de los puestos de trabajo en DATA ANALYTICS", hole=0.5, color_discrete_sequence=colores)
    fig2 = px.pie(datae_filtrado, names="modalidad", title="Modalidad de los puestos de trabajo en DATA ENGINEER", hole=0.5, color_discrete_sequence=colores)
    fig3 = px.pie(datas_filtrado, names="modalidad", title="Modalidad de los puestos de trabajo en DATA SCIENCE", hole=0.5, color_discrete_sequence=colores)

    # Creamos una figura con subplots
    fig = sp.make_subplots(rows=3, cols=1, specs=[[{"type": "domain"}], [{"type": "domain"}], [{"type": "domain"}]])

    # Añadimos cada gráfico al subplot correspondiente
    fig.add_trace(fig1.data[0], row=1, col=1)
    fig.add_trace(fig2.data[0], row=2, col=1)
    fig.add_trace(fig3.data[0], row=3, col=1)

    # Configuramos el diseño del gráfico
    fig.update_layout(
        title="                        Porcentaje de ofertas laborales",
        font=dict(size=14),
        width=1500,
        height=1250,
        margin=dict( t=80, b=250, l=20, r=1000)
        # Aumentamos la altura para dar espacio a los gráficos
    )


    #------------------------------------------------------------------------------------------------
    
    
    color_discrete_map = ("#2E86C1","#FF3131","#85C1E9",)

    # Filtramos los datos basado en la selección del usuario
    dataa_fil = dataa.loc[dataa['localidad'] == pais_seleccionado]
    datae_fil = datae.loc[datae['localidad'] == pais_seleccionado]
    datas_fil = datas.loc[datas['localidad'] == pais_seleccionado]


    # Creamos los gráficos de barras con Plotly Express
    fig4 = go.Figure(go.Histogram(x=dataa_fil["modalidad"], name="DA", marker_color=color_discrete_map))
    fig5 = go.Figure(go.Histogram(x=datae_fil["modalidad"], name="DI", marker_color=color_discrete_map))
    fig6 = go.Figure(go.Histogram(x=datas_fil["modalidad"], name="DS", marker_color=color_discrete_map))


    fig4.update_layout(
        title="Cantidad de ofertas laborales en DATA ANALYTICS",
        xaxis_title="Modalidad",
        yaxis_title="Cantidad de ofertas",
        font=dict(size=14),
        showlegend=False,
        width=500,
        height=350,
        margin=dict( t=50, b=25, l=100, r=10)
    )
    fig5.update_layout(
        title="Cantidad de ofertas laborales en DATA ENGINEER",
        xaxis_title="Modalidad",
        yaxis_title="Cantidad de ofertas",
        font=dict(size=14),
        showlegend=False,
        width=500,
        height=350,
        margin=dict( t=50, b=80, l=100, r=10)

    )
    fig6.update_layout(
        title="Cantidad de ofertas laborales en DATA SCIENCE",
        xaxis_title="Modalidad",
        yaxis_title="Cantidad de ofertas",
        font=dict(size=14),
        showlegend=False,
        width=500,
        height=350,
        margin=dict( t=25, b=100, l=100, r=10)
    )
    # Mostramos los gráficos de barras en la segunda columna

    col1, col2 = st.columns(2)
    col2.plotly_chart(fig)
    col1.plotly_chart(fig4)
    col1.plotly_chart(fig5)
    col1.plotly_chart(fig6)

#     df=pd.read_csv('continentescategory.csv')


#         # Agrupar datos por continente y categoría
#     continent_data = df.groupby(['Continent', 'category'])['Count'].sum().reset_index()

#     # Crear lista de continentes únicos para selectbox
#     continent_list = continent_data['Continent'].unique().tolist()

#     # Crear selectbox para seleccionar continente
#     pais_seleccionado = st.selectbox('Seleccione un país', continent_list)

#     # Filtrar datos por continente seleccionado
#     continent_data_filtered = continent_data[continent_data['Continent'] == pais_seleccionado]

#     # Crear gráfico de barras horizontales
#     fig = px.bar(continent_data_filtered, x='Count', y='category', orientation='h', color='category')

#     # Mostrar gráfico
#     st.plotly_chart(fig)

#    # Agrupar datos por continente y categoría
#     continent_data = df.groupby(['Continent', 'category'])['Count'].sum().reset_index()

#     # Crear figura de mapa
#     fig = go.Figure(data=go.Choropleth(
#         locations=continent_data['Continent'], # Ubicación de cada continente en el mapa
#         z=continent_data['Count'], # Cantidad de categorías en cada continente
#         locationmode='continent names', # Modo de ubicación de los continentes
#         colorscale='Reds', # Escala de colores
#         colorbar_title='Cantidad' # Título de la leyenda de colores
#     ))

#     # Actualizar el diseño de la figura
#     fig.update_layout(
#         title_text='Cantidad de categorías por continente', # Título del mapa
#         geo=dict(
#             showframe=False, # Ocultar el marco del mapa
#             showcoastlines=True, # Mostrar las líneas costeras
#             projection_type='natural earth' # Tipo de proyección del mapa
#         )
#     )

#     # Mostrar el mapa
#     st.plotly_chart(fig)



#-------------------------------------------------------------------------------------------------------------------------------
elif seleccion == "Dashboard":
    postulaciones = {
        "6 meses": 6,
        "3 meses": 3,
        "1 mes": 1,
        
    }


    st.markdown("<div style='text-align: center;'><h1 style='color: #FF8C00;'>POSTULACIONES EN PERIODOS</h1></div>", unsafe_allow_html=True)

    st.write('')
    st.write('')
    st.write('')
    st.write('')

    col1, col2, col3  = st.columns(3)


    with col1:
        st.metric("PERIODO", str(postulaciones["6 meses"]) + " MESES", delta_color="inverse")
    
    with col2:
        st.metric("PERIODO", str(postulaciones["3 meses"]) + " MESES", delta_color="inverse")
   
    with col3:
        st.metric("PERIODO", str(postulaciones["1 mes"]) + " MESES", delta_color="inverse")

    





    



    col1, col2, col3 = st.columns(3)
    periodo = ""

    with st.container():
        col1, col2, col3 = st.columns(3)
        if col1.button("seleccione 6 meses"):
            periodo = "seleccione 6 meses"
        if col2.button("seleccione 3 meses"):
            periodo = "seleccione 3 meses"
        if col3.button("seleccione 1 mes"):
            periodo = "seleccione 1 mes"


    if periodo == "seleccione 6 meses":
        with col1:
            st.empty()
            st.metric("BENEFICIO", str("") + " ", delta="+0%", delta_color="normal")
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>CANTIDAD DE POSTULACIONES</h5></p>", unsafe_allow_html=True)

                   # Convertir el diccionario en un DataFrame de pandas
        # Definimos los datos
        dict_1_mes = {'remoto_e': 17, 'onsite_e': 20, 'hybrid_e': 4, 'DATA ENGINEER': 38, 'remoto_a': 4, 'onsite_a': 12, 'hybrid_a': 9, 'DATA ANALYTIC': 26, 'remoto_s': 4, 'onsite_s': 2, 'hybrid_s': 4, 'DATA SCIENCE': 12}
        dict_3_meses = {'remoto_e': 24, 'onsite_e': 31, 'hybrid_e': 6, 'DATA ENGINEER': 48, 'remoto_a': 6, 'onsite_a': 18, 'hybrid_a': 12, 'DATA ANALYTIC': 37, 'remoto_s': 6, 'onsite_s': 3, 'hybrid_s': 6, 'DATA SCIENCE': 18}
        dict_6_meses = {'remoto_e': 38, 'onsite_e': 33, 'hybrid_e': 10, 'DATA ENGINEER': 57, 'remoto_a': 10, 'onsite_a': 19, 'hybrid_a': 14, 'DATA ANALYTIC': 38, 'remoto_s': 9, 'onsite_s': 5, 'hybrid_s': 9, 'DATA SCIENCE': 24}

        # Preparamos los datos para el gráfico
        y_labels = ['DATA ENGINEER', 'DATA ANALYTIC', 'DATA SCIENCE']
        x_remoto = [dict_1_mes['remoto_e'], dict_1_mes['remoto_a'], dict_1_mes['remoto_s']]
        x_onsite = [dict_1_mes['onsite_e'], dict_1_mes['onsite_a'], dict_1_mes['onsite_s']]
        x_hybrid = [dict_1_mes['hybrid_e'], dict_1_mes['hybrid_a'], dict_1_mes['hybrid_s']]

        # Creamos la figura
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x_remoto, y=y_labels, name='Remoto', marker_color='purple', orientation='h'))
        fig.add_trace(go.Bar(x=x_onsite, y=y_labels, name='Onsite', marker_color='orange', orientation='h'))
        fig.add_trace(go.Bar(x=x_hybrid, y=y_labels, name='Hybrid', marker_color='grey', orientation='h'))

        # Ajustamos la presentación del gráfico
        fig.update_layout(title='Evolución de posiciones en los últimos 6 meses', yaxis_title='Modalidad', xaxis_title='Posiciones')
        fig.update_xaxes(range=[0, 30])
        # Definimos los datos
        dict_6_meses = {'DATA ENGINEER': 41, 'DATA ANALYTIC': 24, 'DATA SCIENCE': 9}

        labels = list(dict_6_meses.keys())
        values = list(dict_6_meses.values())

        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

        fig2.update_layout(title='Puestos en los últimos 6 meses',
                        annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
      
        # Mostramos el gráfico en Streamlit
        col1,col2= st.columns(2)
        col1.plotly_chart(fig)

        col2.plotly_chart(fig2)

        
                # Preparamos los datos para el gráfico
        y_labels = ['DATA ENGINEER', 'DATA ANALYTIC', 'DATA SCIENCE']
        dict_1_mes = {
            'remoto_e': 2,
            'remoto_a': 5,
            'remoto_s': 1,
            'onsite_e': 3,
            'onsite_a': 7,
            'onsite_s': 2,
            'hybrid_e': 5,
            'hybrid_a': 3,
            'hybrid_s': 2
        }
                # Preparamos los datos para el gráfico
        y_labels = ['DATA ENGINEER', 'DATA ANALYTIC', 'DATA SCIENCE']
        x_remoto = [dict_1_mes['remoto_e'], dict_1_mes['remoto_a'], dict_1_mes['remoto_s']]
        x_onsite = [dict_1_mes['onsite_e'], dict_1_mes['onsite_a'], dict_1_mes['onsite_s']]
        x_hybrid = [dict_1_mes['hybrid_e'], dict_1_mes['hybrid_a'], dict_1_mes['hybrid_s']]

        # Creamos la figura
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=x_remoto, y=y_labels, name='Remoto', marker_color='purple', orientation='h'))
        fig1.add_trace(go.Bar(x=x_onsite, y=y_labels, name='Onsite', marker_color='orange', orientation='h'))
        fig1.add_trace(go.Bar(x=x_hybrid, y=y_labels, name='Hybrid', marker_color='grey', orientation='h'))

        # Ajustamos la presentación del gráfico
        fig1.update_layout(title='Evolución de posiciones en los últimos 6 meses', yaxis_title='Modalidad', xaxis_title='Posiciones')
        fig1.update_xaxes(range=[0, 30])
        dict_6_meses = {'DATA ENGINEER': 10, 'DATA ANALYTIC': 15, 'DATA SCIENCE': 5}

        labels = list(dict_6_meses.keys())
        values = list(dict_6_meses.values())

        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

        fig2.update_layout(title='Puestos vigentes',
                        annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
      
        # Mostramos el gráfico en Streamlit
        col1, col2 =st.columns(2)
        col2.plotly_chart(fig2)
        col1.plotly_chart(fig1)

    elif periodo == "seleccione 3 meses":
        with col2:
            st.empty()
            st.metric("BENEFICIO", str("") + " ", delta="+30%", delta_color="normal")
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>CANTIDAD DE POSTULACIONES</h5></p>", unsafe_allow_html=True)

        
            # Definimos los datos
        dict_1_mes = {'remoto_e': 18, 'onsite_e': 22, 'hybrid_e': 4, 'DATA ENGINEER': 40, 'remoto_a': 4, 'onsite_a': 13, 'hybrid_a': 9, 'DATA ANALYTIC': 27, 'remoto_s': 4, 'onsite_s': 2, 'hybrid_s': 4, 'DATA SCIENCE': 13}
        dict_3_meses = {'remoto_e': 26, 'onsite_e': 33, 'hybrid_e': 6, 'DATA ENGINEER': 50, 'remoto_a': 6, 'onsite_a': 19, 'hybrid_a': 13, 'DATA ANALYTIC': 39, 'remoto_s': 6, 'onsite_s': 3, 'hybrid_s': 6, 'DATA SCIENCE': 19}
        dict_6_meses = {'remoto_e': 40, 'onsite_e': 35, 'hybrid_e': 10, 'DATA ENGINEER': 60, 'remoto_a': 10, 'onsite_a': 20, 'hybrid_a': 15, 'DATA ANALYTIC': 40, 'remoto_s': 10, 'onsite_s': 5, 'hybrid_s': 10, 'DATA SCIENCE': 25}

        # Preparamos los datos para el gráfico
        y_labels = ['DATA ENGINEER', 'DATA ANALYTIC', 'DATA SCIENCE']
        x_remoto = [dict_1_mes['remoto_e'], dict_1_mes['remoto_a'], dict_1_mes['remoto_s']]
        x_onsite = [dict_1_mes['onsite_e'], dict_1_mes['onsite_a'], dict_1_mes['onsite_s']]
        x_hybrid = [dict_1_mes['hybrid_e'], dict_1_mes['hybrid_a'], dict_1_mes['hybrid_s']]

        # Creamos la figura
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x_remoto, y=y_labels, name='Remoto', marker_color='purple', orientation='h'))
        fig.add_trace(go.Bar(x=x_onsite, y=y_labels, name='Onsite', marker_color='orange', orientation='h'))
        fig.add_trace(go.Bar(x=x_hybrid, y=y_labels, name='Hybrid', marker_color='grey', orientation='h'))

        # Ajustamos la presentación del gráfico
        fig.update_layout(title='Evolución de posiciones en los últimos 6 meses', yaxis_title='Modalidad', xaxis_title='Posiciones')
        fig.update_xaxes(range=[0, 30])
        dict_6_meses = {'DATA ENGINEER': 44, 'DATA ANALYTIC': 26, 'DATA SCIENCE': 12}

        labels = list(dict_6_meses.keys())
        values = list(dict_6_meses.values())

        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

        fig2.update_layout(title='Cantidad de vacantes en 3 meses',
                        annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
      
        # Mostramos el gráfico en Streamlit
        col1,col2= st.columns(2)
        col1.plotly_chart(fig, use_container_width=True)

        col2.plotly_chart(fig2, use_container_width=True)
       
        
        # Preparamos los datos para el gráfico
        y_labels = ['DATA ENGINEER', 'DATA ANALYTIC', 'DATA SCIENCE']
        dict_1_mes = {
            'remoto_e': 2,
            'remoto_a': 5,
            'remoto_s': 1,
            'onsite_e': 3,
            'onsite_a': 7,
            'onsite_s': 2,
            'hybrid_e': 5,
            'hybrid_a': 3,
            'hybrid_s': 2
        }
        
        # Preparamos los datos para el gráfico
        y_labels = ['DATA ENGINEER', 'DATA ANALYTIC', 'DATA SCIENCE']
        x_remoto = [dict_1_mes['remoto_e'], dict_1_mes['remoto_a'], dict_1_mes['remoto_s']]
        x_onsite = [dict_1_mes['onsite_e'], dict_1_mes['onsite_a'], dict_1_mes['onsite_s']]
        x_hybrid = [dict_1_mes['hybrid_e'], dict_1_mes['hybrid_a'], dict_1_mes['hybrid_s']]

        # Creamos la figura
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=x_remoto, y=y_labels, name='Remoto', marker_color='purple', orientation='h'))
        fig1.add_trace(go.Bar(x=x_onsite, y=y_labels, name='Onsite', marker_color='orange', orientation='h'))
        fig1.add_trace(go.Bar(x=x_hybrid, y=y_labels, name='Hybrid', marker_color='grey', orientation='h'))

        # Ajustamos la presentación del gráfico
        fig1.update_layout(title='Evolución de posiciones en los últimos 6 meses', yaxis_title='Modalidad', xaxis_title='Posiciones')
        fig1.update_xaxes(range=[0, 30])
        dict_6_meses = {'DATA ENGINEER': 10, 'DATA ANALYTIC': 15, 'DATA SCIENCE': 5}

        labels = list(dict_6_meses.keys())
        values = list(dict_6_meses.values())

        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

        fig2.update_layout(title='cantidad de vacantes vigentes segun perfil',
                        annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
      
        # Mostramos el gráfico en Streamlit
        col1, col2 =st.columns(2)
        col2.plotly_chart(fig2)
        col1.plotly_chart(fig1)
        


    elif periodo == "seleccione 1 mes":
        with col3:
            st.empty()
            st.metric("BENEFICIO", str("") + " ", delta="+50%", delta_color="normal")
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>CANTIDAD DE POSTULACIONES</h5></p>", unsafe_allow_html=True)
        

        # Definimos los datos
        dict_1_mes = {'remoto_e': 17, 'onsite_e': 20, 'hybrid_e': 4, 'DATA ENGINEER': 37, 'remoto_a': 4, 'onsite_a': 12, 'hybrid_a': 8, 'DATA ANALYTIC': 25, 'remoto_s': 4, 'onsite_s': 1, 'hybrid_s': 4, 'DATA SCIENCE': 12}
        dict_3_meses = {'remoto_e': 24, 'onsite_e': 31, 'hybrid_e': 5, 'DATA ENGINEER': 47, 'remoto_a': 5, 'onsite_a': 18, 'hybrid_a': 12, 'DATA ANALYTIC': 36, 'remoto_s': 5, 'onsite_s': 3, 'hybrid_s': 5, 'DATA SCIENCE': 18}
        dict_6_meses = {'remoto_e': 37, 'onsite_e': 32, 'hybrid_e': 9, 'DATA ENGINEER': 56, 'remoto_a': 9, 'onsite_a': 19, 'hybrid_a': 14, 'DATA ANALYTIC': 37, 'remoto_s': 9, 'onsite_s': 4, 'hybrid_s': 9, 'DATA SCIENCE': 23}

        # Preparamos los datos para el gráfico
        y_labels = ['DATA ENGINEER', 'DATA ANALYTIC', 'DATA SCIENCE']
        x_remoto = [dict_1_mes['remoto_e'], dict_1_mes['remoto_a'], dict_1_mes['remoto_s']]
        x_onsite = [dict_1_mes['onsite_e'], dict_1_mes['onsite_a'], dict_1_mes['onsite_s']]
        x_hybrid = [dict_1_mes['hybrid_e'], dict_1_mes['hybrid_a'], dict_1_mes['hybrid_s']]

        # Creamos la figura
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x_remoto, y=y_labels, name='Remoto', marker_color='purple', orientation='h'))
        fig.add_trace(go.Bar(x=x_onsite, y=y_labels, name='Onsite', marker_color='orange', orientation='h'))
        fig.add_trace(go.Bar(x=x_hybrid, y=y_labels, name='Hybrid', marker_color='grey', orientation='h'))

        # Ajustamos la presentación del gráfico
        fig.update_layout(title='Evolución de posiciones en lo último  mes', yaxis_title='Modalidad', xaxis_title='Posiciones')
        fig.update_xaxes(range=[0, 30])
        # Definimos los datos
        

   
        dict_6_meses = {'DATA ENGINEER': 41, 'DATA ANALYTIC': 24, 'DATA SCIENCE': 9}

        labels = list(dict_6_meses.keys())
        values = list(dict_6_meses.values())

        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

        fig2.update_layout(title='Puestos en los últimos 6 meses',
                        annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
        # Mostramos el gráfico en Streamlit
        col1,col2= st.columns(2)
        col1.plotly_chart(fig, use_container_width=True)

        col2.plotly_chart(fig2)

       
        # Creamos el DataFrame con los datos
        df = pd.DataFrame(dict(
            Perfiles = ["remoto_e", "onsite_e", "hybrid_e","DATA ENGINEER", "remoto_a", "onsite_a", "hybrid_a", "DATA ANALYTIC","remoto_s", "onsite_s", "hybrid_s","DATA SCIENCE"],
            Vacantes_vigentes = [2,3,5,10,5,3,7,15,2,1,2,5 ]))

        # Preparamos los datos para el gráfico
        y_labels = ['DATA ENGINEER', 'DATA ANALYTIC', 'DATA SCIENCE']
        dict_1_mes = {
            'remoto_e': 2,
            'remoto_a': 5,
            'remoto_s': 1,
            'onsite_e': 3,
            'onsite_a': 7,
            'onsite_s': 2,
            'hybrid_e': 5,
            'hybrid_a': 3,
            'hybrid_s': 2
        }
        x_remoto = [dict_1_mes['remoto_e'], dict_1_mes['remoto_a'], dict_1_mes['remoto_s']]
        x_onsite = [dict_1_mes['onsite_e'], dict_1_mes['onsite_a'], dict_1_mes['onsite_s']]
        x_hybrid = [dict_1_mes['hybrid_e'], dict_1_mes['hybrid_a'], dict_1_mes['hybrid_s']]

        # Creamos la figura
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=x_remoto, y=y_labels, name='Remoto', marker_color='purple', orientation='h'))
        fig1.add_trace(go.Bar(x=x_onsite, y=y_labels, name='Onsite', marker_color='orange', orientation='h'))
        fig1.add_trace(go.Bar(x=x_hybrid, y=y_labels, name='Hybrid', marker_color='grey', orientation='h'))

        # Ajustamos la presentación del gráfico
        fig1.update_layout(title='vancantes vigentes segun modalidad', yaxis_title='Modalidad', xaxis_title='Posiciones')
        fig1.update_xaxes(range=[0, 30])
        # Definimos los datos
        dict_6_meses = {'DATA ENGINEER': 10, 'DATA ANALYTIC': 15, 'DATA SCIENCE': 5}

        labels = list(dict_6_meses.keys())
        values = list(dict_6_meses.values())

        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

        fig2.update_layout(title='cantidad de vacantes vigentes segun perfil',
                        annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
      
        # Mostramos el gráfico en Streamlit
        col1, col2 =st.columns(2)
        col2.plotly_chart(fig2)
        col1.plotly_chart(fig1)


        







    
    st.markdown("<div style='text-align: center;'><h1 style='color: #FF8C00;'>TIEMPO PROMEDIO DE CONTRATACIONES</h1></div>", unsafe_allow_html=True)

    st.write('')
    st.write('')
    st.write('')
    st.write('')

    col1, col2, col3  = st.columns(3)


    with col1:
        st.metric("PERIODO", str(postulaciones["6 meses"]) + " MESES", delta_color="inverse")
    
    with col2:
        st.metric("PERIODO", str(postulaciones["3 meses"]) + " MESES", delta_color="inverse")
   
    with col3:
        st.metric("PERIODO", str(postulaciones["1 mes"]) + " MESES", delta_color="inverse")

    

    col1, col2, col3 = st.columns(3)
    periodo = ""

    with st.container():
        col1, col2, col3 = st.columns(3)
        if col1.button("seleccione 6 meses."):
            periodo = "seleccione 6 meses."
        if col2.button("seleccione 3 meses."):
            periodo = "seleccione 3 meses."
        if col3.button("seleccione 1 mes."):
            periodo = "seleccione 1 mes."


    if periodo == "seleccione 6 meses.":
        with col1:
            st.empty()   
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>REDUCCION DEL TIEMPO EN CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.metric("PERIODO", str(postulaciones["6 meses"]) + " MESES", delta=" -0 %", delta_color="normal")

        df= pd.DataFrame(dict(
        Perfiles = 'Tiempo',
        Vacantes_vigentes = [90 ]))

        
        fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles')

        # Establedfcer el rango de medición del eje x
        fig1.update_xaxes(range=[0, 100])

        fig1.update_layout(
            title="TIEMPO PROMEDIO DE CONTRATACION",
            xaxis_title="Periodo en dias",
            yaxis_title="Tiempo",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=170, b=100, l=100, r=10)
        )
        df= pd.DataFrame(dict(
        Perfiles = 'Tiempo',
        Vacantes_vigentes = [40 ]))

        
        fig = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color_discrete_sequence=['lightgreen'])

        # Establedfcer el rango de medición del eje x
        fig.update_xaxes(range=[0, 100])

        fig.update_layout(
            title="TIEMPO PROMEDIO DE CONTRATACION ACTUALMENTE",
            xaxis_title="Periodo en dias",
            yaxis_title="Tiempo",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=170, b=100, l=100, r=10)
        )
        col1, col2 =st.columns(2)
        col1.plotly_chart(fig1)
        col2.plotly_chart(fig)

    elif periodo == "seleccione 3 meses.":
        with col2:
            st.empty()            
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>REDUCCION DEL TIEMPO EN CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.metric("PERIODO", str(postulaciones["3 meses"]) + " MESES", delta=" -22 %", delta_color="normal")

        df= pd.DataFrame(dict(
        Perfiles = 'Tiempo',
        Vacantes_vigentes = [70 ]))

        
        fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles')

        # Establedfcer el rango de medición del eje x
        fig1.update_xaxes(range=[0, 100])

        fig1.update_layout(
            title="TIEMPO PROMEDIO DE CONTRATACION",
            xaxis_title="Periodo en dias",
            yaxis_title="Tiempo",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=170, b=100, l=100, r=10)
        )
        df= pd.DataFrame(dict(
        Perfiles = 'Tiempo',
        Vacantes_vigentes = [40 ]))

        
        fig = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color_discrete_sequence=['lightgreen'])

        # Establedfcer el rango de medición del eje x
        fig.update_xaxes(range=[0, 100])

        fig.update_layout(
            title="TIEMPO PROMEDIO DE CONTRATACION ACTUALMENTE",
            xaxis_title="Periodo en dias",
            yaxis_title="Tiempo",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=170, b=100, l=100, r=10)
        )
        col1, col2 =st.columns(2)
        col1.plotly_chart(fig1)
        col2.plotly_chart(fig)

    elif periodo == "seleccione 1 mes.":
        with col3:
            st.empty()
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>REDUCCION DEL TIEMPO EN CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.metric("PERIODO", str(postulaciones["1 mes"]) + " MESES", delta=" -45 %", delta_color="normal")
        
        df= pd.DataFrame(dict(
        Perfiles = 'Tiempo',
        Vacantes_vigentes = [45 ]))

        
        fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles')

        # Establedfcer el rango de medición del eje x
        fig1.update_xaxes(range=[0, 100])

        fig1.update_layout(
            title="TIEMPO PROMEDIO DE CONTRATACION",
            xaxis_title="Periodo en dias",
            yaxis_title="Tiempo",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=170, b=100, l=100, r=10)
        )
        df= pd.DataFrame(dict(
        Perfiles = 'Tiempo',
        Vacantes_vigentes = [40 ]))

        
        fig = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color_discrete_sequence=['lightgreen'])

        # Establedfcer el rango de medición del eje x
        fig.update_xaxes(range=[0, 100])

        fig.update_layout(
            title="TIEMPO PROMEDIO DE CONTRATACION ACTUALMENTE",
            xaxis_title="Periodo en dias",
            yaxis_title="Tiempo",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=170, b=100, l=100, r=10)
        )
        col1, col2 =st.columns(2)
        col1.plotly_chart(fig1)
        col2.plotly_chart(fig)
     

    




    st.markdown("<div style='text-align: center;'><h1 style='color: #FF8C00;'>COSTO PROMEDIO EN CONTRATACIONES</h1></div>", unsafe_allow_html=True)

    st.write('')
    st.write('')
    st.write('')
    st.write('')

    col1, col2, col3  = st.columns(3)


    with col1:
        st.metric("PERIODO", str(postulaciones["6 meses"]) + " MESES", delta_color="inverse")
    
    with col2:
        st.metric("PERIODO", str(postulaciones["3 meses"]) + " MESES", delta_color="inverse")
   
    with col3:
        st.metric("PERIODO", str(postulaciones["1 mes"]) + " MESES", delta_color="inverse")

    

    col1, col2, col3 = st.columns(3)
 

    with col1:
        st.empty()   
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>REDUCCION EN LOS COSTOS POR CONTRATACION</h5></p>", unsafe_allow_html=True)
        st.metric("COSTO PROMEDIO", str(1000) + " USD", delta=" -0 %", delta_color="normal")

    

    with col2:
        st.empty()            
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>REDUCCION EN LOS COSTOS POR CONTRATACION</h5></p>", unsafe_allow_html=True)
        st.metric("COSTO PROMEDIO ", str(500) + " USD", delta=" -50 %", delta_color="normal")

    

    with col3:
        st.empty()
        st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>REDUCCION EN LOS COSTOS POR CONTRATACION</h5></p>", unsafe_allow_html=True)
        st.metric("COSTO PROMEDIO", str(500) + " USD", delta=" -50 %", delta_color="normal")
        
        

    st.markdown("<div style='text-align: center;'><h1 style='color: #FF8C00;'>EFICIENCIA DEL MODELO DE RECOMENDACIÓN</h1></div>", unsafe_allow_html=True)


    col1, col2, col3  = st.columns(3)


    with col1:
        st.metric("PERIODO", str(postulaciones["6 meses"]) + " MESES", delta_color="inverse")
    
    with col2:
        st.metric("PERIODO", str(postulaciones["3 meses"]) + " MESES", delta_color="inverse")
   
    with col3:
        st.metric("PERIODO", str(postulaciones["1 mes"]) + " MESES", delta_color="inverse")
     # Datos de ejemplo
    aptos_1 = 20
    no_aptos_1 = 80

    aptos_2 = 60
    no_aptos_2 = 20

    aptos_3 = 40
    no_aptos_3 = 2
    
    # Crear primer gráfico de dona
    fig1 = go.Figure(data=[go.Pie(labels=['No Aptos','Aptos', ], 
                                values=[no_aptos_1,aptos_1, ],
                                hole=0.5,
                                marker=dict(colors=[ 'red']))])
    fig1.update_layout(
            title="APTOS VS NO APTOS",
            font=dict(size=14),
            showlegend=False,
            width=600,
            height=450,
            margin=dict(t=50, b=80, l=10, r=200)
        )


    # Crear segundo gráfico de dona
    fig2 = go.Figure(data=[go.Pie(labels=['No Aptos','Aptos',], 
                                values=[no_aptos_2,aptos_2, ],
                                hole=0.5,
                                marker=dict(colors=[ 'red']))])
    fig2.update_layout(
            title="APTOS VS NO APTOS",
            font=dict(size=14),
            showlegend=False,
            width=600,
            height=450,
            margin=dict(t=50, b=80, l=10, r=200)
        )


    # Crear tercer gráfico de dona
    fig3 = go.Figure(data=[go.Pie(labels=['No Aptos','Aptos',], 
                                values=[no_aptos_3,aptos_3, ],
                                hole=0.5,
                                marker=dict(colors=['red']))])
    fig3.update_layout(
            title="APTOS VS NO APTOS",
            font=dict(size=14),
            showlegend=False,
            width=600,
            height=450,
            margin=dict(t=50, b=80, l=10, r=200)
        )

    # Mostrar los gráficos
    col1,col2,col3=st.columns(3)
    col1.plotly_chart(fig1)
    col2.plotly_chart(fig2)
    col3.plotly_chart(fig3)

    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        # Función para normalizar la entrada de texto
elif seleccion == "TalyIA":
    def normalize_input(input_string):
        return re.sub(r'[^\w\s]','',input_string.lower())
    st.image('./IA.jpeg', caption='Caption of your image', use_column_width=True)

    st.markdown("<div style='text-align: center;'><h1 style='color: #FF8C00;'>TALY</h1></div>", unsafe_allow_html=True)        

    st.header('Tu herramienta ideal')
    st.markdown('#### sistema de recomendacion para perfiles del sector data')

    # Crea secciones para cada tipo de entrada de datos
    with st.form(key='my_form'):
        
        # Rango de años de experiencia
        st.header("Rango de años de experiencia")
        experiencia = st.select_slider("Selecciona el rango de años de experiencia que mejor se adapte a tus necesidades:", options=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        # Lenguajes
        st.header("Lenguajes")
        lenguajes = st.radio("Selecciona el lenguaje que prefieras entre los ofrecidos:", options=["Python", "SQL", "R","Java"])

        # Habilidades
        st.header("Habilidades")
        habilidades = st.multiselect("Elige las habilidades que consideres más importantes según el perfil que te interesa:", options=["ETL", "Big Data", "Análisis estadístico", "Visualización de datos", "Data wrangling", "Modelos predictivos", "Cloud Computing", "Arquitectura"])

        # Orientación profesional
        st.header("Orientación profesional")
        orientacion = st.selectbox("Selecciona la orientación profesional que te interesa entre las opciones disponibles:", options=["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"])

        # Idiomas recomendados
        st.header("Idiomas recomendados")
        idiomas = st.multiselect("Elige los idiomas que domines o en los que te sientas más cómodo trabajando:", options=["Inglés", "Español"])

        # Herramientas
        st.header("Herramientas")
        herramientas = st.multiselect("Selecciona las herramientas que tengas experiencia utilizando:", options=["Jupyter Notebook", "Git", "Google Cloud", "Tableau", "PowerBI", "Hadoop", "Spark", "MongoDB", "Apache Airflow", "Apache NiFi", "Grafana", "Looker Studio", "Google Analytics", "QlikView"])

        # Salario mínimo
        st.header("Salario mínimo")
        salario = st.slider("Elige el salario mínimo que te gustaría recibir:", min_value=1000, max_value=15000, step=500)

    
        # Añadimos un botón para ejecutar el código cuando el usuario termine de responder las preguntas
        submit_button = st.form_submit_button(label='Buscar candidato')
        perfiles = {
    "Data Engineer trainee : ": {
        "rango de años de experiencia": range(0,1),
        "lenguajes": ["Python", "SQL"],
        "habilidades": ["ETL", "Big Data"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Git", "Google Cloud"],
        "salario mínimo": [2500, 3000]
    },
        "Data Analyst trainee": {
        "rango de años de experiencia": range(0,1),
        "lenguajes": ["Python", "R", "SQL"],
        "habilidades": ["Análisis estadístico", "Visualización de datos"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI", ],
        "salario mínimo": [2500, 3000]
    },
    "Data Scientist trainee": {
        "rango de años de experiencia": range(0,1),
        "lenguajes": ["Python", "R"],
        "habilidades": ["Análisis de datos", "Estadística"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI", "SQL",],
        "salario mínimo": [2500, 3000]
    },
    "Data Engineer junior": {
        "rango de años de experiencia": range(2,3),
        "lenguajes": ["Python", "SQL"],
        "habilidades": ["ETL", "Big Data", "webscripting"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Hadoop","Git","Spark","MongoDB "],
        "salario mínimo": [3500, 4000]
    },
    "Data Engineer semi-senior": {
        "rango de años de experiencia": range(4, 5),
        "lenguajes": ["Python", "SQL", "Java"],
        "habilidades": ["ETL", "Big Data", "Cloud Computing"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook","Apache Airflow","MongoDB","Spark","Git","Hadoop","Google Cloud",],
        "salario mínimo": [5000, 5500]
    },
    "Data Engineer senior": {
        "rango de años de experiencia": range(6,10),
        "lenguajes": ["Python", "SQL", "Java"],
        "habilidades": ["ETL", "Big Data", "Cloud Computing", "Arquitectura"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Grafana","Apache Airflow","Apache NiFi ","MongoDB","Spark","Git","Hadoop","Google Cloud",],
        "salario mínimo": [8000, 10000]
    },


    "Data Analyst junior": {
        "rango de años de experiencia": range(2,3),
        "lenguajes": ["Python", "R", "SQL"],
        "habilidades": ["Análisis estadístico", "Visualización de datos", "Data wrangling"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI", "Looker Studio","Google Analytics"],
        "salario mínimo": [3500, 4000]
    },
    "Data Analyst semi-senior": {
        "rango de años de experiencia": range(4, 5),
        "lenguajes": ["Python", "R", "SQL"],
        "habilidades": ["Análisis estadístico", "Visualización de datos", "Data wrangling", "Modelos predictivos"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI", "Looker Studio","Google Analytics","QlikView"],
        "salario mínimo": [5000, 5500]
    },
    "Data Analyst senior": {
        "rango de años de experiencia": range(6,10),
        "lenguajes": ["Python", "R", "SQL"],
        "habilidades": ["Análisis estadístico", "Visualización de datos", "Data wrangling", "Modelos predictivos", "Machine learning"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI", "Looker Studio","Google Analytics","QlikView","spaCy","NLTK"],
        "salario mínimo": [8000, 10000]
    },
    "Data Scientist trainee": {
        "rango de años de experiencia": range(0,1),
        "lenguajes": ["Python", "R","SQL"],
        "habilidades": ["Análisis de datos", "Estadística"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI","GitHub"],
        "salario mínimo": [2500, 3000]
    },
    "Data Scientist junior": {
        "rango de años de experiencia": range(2,3),
        "lenguajes": ["Python", "R", "SQL"],
        "habilidades": ["Análisis de datos", "Estadística", "Machine Learning"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI", "MongoDB","Bitbucket","GitHub"],
        "salario mínimo": [3500, 4000]
        
    },
    "Data Scientist semi-senior": {
        "rango de años de experiencia": range(4, 5),
        "lenguajes": ["Python", "R", "SQL"],
        "habilidades": ["Análisis de datos", "Estadística", "Machine Learning", "Visualización de datos"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI", "MongoDB","Bitbucket","GitHub","AWS","Azure"],
        "salario mínimo": [5000, 5500]
    },
    "Data Scientist senior": {
        "rango de años de experiencia": range(6,10),
        "lenguajes": ["Python", "R", "SQL"],
        "habilidades": ["Análisis de datos", "Estadística", "Machine Learning", "Visualización de datos", "Investigación"],
        "orientacion profesional": ["Tecnología", "Ciencias", "Finanzas", "Marketing", "Salud"],
        "idiomas recomendados": ["Inglés", "Español"],
        "herramientas": ["Jupyter Notebook", "Tableau", "PowerBI", "MongoDB","Bitbucket","GitHub","AWS","Azure","SPSS","SAS"],
        "salario mínimo": [8000, 10000]
    }
}
        
        # Validar que el salario sea un número válido
    mejor_match = None
    puntaje_mejor_match = 0
    perfil_similar = None
    puntaje_perfil_similar = 0

    for perfil, detalles in perfiles.items():
        puntaje = 0

        # Comparamos la experiencia
        if experiencia and int(experiencia) in detalles.get("rango de años de experiencia", []):
            puntaje += 1

        # Comparamos los lenguajes
        lenguajes_perfil = normalize_input(" ".join(detalles.get("lenguajes", [])))
        for lenguaje in lenguajes.split():
            if lenguaje in lenguajes_perfil:
                puntaje += 1

        habilidades_perfil = normalize_input(" ".join(detalles.get("habilidades", [])))
        for habilidad in " ".join(habilidades).split():
            if habilidad in habilidades_perfil:
                puntaje += 1

        # Comparamos la orientación profesional
        orientacion_perfil = normalize_input(" ".join(detalles.get("orientacion profesional", [])))
        for area in orientacion.split():
            if area in orientacion_perfil:
                puntaje += 1

        # Comparamos el salario mínimo
        salario_minimo = detalles.get("salario mínimo", [])
        if len(salario_minimo) == 1:
            if int(salario) >= salario_minimo[0]:
                puntaje += 1
        elif len(salario_minimo) == 2:
            if salario_minimo[0] <= int(salario) <= salario_minimo[1]:
                puntaje += 1

        # Actualizamos el mejor match si este puntaje es mayor que el anterior
        if puntaje > puntaje_mejor_match:
            mejor_match = perfil
            puntaje_mejor_match = puntaje
        elif puntaje > puntaje_perfil_similar:
            perfil_similar = perfil
            puntaje_perfil_similar = puntaje
                
    if puntaje_mejor_match == 0:
        # Si no hay ningún perfil que cumpla con los requisitos exactos, usamos el perfil más similar
        st.write(f"No se encontró ningún perfil que cumpla exactamente con los requisitos. Se recomienda el perfil '{perfil_similar}' que tiene {puntaje_perfil_similar} puntos de coincidencia con los requisitos proporcionados.")

    else:
        perfil_recomendado = perfiles[mejor_match]
        st.subheader(f"El perfil recomendado es '{mejor_match}' que cumple con los requisitos proporcionados para el puesto. Este perfil tiene las siguientes características:")
        st.subheader(f"Años de experiencia: {perfil_recomendado['rango de años de experiencia']}")
        st.subheader(f"Lenguajes de programación: {', '.join(perfil_recomendado['lenguajes']).replace('[','').replace(']','').replace('(','').replace(')','')}")
        st.subheader(f"Habilidades: {', '.join(perfil_recomendado['habilidades']).replace('[','').replace(']','').replace('(','').replace(')','')}")
        st.subheader(f"Orientación profesional: {', '.join(perfil_recomendado['orientacion profesional']).replace('[','').replace(']','').replace('(','').replace(')','')}")
        st.subheader(f"Salario mínimo: {', '.join(map(str, perfil_recomendado['salario mínimo'])).replace('[','').replace(']','')}")


# menuu=('Proyecto', 'back end')
# seleccion=st.sidebar.selectbox('Nosotros', menuu )


if seleccion == "Dashboard interno":
  #Definimos la estructura del dashboard
    st.title("SEGUIMIENTO DE SOCIOS")
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    col1,col2 = st.columns(2)

    # Agregamos un título a la columna
    with col1:
        st.header("Seleccione un Socio")
        empresas = ["DataTech", "CodeWorks", "CyberDefenders", "TechSolutions", "CloudMinds"]
        empresa_seleccionada = st.radio("Selecciona una empresa cliente", empresas)

    # Crea una columna en el layout principal
    with col2:
        st.header(f"Información de la **{empresa_seleccionada}**")
        st.write('')
        # Muestra la información de la empresa seleccionada en la columna 2
        if empresa_seleccionada == "DataTech":
            st.markdown("##### Ingreso desde: 20-06-2022")
            st.markdown("##### Ubicación: Silicon Valley, California, EE. UU.")
            st.markdown("##### Industria: soluciones de inteligencia artificial")
            st.markdown("##### Número de empleados: 500")
            
        elif empresa_seleccionada == "CloudMinds":
            st.markdown("##### Ingreso desde: 01-11-2022")
            st.markdown("##### Ubicación: Ciudad de México, México.")
            st.markdown("##### Industria: servicios de nube y almacenamiento en la nube.")
            st.markdown("##### Número de empleados: 250")
        elif empresa_seleccionada == "CodeWorks":
            st.markdown("##### Ingreso desde: 17-09-2022")
            st.markdown("##### Ubicación:  NeoTokio, Japón.")
            st.markdown("##### Industria: desarrollo de software")
            st.markdown("##### Número de empleados: 300")
        elif empresa_seleccionada == "CyberDefenders":
            st.markdown("##### Ingreso desde: 02-11-2022")
            st.markdown("##### Ubicación: São Paulo, Brasil.")
            st.markdown("##### Industria: ciberseguridad")
            st.markdown("##### Número de empleados: 150")
        elif empresa_seleccionada == "TechSolutions":
            st.markdown("##### Ingreso desde: 21-01-2023")
            st.markdown("##### Ubicación: Berlín, Alemania.")
            st.markdown("##### Industria:  desarrollo de software y soluciones tecnológicas.")
            st.markdown("##### Número de empleados: 300")

  # Definimos los KPIs
    ventas_totales = 2000000
    clientes_totales = 500
    promedio_compra = 4000
    tasa_retencion = 0.8
    conversion_visitas = 0.05

    # Creamos los gráficos
    datos_antes = pd.DataFrame({
        "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        "Ventas": [100000, 150000, 200000, 250000, 300000, 350000]
    })
    fig_antes = px.line(datos_antes, x="Meses", y="Ventas", title="Ventas antes de nuestros servicios")

    datos_despues = pd.DataFrame({
        "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        "Ventas": [150000, 200000, 250000, 300000, 350000, 400000]
    })
    fig_despues = px.line(datos_despues, x="Meses", y="Ventas", title="Ventas después de nuestros servicios")


    if empresa_seleccionada == "DataTech":

        col1, col2, col3,col4,col5 = st.columns(5)

        with col1: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>AUMENTO DE LAS CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 1", delta=" -50 %", delta_color="normal")
        with col2: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>ATRACTIVO EN LAS VACANTES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 2", delta=" -50 %", delta_color="normal")
        with col3:
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>PERMANENCIA EN LA EMPRESA</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 3", delta=" -50 %", delta_color="normal")
        with col4: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>TIEMPO DE CONTRATACION</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 4", delta=" -50 %", delta_color="normal")
        with col5:     
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>COSTOS EN CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 5", delta=" -50 %", delta_color="normal")

        
        with st.container():
            col1, col2, col3,col4,col5 = st.columns(5)
            periodo = ""
            if col1.button("selecione1"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
                    "Antes del servicio": [22,40, 50, 63, 50, 51],
                    "Con servicio": [30, 50, 68, 90, 85, 100]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones)         
            if col2.button("selecione2"):
                st.subheader(" cantidad de postulantes a la vacante - cantidad de postulantes con el perfil adecuado/cantidad de postulantes que pasan a ser entrevistados por la empresa")

                dict_6_meses = {'NO APTOS': 66, 'APTOS': 20}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig1 = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig1.update_layout(title='Aspirantes antes del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])

                

                dict_6_meses = {'NO APTOS': 7, 'APTOS': 40}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig.update_layout(title='Aspirantes despues del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
                
                col1,col2=st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig)
              
            
            if col3.button("selecione3"):
                st.subheader("((Número de empleados al final del periodo - Número de empleados que dejaron la empresa durante el periodo) / Número de empleados al inicio del periodo)) x 100")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Marzo", "Mayo","Julio", "Septiembre", "Nobiembre"],
                    "Antes del servicio": [20, 20, 20, 40, 50, 60],
                    "Con servicio": [30, 50, 60, 60, 75, 90]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Medicion de parametros 6 meses en comparacion antes y despues de Taly ")
                st.plotly_chart(fig_contrataciones)
            if col4.button("selecione4"):
                st.subheader("(Número total de días transcurridos en el proceso de contratación) / (Número total de contrataciones)")

                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [10 ]))

                
                fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles')

                # Establedfcer el rango de medición del eje x
                fig1.update_xaxes(range=[0, 100])

                fig1.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [45 ]))

                
                fig = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color_discrete_sequence=['lightgreen'])

                # Establedfcer el rango de medición del eje x
                fig.update_xaxes(range=[0, 100])

                fig.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION ACTUALMENTE",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                col1, col2 =st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig)
            if col5.button("selecione5"):
                st.subheader("(Costo total de contratación) / (Número de nuevos empleados contratados) ")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","julio", "Agosto", "Septiembre","Octubre", "Nobiembre", "Diciembre"],
                    "Antes del servicio": [1000,1200,800, 900,1000,800,900,800,1000,1100,800,700],
                    "Con servicio": [700, 750, 700, 650, 600, 550,540,530,490,490,490,490]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones)   




    elif empresa_seleccionada == "CloudMinds":
        col1, col2, col3,col4,col5 = st.columns(5)

        with col1: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>AUMENTO DE LAS CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 1", delta=" -50 %", delta_color="normal")
        with col2: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>ATRACTIVO EN LAS VACANTES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 2", delta=" -50 %", delta_color="normal")
        with col3:
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>PERMANENCIA EN LA EMPRESA</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 3", delta=" -50 %", delta_color="normal")
        with col4: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>TIEMPO DE CONTRATACION</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 4", delta=" -50 %", delta_color="normal")
        with col5:     
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>COSTOS EN CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 5", delta=" -50 %", delta_color="normal")

        
        with st.container():
            col1, col2, col3,col4,col5 = st.columns(5)
            periodo=""
            if col1.button("selecione1"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
                    "Antes del servicio": [6,12,17, 17, 12,15],
                    "Con servicio": [12, 14, 16, 25, 33, 48]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones)         
            if col2.button("selecione2"):
                dict_6_meses = {'NO APTOS': 100, 'APTOS': 33}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig1 = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig1.update_layout(title='Aspirantes antes del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])

                

                dict_6_meses = {'NO APTOS': 5, 'APTOS': 30}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig.update_layout(title='Aspirantes despues del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
                
                col1,col2=st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig) 
            if col3.button("selecione3"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Marzo", "Mayo","Julio", "Septiembre", "Nobiembre"],
                    "Antes del servicio": [10, 20, 20, 30, 20, 60],
                    "Con servicio": [10, 20, 40, 50, 90, 120]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Medicion de parametros 6 meses en comparacion antes y despues de Taly ")
                st.plotly_chart(fig_contrataciones)
            if col4.button("selecione4"):
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [120 ]))

                
                fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles')

                # Establedfcer el rango de medición del eje x
                fig1.update_xaxes(range=[0, 100])

                fig1.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [50 ]))

                
                fig = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color_discrete_sequence=['lightgreen'])

                # Establedfcer el rango de medición del eje x
                fig.update_xaxes(range=[0, 100])

                fig.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION ACTUALMENTE",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                col1, col2 =st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig)
            if col5.button("selecione5"):
                st.subheader("(Costo total de contratación) / (Número de nuevos empleados contratados) ")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","julio", "Agosto", "Septiembre","Octubre", "Nobiembre", "Diciembre"],
                    "Antes del servicio": [1000,1200,800, 900,1000,800,900,800,1000,1100,800,700],
                    "Con servicio": [700, 750, 700, 650, 600, 550,540,530,490,490,490,490]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones)



    elif empresa_seleccionada == "CodeWorks":

        col1, col2, col3,col4,col5 = st.columns(5)

        with col1: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>AUMENTO DE LAS CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 1", delta=" -50 %", delta_color="normal")
        with col2: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>ATRACTIVO EN LAS VACANTES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 2", delta=" -50 %", delta_color="normal")
        with col3:
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>PERMANENCIA EN LA EMPRESA</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 3", delta=" -50 %", delta_color="normal")
        with col4: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>TIEMPO DE CONTRATACION</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 4", delta=" -50 %", delta_color="normal")
        with col5:     
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>COSTOS EN CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 5", delta=" -50 %", delta_color="normal")

        
        with st.container():
            col1, col2, col3,col4,col5 = st.columns(5)
            periodo=""
            if col1.button("selecione1"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
                    "Antes del servicio": [22,12,17, 16, 12,15],
                    "Con servicio": [23, 25, 33, 35, 30, 44]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones) 
            if col2.button("selecione2"):
                dict_6_meses = {'NO APTOS': 60, 'APTOS': 20}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig1 = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig1.update_layout(title='Aspirantes antes del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])

                

                dict_6_meses = {'NO APTOS': 7, 'APTOS': 40}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig.update_layout(title='Aspirantes despues del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
                
                col1,col2=st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig) 
            if col3.button("selecione3"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Marzo", "Mayo","Julio", "Septiembre", "Nobiembre"],
                    "Antes del servicio": [20, 20, 20, 30, 40, 60],
                    "Con servicio": [30, 50, 55, 70, 90, 120]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Medicion de parametros 6 meses en comparacion antes y despues de Taly ")
                st.plotly_chart(fig_contrataciones)
            if col4.button("selecione4"):
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [95 ]))

                
                fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles')

                # Establedfcer el rango de medición del eje x
                fig1.update_xaxes(range=[0, 100])

                fig1.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [50 ]))

                
                fig = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color_discrete_sequence=['lightgreen'])

                # Establedfcer el rango de medición del eje x
                fig.update_xaxes(range=[0, 100])

                fig.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION ACTUALMENTE",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                col1, col2 =st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig)
            if col5.button("selecione5"):
                st.subheader("(Costo total de contratación) / (Número de nuevos empleados contratados) ")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","julio", "Agosto", "Septiembre","Octubre", "Nobiembre", "Diciembre"],
                    "Antes del servicio": [800, 960, 640, 720, 800, 640, 720, 640, 800, 880, 640, 560],
                    "Con servicio": [560, 600, 560, 520, 480, 440, 432, 424, 392, 392, 392, 392]
                    })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones)




    elif empresa_seleccionada == "CyberDefenders":
        col1, col2, col3,col4,col5 = st.columns(5)

        with col1: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>AUMENTO DE LAS CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 1", delta=" -50 %", delta_color="normal")
        with col2: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>ATRACTIVO EN LAS VACANTES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 2", delta=" -50 %", delta_color="normal")
        with col3:
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>PERMANENCIA EN LA EMPRESA</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 3", delta=" -50 %", delta_color="normal")
        with col4: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>TIEMPO DE CONTRATACION</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 4", delta=" -50 %", delta_color="normal")
        with col5:     
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>COSTOS EN CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 5", delta=" -50 %", delta_color="normal")

        
        with st.container():
            col1, col2, col3,col4,col5 = st.columns(5)
            periodo=""
            if col1.button("selecione1"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
                    "Antes del servicio": [50, 50, 44, 33, 40, 35],
                    "Con servicio": [33, 44, 52, 66, 63, 68]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones) 
            if col2.button("selecione2"):
                dict_6_meses = {'NO APTOS': 100, 'APTOS': 300}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig1 = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig1.update_layout(title='Aspirantes antes del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])

                

                dict_6_meses = {'NO APTOS': 7, 'APTOS': 60}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig.update_layout(title='Aspirantes despues del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
                
                col1,col2=st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig)
            if col3.button("selecione3"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Marzo", "Mayo","Julio", "Septiembre", "Nobiembre"],
                    "Antes del servicio": [20, 20, 40, 60, 60, 65],
                    "Con servicio": [30, 50, 50, 60, 80, 100]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Medicion de parametros 6 meses en comparacion antes y despues de Taly ")
                st.plotly_chart(fig_contrataciones)
            if col4.button("selecione4"):
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [100 ]))

                
                fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles')

                # Establedfcer el rango de medición del eje x
                fig1.update_xaxes(range=[0, 100])

                fig1.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [45 ]))

                
                fig = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color_discrete_sequence=['lightgreen'])

                # Establedfcer el rango de medición del eje x
                fig.update_xaxes(range=[0, 100])

                fig.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION ACTUALMENTE",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                col1, col2 =st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig)
            if col5.button("selecione5"):
                st.subheader("(Costo total de contratación) / (Número de nuevos empleados contratados) ")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","julio", "Agosto", "Septiembre","Octubre", "Nobiembre", "Diciembre"],
                    "Antes del servicio": [1000,1200,800, 900,1000,800,900,800,1000,1100,800,700],
                    "Con servicio": [700, 750, 700, 650, 600, 550,540,530,490,490,490,490]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones)



    elif empresa_seleccionada == "TechSolutions":
        col1, col2, col3,col4,col5 = st.columns(5)

        with col1: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>AUMENTO DE LAS CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 1", delta=" -50 %", delta_color="normal")
        with col2: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>ATRACTIVO EN LAS VACANTES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 2", delta=" -50 %", delta_color="normal")
        with col3:
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>PERMANENCIA EN LA EMPRESA</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 3", delta=" -50 %", delta_color="normal")
        with col4: 
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>TIEMPO DE CONTRATACION</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 4", delta=" -50 %", delta_color="normal")
        with col5:     
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>COSTOS EN CONTRATACIONES</h5></p>", unsafe_allow_html=True)
            st.empty()
            st.metric("", str('KPI') + " 5", delta=" -50 %", delta_color="normal")

        
        with st.container():
            col1, col2, col3,col4,col5 = st.columns(5)
            periodo=""
            if col1.button("selecione1"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
                    "Antes del servicio": [2, 1, 2, 3, 2, 2],
                    "Con servicio": [3, 5, 5, 6, 8, 10]
                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Medicion de parametros 6 meses en comparacion antes y despues de Taly ")
                st.plotly_chart(fig_contrataciones) 
            if col2.button("selecione2"):
                dict_6_meses = {'NO APTOS': 80, 'APTOS': 20}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig1 = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig1.update_layout(title='Aspirantes antes del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])

                

                dict_6_meses = {'NO APTOS': 5, 'APTOS': 35}

                labels = list(dict_6_meses.keys())
                values = list(dict_6_meses.values())

                fig = go.Figure(data=[go.Pie(labels=labels, 
                                            values=values, 
                                            hole=0.5, 
                                            marker=dict(colors=['red']))])

                fig.update_layout(title='Aspirantes despues del Modelo Taly', 
                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])
                
                col1,col2=st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig)
            if col3.button("selecione3"):
                st.subheader("Contrataciones antes del servicio - Contrataciones actuales con servicio = Beneficio de servicio en contrataciones")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Marzo", "Mayo","Julio", "Septiembre", "Nobiembre"],
                    "Antes del servicio": [20, 40, 60, 60, 66, 70],
                    "Con servicio": [30, 50, 50, 60, 80, 100]
                })

                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Medicion de parametros 6 meses en comparacion antes y despues de Taly ")
                st.plotly_chart(fig_contrataciones)
            if col4.button("selecione4"):
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [85 ]))

                
                fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles')

                # Establedfcer el rango de medición del eje x
                fig1.update_xaxes(range=[0, 100])

                fig1.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                df= pd.DataFrame(dict(
                Perfiles = 'Tiempo',
                Vacantes_vigentes = [30 ]))

                
                fig = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color_discrete_sequence=['lightgreen'])

                # Establedfcer el rango de medición del eje x
                fig.update_xaxes(range=[0, 100])

                fig.update_layout(
                    title="TIEMPO PROMEDIO DE CONTRATACION ACTUALMENTE",
                    xaxis_title="Periodo en dias",
                    yaxis_title="Tiempo",
                    font=dict(size=14),
                    showlegend=False,
                    width=500,
                    height=350,
                    margin=dict(t=170, b=100, l=100, r=10)
                )
                col1, col2 =st.columns(2)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig)
            if col5.button("selecione5"):
                st.subheader("(Costo total de contratación) / (Número de nuevos empleados contratados) ")
                # Aquí se puede agregar el código para generar y mostrar el gráfico
                df_contrataciones = pd.DataFrame({
                    "Meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","julio", "Agosto", "Septiembre","Octubre", "Nobiembre", "Diciembre"],
                    "Antes del servicio": [900, 1080, 720, 810, 900, 720, 810, 720, 900, 990, 720, 630],
                    "Con servicio": [700, 750, 700, 650, 600, 550, 540, 530, 490, 490, 490, 490]
            

                })
                fig_contrataciones = px.line(df_contrataciones, x="Meses", y=["Antes del servicio", "Con servicio"], title="Comparación de contrataciones")
                st.plotly_chart(fig_contrataciones)
    

       

    
if seleccion == "Back End":
    st.title('EL DETRAS DE ESCENA.')
    st.header('Te contamos como inicio Taly')
    st.markdown('#### El rubro de los datos se ha convertido en un sector cada vez más importante en el mercado laboral. Con la explosión del big data y la inteligencia artificial, las oportunidades laborales en este campo se han multiplicado en los últimos años. Una de las tendencias más importantes es la demanda de profesionales altamente capacitados en áreas como la ciencia de datos, la minería de datos y la analítica de datos. Las corporaciones buscan personas con habilidades técnicas en programación, estadísticas y matemáticas, así como con habilidades interpersonales para comunicar los resultados de sus análisis a las partes interesadas. Sin embargo, hay un gran déficit de profesionales de este sector, lo cual es un gran problema…') 
    st.markdown('#### Para esto, vamos a analizar la tendencia de las ofertas laborales en el sector de datos y calcular el porcentaje de incremento que se ha dado en los últimos años. Cada empresa establece los requisitos para cada puesto y a veces solicitan apoyo de profesionales externos para llevar a cabos los procesos de reclutamiento y selección. ')
    st.markdown('#### Es en esa situación que, como consultora de recursos humanos, podemos ofrecer nuestros servicios para estandarizar las ofertas de empleo para poder encontrar el personal adecuado del área de los datos. ')
    st.markdown('### ¿Qué hicimos? ')
    st.markdown('#### Buscamos vacantes laborales del área de datos en Linkedin, la fuente de empleos más importante en el rubro IT. Realizamos scraping para obtener las publicaciones sobre los puestos de data analytics, data engineer y data science. ')
    st.markdown('#### También descargamos un csv de Sysarmy, el cual reflejaba las remuneraciones de diversos puestos IT.')
    st.markdown('#### Realizamos ETL para transformar los títulos de las columnas y extraer de éstas, la información para hacer nuevas columnas. Decidimos no imputar las filas vacías ya que pertenecían a columnas que no aportaban información para nuestro posterior análisis. Borramos los datos duplicados para no sesgar los resultados. ')
    st.markdown('#### Luego realizamos el EDA, donde pudimos concluir que las variables importantes para nuestro análisis serían “localidad” y “modalidad”. ')
    st.markdown('#### Utilizamos Pandas, Numpy y Seaborn para el ETL y EDA. Luego Google cloud para el almacenamiento y Prefect para la automatización y el sistema de recomendación. Finalmente, hicimos el deploy en Streamlit, para mostrar la página web de nuestra empresa. ')


    st.header('HERRAMIENTAS UTILIZADAS')
    st.image('./bacck.png', caption='Caption of your image', use_column_width=True)
    st.title('GSP')
    st.subheader('GSP es una solución de búsqueda empresarial de Google que proporciona herramientas para mejorar la calidad de la búsqueda en sitios web, aplicaciones y otros tipos de contenido')
    st.image('./imagencloud.jpeg', caption='Caption of your image', use_column_width=True)

    st.title('PREFECT')
    st.subheader('Prefect es una plataforma de flujo de trabajo de datos de código abierto que se utiliza para automatizar tareas y procesos en el mundo de la ciencia de datos y el aprendizaje automático. Prefect proporciona una API intuitiva para definir y ejecutar flujos de trabajo, y también ofrece integraciones con servicios en la nube como AWS, GCP y Azure. Con Prefect, los usuarios pueden crear flujos de trabajo complejos que orquestren tareas en sistemas distribuidos con alta escalabilidad y fiabilidad.')
    st.title('PYTHON')
    st.subheader('Python es un lenguaje de programación de alto nivel, interpretado y orientado a objetos. Es fácil de leer y escribir gracias a su sintaxis simple y clara. Se utiliza para una amplia gama de aplicaciones, como desarrollo web, análisis de datos, inteligencia artificial y automatización de tareas. Además, es una de las opciones más populares para la enseñanza de programación debido a su facilidad de uso y amplia comunidad de apoyo.')
    st.title('STREAMLIT')
    st.subheader('Streamlit es una biblioteca de Python de código abierto que permite a los usuarios crear aplicaciones web interactivas y personalizadas para visualizar y compartir datos y modelos de aprendizaje automático. Con Streamlit, los desarrolladores pueden crear aplicaciones en pocos minutos utilizando herramientas familiares de Python y una sintaxis simple. Streamlit proporciona una forma rápida y fácil de prototipar y compartir aplicaciones interactivas en la web.')


    st.title('PROCESO Y MANOS EN OBRA')
    st.image('./flujo.jpeg', caption='Caption of your image', use_column_width=True)
    st.subheader('Se comenzó obteniendo datos de diversas fuentes, incluyendo una práctica llamada web scraping para obtener datos de ofertas laborales de LinkedIn, siendo esta una de las fuentes principales. Luego, se almacenaron todos los datos en la nube de GCS. Posteriormente, se creó un flujo de trabajo con Prefect para que el proceso de ETL se realizara de manera automatizada, leyendo los datos directamente desde la nube sin necesidad de descargarlos en nuestros equipos locales. De esta forma, se automatizó el proceso de limpieza y transformación de los archivos según nuestras necesidades para su posterior consumo en nuestros análisis y sistemas de recomendación. Esto nos permitió tener un mejor entendimiento de los datos y un consumo más eficiente de nuestras fuentes..')

elif seleccion == "Contactanos":
    st.subheader('tusociotaly@talentia.com')
    st.subheader('Tel:01145654585')