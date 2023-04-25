import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from plotly.subplots import make_subplots
from streamlit_folium import folium_static

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
menu=('Incio', 'Dashboard', 'TalyIA','Contactos')
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
    st.markdown('##### En un mercado laboral cada vez más competitivo, es esencial contar con el equipo adecuado que pueda llevar a su empresa o reclutadora al éxito. En nuestra consultora de recursos humanos, nos apasiona la innovación y la excelencia en todo lo que hacemos. Con más de XX años de experiencia en la industria, nuestro equipo de expertos en recursos humanos ha ayudado a innumerables clientes a superar los desafíos de contratación más difíciles, desde la disminución en las contrataciones deseadas hasta los altos costos de contratación.')
    st.markdown('##### Nos enorgullece brindar soluciones únicas y personalizadas que superan las expectativas de nuestros clientes. Somos innovadores y estamos a la vanguardia de las últimas tendencias y tecnologías de la industria, lo que nos permite ofrecer un servicio de alta calidad y personalizado para cada cliente.')
    st.markdown('##### Además, nos comprometemos a brindar soluciones efectivas y únicas. Contamos con una amplia red de contactos y un sistema avanzado de recomendación que nos permite encontrar a los candidatos adecuados para cada puesto y ayudar a nuestros clientes a tomar decisiones de contratación informadas y acertadas.')
    st.markdown('##### Confíe en nosotros para brindarle soluciones de recursos humanos únicas y efectivas que lo ayuden a superar los desafíos de contratación más difíciles y a encontrar al candidato perfecto para cada puesto. En nuestra consultora, nos apasiona la excelencia y estamos dedicados a ayudar a nuestros clientes a alcanzar el éxito en un mercado laboral cada vez más competitivo.')
    
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
            st.metric("PERIODO", str(postulaciones["6 meses"]) + " MESES", delta=" (+0%)", delta_color="normal")
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>CANTIDAD DE POSTULACIONES</h5></p>", unsafe_allow_html=True)

        color_map = {"remoto_e": "red", "onsite_e": "lightgreen", "hybrid_e": "lightblue",
             "DATA ENGINEER": "blue", "remoto_a": "red", "onsite_a": "lightgreen",
             "hybrid_a": "lightblue", "DATA ANALYTIC": "blue", "remoto_s": "red",
             "onsite_s": "lightgreen", "hybrid_s": "lightblue", "DATA SCIENCE": "blue"}


        dict_6_meses = {
            "remoto_e": 40,
            "onsite_e": 35,
            "hybrid_e": 10,
            "DATA ENGINEER": 60,
            "remoto_a": 10,
            "onsite_a": 20,
            "hybrid_a": 15,
            "DATA ANALYTIC": 40,
            "remoto_s": 10,
            "onsite_s": 5,
            "hybrid_s": 10,
            "DATA SCIENCE": 25
        }

        # Convertir el diccionario en un DataFrame de pandas
        df = pd.DataFrame.from_dict(dict_6_meses, orient='index', columns=['Vacantes_cubiertas'])

        # Agregar la columna de perfiles
        df['Perfiles'] = df.index

        # Calcular el porcentaje de crecimiento desde los 6 meses hasta la actualidad
        df['Crecimiento'] = (df['Vacantes_cubiertas'] * 1.2) / df.loc['DATA ENGINEER', 'Vacantes_cubiertas']

        # Graficar los datos
        fig = px.bar(df, x='Vacantes_cubiertas', y='Perfiles', color='Perfiles', color_discrete_map=color_map)

        # Establecer el rango de medición del eje x
        fig.update_xaxes(range=[0, 80])

        fig.update_layout(
            title="VACANTES CUBIERTAS",
            xaxis_title="Vacantes cubiertas",
            yaxis_title="Perfiles Data",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=25, b=100, l=100, r=10)
        )

        
        df = pd.DataFrame(dict(
            Perfiles = ["remoto_e", "onsite_e", "hybrid_e","DATA ENGINEER", "remoto_a", "onsite_a", "hybrid_a", "DATA ANALYTIC","remoto_s", "onsite_s", "hybrid_s","DATA SCIENCE"],
            Vacantes_vigentes = [2,3,5,10,5,3,7,15,2,1,2,5 ]))

      
        fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color='Perfiles', color_discrete_map=color_map)

        # Establecer el rango de medición del eje x
        fig1.update_xaxes(range=[0, 60])

        fig1.update_layout(
            title="VACANTES VIGENTES",
            xaxis_title="Vacantes vigentes",
            yaxis_title="Perfiles Data",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=25, b=100, l=100, r=10)
        )

        col1, col2 =st.columns(2)
        col1.plotly_chart(fig)
        col2.plotly_chart(fig1)

    elif periodo == "seleccione 3 meses":
        with col2:
            st.empty()
            st.metric("PERIODO", str(postulaciones["3 meses"]) + " MESES", delta=" (+30%)", delta_color="normal")
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>CANTIDAD DE POSTULACIONES</h5></p>", unsafe_allow_html=True)

        color_map = {"remoto_e": "red", "onsite_e": "lightgreen", "hybrid_e": "lightblue",
             "DATA ENGINEER": "blue", "remoto_a": "red", "onsite_a": "lightgreen",
             "hybrid_a": "lightblue", "DATA ANALYTIC": "blue", "remoto_s": "red",
             "onsite_s": "lightgreen", "hybrid_s": "lightblue", "DATA SCIENCE": "blue"}


        dict_3_meses = {
            'remoto_e': 26,
            'onsite_e': 33,
            'hybrid_e': 6,
            'DATA ENGINEER': 50,
            'remoto_a': 6,
            'onsite_a': 19,
            'hybrid_a': 13,
            'DATA ANALYTIC': 39,
            'remoto_s': 6,
            'onsite_s': 3,
            'hybrid_s': 6,
            'DATA SCIENCE': 19}

        # Convertir el diccionario en un DataFrame de pandas
        df = pd.DataFrame.from_dict(dict_3_meses, orient='index', columns=['Vacantes_cubiertas'])

        # Agregar la columna de perfiles
        df['Perfiles'] = df.index

        # Calcular el porcentaje de crecimiento desde los 6 meses hasta la actualidad
        df['Crecimiento'] = (df['Vacantes_cubiertas'] * 1.2) / df.loc['DATA ENGINEER', 'Vacantes_cubiertas']

        # Graficar los datos
        fig = px.bar(df, x='Vacantes_cubiertas', y='Perfiles', color='Perfiles', color_discrete_map=color_map)

        # Establecer el rango de medición del eje x
        fig.update_xaxes(range=[0, 80])

        fig.update_layout(
            title="VACANTES CUBIERTAS",
            xaxis_title="Vacantes cubiertas",
            yaxis_title="Perfiles Data",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=25, b=100, l=100, r=10)
        )

       
        df = pd.DataFrame(dict(
            Perfiles = ["remoto_e", "onsite_e", "hybrid_e","DATA ENGINEER", "remoto_a", "onsite_a", "hybrid_a", "DATA ANALYTIC","remoto_s", "onsite_s", "hybrid_s","DATA SCIENCE"],
            Vacantes_vigentes = [2,3,5,10,5,3,7,15,2,1,2,5 ]))

      
        fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color='Perfiles', color_discrete_map=color_map)

        # Establecer el rango de medición del eje x
        fig1.update_xaxes(range=[0, 60])

        fig1.update_layout(
            title="VACANTES VIGENTES",
            xaxis_title="Vacantes vigentes",
            yaxis_title="Perfiles Data",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=25, b=100, l=100, r=10)
        )

        col1, col2 =st.columns(2)
        col1.plotly_chart(fig)
        col2.plotly_chart(fig1)


    elif periodo == "seleccione 1 mes":
        with col3:
            st.empty()
            st.metric("PERIODO", str(postulaciones["1 mes"]) + " MESES", delta=" (+50%)", delta_color="normal")
            st.markdown("<p style='font-size: 18px; font-weight: bold;'><h5>CANTIDAD DE POSTULACIONES</h5></p>", unsafe_allow_html=True)
        

        color_map = {"remoto_e": "red", "onsite_e": "lightgreen", "hybrid_e": "lightblue",
             "DATA ENGINEER": "blue", "remoto_a": "red", "onsite_a": "lightgreen",
             "hybrid_a": "lightblue", "DATA ANALYTIC": "blue", "remoto_s": "red",
             "onsite_s": "lightgreen", "hybrid_s": "lightblue", "DATA SCIENCE": "blue"}



        dict_1_mes = {
            'remoto_e': 18,
            'onsite_e': 22,
            'hybrid_e': 4,
            'DATA ENGINEER': 40,
            'remoto_a': 4,
            'onsite_a': 13,
            'hybrid_a': 9,
            'DATA ANALYTIC': 27,
            'remoto_s': 4,
            'onsite_s': 2,
            'hybrid_s': 4,
            'DATA SCIENCE': 13}
        

        # Convertir el diccionario en un DataFrame de pandas
        df = pd.DataFrame.from_dict(dict_1_mes, orient='index', columns=['Vacantes_cubiertas'])

        # Agregar la columna de perfiles
        df['Perfiles'] = df.index

        # Calcular el porcentaje de crecimiento desde los 6 meses hasta la actualidad
        df['Crecimiento'] = (df['Vacantes_cubiertas'] * 1.2) / df.loc['DATA ENGINEER', 'Vacantes_cubiertas']

        # Graficar los datos
        fig = px.bar(df, x='Vacantes_cubiertas', y='Perfiles', color='Perfiles', color_discrete_map=color_map)

        # Establecer el rango de medición del eje x
        fig.update_xaxes(range=[0, 80])

        fig.update_layout(
            title="VACANTES CUBIERTAS",
            xaxis_title="Vacantes cubiertas",
            yaxis_title="Perfiles Data",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=25, b=100, l=100, r=10)
        )

       
        df = pd.DataFrame(dict(
            Perfiles = ["remoto_e", "onsite_e", "hybrid_e","DATA ENGINEER", "remoto_a", "onsite_a", "hybrid_a", "DATA ANALYTIC","remoto_s", "onsite_s", "hybrid_s","DATA SCIENCE"],
            Vacantes_vigentes = [2,3,5,10,5,3,7,15,2,1,2,5 ]))

      
        fig1 = px.bar(df, x='Vacantes_vigentes', y='Perfiles', color='Perfiles', color_discrete_map=color_map)

        # Establecer el rango de medición del eje x
        fig1.update_xaxes(range=[0, 60])

        fig1.update_layout(
            title="VACANTES VIGENTES",
            xaxis_title="Vacantes vigentes",
            yaxis_title="Perfiles Data",
            font=dict(size=14),
            showlegend=False,
            width=500,
            height=350,
            margin=dict(t=25, b=100, l=100, r=10)
        )

        col1, col2 =st.columns(2)
        col1.plotly_chart(fig)
        col2.plotly_chart(fig1)

    
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
        
        

    st.markdown("<div style='text-align: center;'><h1 style='color: #FF8C00;'>EFICIENCIA DEL MODELO DE REOMENDACIÓN</h1></div>", unsafe_allow_html=True)


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
    no_aptos_2 = 40

    aptos_3 = 40
    no_aptos_3 = 35

    
    # Crear primer gráfico de dona
    fig1 = go.Figure(data=[go.Pie(labels=['No Aptos','Aptos', ], 
                                values=[aptos_1, no_aptos_1],
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
                                values=[aptos_2, no_aptos_2],
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
                                values=[aptos_3, no_aptos_3],
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

else:
    st.write("Sistema de recomendacion")

menuu=('Proyecto', 'back end')
seleccion=st.sidebar.selectbox('Nosotros', menuu )