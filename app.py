import streamlit as st
import pandas as pd
import re

# 1. Configuración de Seguridad y Diseño
st.set_page_config(page_title="DataCleaner Pro", page_icon="🔒")
st.title("🛡️ Limpiador de Datos Automatizado")
st.write("Sube tu archivo, paga y descarga en segundos.")

# 2. Subida de archivo (Cualquiera puede subirlo para probar)
archivo = st.file_uploader("Sube tu Excel o CSV", type=["xlsx", "csv"])

if archivo:
    df = pd.read_excel(archivo) if archivo.name.endswith('xlsx') else pd.read_csv(archivo)
    st.write("✅ Archivo cargado. Vista previa de los primeros 5 datos:")
    st.dataframe(df.head())

    st.divider()

    # 3. EL MURO DE PAGO
    st.subheader("Paso 2: Obtén tu clave de descarga")
    st.write("Para procesar y descargar tu lista completa, realiza el pago de $5 USD.")
    
    # Botón que lleva al cliente a pagar en Stripe (Seguridad Total)
    st.markdown("[👉 CLIC AQUÍ PARA PAGAR $5 USD](https://estilistaintegral.gumroad.com/l/rmxfm)")

    # 4. VALIDACIÓN DE SEGURIDAD
    # Solo después de pagar, el cliente recibe una clave (ejemplo: 'PAGO123')
    clave_cliente = st.text_input("Introduce el Código de Acceso que recibiste en tu correo:")

    if clave_cliente == "PAGO123": # Tú puedes cambiar esta clave cada semana
        st.success("🔓 Acceso concedido")
        
        # Aquí va la lógica de limpieza (lo que hace tu sistema)
        def limpiar(texto):
            return re.sub(r'\D', '', str(texto))

        if st.button("Procesar y Descargar"):
            df.iloc[:, 0] = df.iloc[:, 0].apply(limpiar) # Limpia la primera columna
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Descargar Archivo Final", data=csv, file_name="lista_limpia.csv")
    else:
        if clave_cliente:

            st.error("❌ Código incorrecto o expirado.")
