import streamlit as st
import dropbox

st.set_page_config(page_title="Revisión de OT", page_icon="📂")

st.title("🔍 Revisión de OT")
st.write("Busca archivos relacionados con órdenes de trabajo en Dropbox")

ACCESS_TOKEN = st.secrets["dropbox"]["access_token"]
dbx = dropbox.Dropbox(ACCESS_TOKEN)

consulta = st.text_input("🔎 Ingrese parte del nombre del archivo:")

if st.button("Buscar"):
    if not consulta.strip():
        st.warning("Por favor ingrese un texto para buscar.")
    else:
        try:
            resultados = dbx.files_search_v2(query=consulta)
            if not resultados.matches:
                st.info("No se encontraron archivos.")
            else:
                st.success(f"{len(resultados.matches)} archivo(s) encontrados:")
                for match in resultados.matches:
                    archivo = match.metadata.get_metadata()
                    st.write(f"📄 {archivo.name}")
                    st.code(archivo.path_display)
        except Exception as e:
            st.error(f"Error: {e}")