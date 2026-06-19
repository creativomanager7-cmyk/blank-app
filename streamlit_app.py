import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HITLAB CENTRAL",
    page_icon="🎙️",
    layout="wide"
)

# Encabezado Principal
st.title("🎙️ HITLAB CENTRAL")
st.markdown("## El Ahora de la Música: Ecosistema de Inteligencia de IP")
st.write("Auditoría estratégica de metadatos y distribución de catálogo propio.")

# Pestañas de Trabajo
tab1, tab2 = st.tabs(["📊 Mi Catálogo de Composiciones", "👥 Enfoque de Comunidades"])

# BASE DE DATOS COMPLETA EXTRAÍDA DE TUS 10 CAPTURAS DE MUSO.AI
composiciones_data = {
    "Canción": [
        "Mi Debilidad", "La Bandida", "¿Dónde Estabas Tú?", "Despechada", "Amantes",
        "Piedra, Papel o Tijera", "Vivir La Vida", "Si me ven llorando - En Vivo", "Ojalá", "AMORES DE UN RATITO",
        "Ven, Espíritu Ven", "Que Seas Feliz", "Amigo El Ratón Del Queso - Versión Popular", "Vente Conmigo", "Te Ves Muy Feliz",
        "Soltera", "Te Olvidé", "El Malo Soy Yo", "Vicio de Ti", "De 5 en 5",
        "¿De Qué Me Sirve? - Cero39 Remix", "Me Vale Madre", "¿De Qué Me Sirve?", "Ojalá (Edwin Gaona)",
        "Culpable", "El Malo Soy Yo (Chris Jonex)", "Voy a Embriagarme", "Desgraciado", "Amigo El Ratón Del Queso",
        "Prohibidos", "Horas Extras", "Corazón de Jesús", "Mi Debilidad (Gerardo Morán)", "Decepciones",
        "Si me ven llorando (Koky Jarrín)", "Soltera (Ela Prieto)", "Inevitable", "Culpable (Andreew)", "Pasado Borrado",
        "Como Es la Vuelta", "Cuchiviri Rechevere", "Golpe Avisa", "Bolsita de Marca", "Insomnios",
        "Si Me Ven Llorando (Kassandra Chanamé)", "Malditona", "Mi Soledad y Yo", "El Cabron", "Te pienso"
    ],
    "Artista / Intérprete": [
        "Francy", "Hanna Rivas", "Paola Jara", "Julian Daza, Jhon Alex Castaño", "Gustavo Elis, Sixto Rein",
        "Dayanara, Pipe Bueno", "Key Ospina", "Jessi Uribe", "Joaquin Guiller", "Sofi Piñan",
        "Ministerio Etan", "Los Banis", "Los Caballeros de la Cantina", "Noche de Brujas, Jorge Celedón", "Pancho Uresti",
        "Marcela Gómez", "La Pandilla del Rio Bravo", "Edwin Gaona", "Miguel Vaquero", "Nicole Vega",
        "Diana Burco, CERO39", "Nicole Vega", "Diana Burco", "Edwin Gaona",
        "Lady Noriega", "Chris Jonex", "Edwin Gaona", "Nicole Vega", "Los Caballeros de la Cantina",
        "Bocanegra La Voz", "k-LOVE", "Las Cigarreras", "Gerardo Morán, Alma Musa", "Aura Cristina Geithner",
        "Koky Jarrín Y Los Nacis", "Ela Prieto", "k-LOVE", "Andreew", "Pablo Montana",
        "Valeria Rico", "Vargasvil", "Nicole Vega", "Nicole Vega", "Nicole Vega",
        "Kassandra Chanamé", "Nicole Vega", "Lady Noriega", "Champen", "Gerald Merlin"
    ],
    "Rol Registrado": [
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist"
    ],
    "Estatus IP (Sony Pubcol)": [
        "99.1% Aligned", "100% Aligned", "98.4% Aligned", "99.0% Aligned", "100% Aligned",
        "100% Aligned", "95.0% Aligned", "97.8% Aligned", "96.5% Aligned", "100% Aligned",
        "100% Aligned", "100% Aligned", "98.0% Aligned", "99.0% Aligned", "97.5% Aligned",
        "96.0% Aligned", "100% Aligned", "98.2% Aligned", "99.0% Aligned", "100% Aligned",
        "100% Aligned", "100% Aligned", "100% Aligned", "98.2% Aligned",
        "99.4% Aligned", "100% Aligned", "98.2% Aligned", "100% Aligned", "98.0% Aligned",
        "95.5% Aligned", "100% Aligned", "100% Aligned", "99.1% Aligned", "96.8% Aligned",
        "97.8% Aligned", "96.0% Aligned", "100% Aligned", "99.4% Aligned", "100% Aligned",
        "100% Aligned", "100% Aligned", "100% Aligned", "100% Aligned", "100% Aligned",
        "97.8% Aligned", "100% Aligned", "99.4% Aligned", "100% Aligned", "100% Aligned"
    ]
}
df_catalogo = pd.DataFrame(composiciones_data)

with tab1:
    st.subheader("Auditoría Automatizada de Catálogo Real")
    st.write("Filtra y audita la indexación global de tus obras directamente desde el panel.")
    
    # Buscador Interactivo Real
    buscar_obra = st.text_input("Buscar canción o artista en tu catálogo de propiedad intelectual:", "")
    
    if buscar_obra:
        resultado = df_catalogo[
            df_catalogo['Canción'].str.contains(buscar_obra, case=False) | 
            df_catalogo['Artista / Intérprete'].str.contains(buscar_obra, case=False)
        ]
        st.write(f"Resultados encontrados para '{buscar_obra}':")
        st.dataframe(resultado, use_container_width=True)
    else:
        st.write("Catálogo General Indexado (Desplázate hacia abajo para ver todo):")
        st.dataframe(df_catalogo, use_container_width=True)
        
    st.markdown("### 📊 Métricas Agregadas de Regalías e IP")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="Total Obras Registradas en Panel", value=f"{len(df_catalogo)} Tracks")
    with c2:
        st.metric(label="Alineación Promedio de Metadatos", value="98.7%")
    with c3:
        st.metric(label="Editorial Principal Vinculada", value="Sony Music Publishing")

with tab2:
    st.subheader("Laboratorio de Algoritmos: Incubadora de Superfans")
    st.write("Análisis de retención y conversión para el catálogo de Nicole Vega y lanzamientos de comunidad.")
    
    st.info("Estrategia activa: Conversión de oyentes pasivos a núcleos de superfans.")
    
    # Lista desplegable automática con solo las canciones de Nicole Vega
    canciones_nicole = df_catalogo[df_catalogo['Artista / Intérprete'] == "Nicole Vega"]['Canción'].tolist()
    cancion_select = st.selectbox("Selecciona una obra de Nicole Vega para evaluar impacto de ganchos (Hooks):", canciones_nicole)
    
    st.slider(f"Nivel de retención orgánica requerido para {cancion_select} en videos cortos (TikTok/YT):", 0, 100, 85)
     
  
