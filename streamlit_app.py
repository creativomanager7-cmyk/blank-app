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

# Base de datos real extraída de Muso.AI
composiciones_data = {
    "Canción": [
        "Mi Debilidad", "¿Dónde Estabas Tú?", "Piedra, Papel o Tijera", 
        "Si me ven llorando - En Vivo", "Ojalá", "Vente Conmigo", 
        "De 5 en 5", "Me Vale Madre", "Golpe Avisa", 
        "Bolsita de Marca", "Insomnios", "Malditona"
    ],
    "Artista / Intérprete": [
        "Francy", "Paola Jara", "Dayanara, Pipe Bueno", 
        "Jessi Uribe", "Joaquin Guiller", "Noche de Brujas, Jorge Celedón", 
        "Nicole Vega", "Nicole Vega", "Nicole Vega", 
        "Nicole Vega", "Nicole Vega", "Nicole Vega"
    ],
    "Rol Registrado": [
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist", 
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist",
        "Composer / Lyricist", "Composer / Lyricist", "Composer / Lyricist"
    ],
    "Estatus IP (Sony Pubcol)": [
        "99.1% Aligned", "98.4% Aligned", "100% Aligned", 
        "97.8% Aligned", "96.5% Aligned", "99.0% Aligned",
        "100% Aligned", "100% Aligned", "100% Aligned",
        "100% Aligned", "100% Aligned", "100% Aligned"
    ]
}
df_catalogo = pd.DataFrame(composiciones_data)

with tab1:
    st.subheader("Auditoría Automatizada de Catálogo Real")
    st.write("Filtra y audita la indexación global de tus obras directamente desde el panel.")
    
    # Buscador Interactivo
    buscar_obra = st.text_input("Buscar canción o artista en tu catálogo de propiedad intelectual:", "")
    
    if buscar_obra:
        resultado = df_catalogo[
            df_catalogo['Canción'].str.contains(buscar_obra, case=False) | 
            df_catalogo['Artista / Intérprete'].str.contains(buscar_obra, case=False)
        ]
        st.write("Resultados encontrados:")
        st.dataframe(resultado, use_container_width=True)
    else:
        st.write("Catálogo General Indexado:")
        st.dataframe(df_catalogo, use_container_width=True)
        
    st.markdown("### 📊 Métricas Agregadas de Regalías e IP")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="Total Obras Registradas en Panel", value=f"{len(df_catalogo)} Tracks")
    with c2:
        st.metric(label="Alineación Promedio de Metadatos", value="99.2%")
    with c3:
        st.metric(label="Editorial Principal Vinculada", value="Sony Music Publishing")

with tab2:
    st.subheader("Laboratorio de Algoritmos: Incubadora de Superfans")
    st.write("Análisis de retención y conversión para el catálogo de Nicole Vega y lanzamientos de comunidad.")
    
    st.info("Estrategia activa: Conversión de oyentes pasivos a núcleos de superfans.")
    cancion_select = st.selectbox("Selecciona una obra para evaluar impacto de ganchos:", ["De 5 en 5", "Me Vale Madre", "Golpe Avisa"])
    
    st.slider(f"Nivel de retención orgánica requerido para {cancion_select} (Hooks cortos):", 0, 100, 80)
 
