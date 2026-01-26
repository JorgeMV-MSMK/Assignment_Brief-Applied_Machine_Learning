import streamlit as st
import pandas as pd
import joblib
# Importamos CatBoostClassifier para que joblib reconozca la clase al cargar el modelo
from catboost import CatBoostClassifier 

# ----------------------------------------------------------------------------------
# 1. CARGA DE MODELO Y PREPROCESADOR
# ----------------------------------------------------------------------------------
try:
    # Asegúrate de que estos archivos estén en la misma carpeta o subidos al repo
    modelo = joblib.load('modelo_catboost.pkl')
    preprocessor = joblib.load('preprocesador.pkl')
except FileNotFoundError:
    st.error("⚠️ Error Crítico: No se encuentran los archivos .pkl. Asegúrate de haberlos generado en el notebook y subido al directorio.")
    st.stop()

# ----------------------------------------------------------------------------------
# 2. LISTAS DE OPCIONES (DATASET EXACTO)
# ----------------------------------------------------------------------------------

OPCIONES_TRABAJO = [
    'Data Scientist', 
    'Network Engineer', 
    'OSINT Investigator', 
    'Penetration Tester', 
    'Security Analyst', 
    'Software Engineer'
]

# Lista exacta extraída de tu dataset para evitar errores de "categoría desconocida"
OPCIONES_PAIS = [
    'Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 
    'Antarctica (the territory South of 60 deg S)', 'Antigua and Barbuda', 'Argentina', 'Armenia', 
    'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 
    'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 
    'Botswana', 'Bouvet Island (Bouvetoya)', 'Brazil', 'British Indian Ocean Territory (Chagos Archipelago)', 
    'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 
    'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 
    'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 
    'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 
    'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 
    'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 
    'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 
    'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 
    'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 
    'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 
    'Kazakhstan', 'Kenya', 'Kiribati', 'Korea', 'Kuwait', 'Kyrgyz Republic', "Lao People's Democratic Republic", 
    'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania', 
    'Luxembourg', 'Macao', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 
    'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 
    'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 
    'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 
    'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 
    'Oman', 'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 
    'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 
    'Russian Federation', 'Rwanda', 'Saint Barthelemy', 'Saint Helena', 'Saint Kitts and Nevis', 
    'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 
    'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 
    'Sierra Leone', 'Singapore', 'Slovakia (Slovak Republic)', 'Slovenia', 'Solomon Islands', 'Somalia', 
    'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 
    'Svalbard & Jan Mayen Islands', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan', 
    'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 
    'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 
    'United Arab Emirates', 'United Kingdom', 'United States Minor Outlying Islands', 
    'United States Virgin Islands', 'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu', 
    'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe'
]

# ----------------------------------------------------------------------------------
# 3. FUNCIONES AUXILIARES
# ----------------------------------------------------------------------------------

def fuerza_contrasena(password):
    """Calcula una fortaleza simple basada en la longitud y contenido."""
    if not password:
        return "Weak"
    if len(password) < 8:
        return "Weak"
    elif any(char.isdigit() for char in password):
        return "Moderate"
    else:
        return "Strong"

# ----------------------------------------------------------------------------------
# 4. INTERFAZ DE USUARIO (STREAMLIT)
# ----------------------------------------------------------------------------------

st.set_page_config(page_title="Detector de Brechas OSINT", page_icon="🕵️‍♂️")

st.title("🕵️‍♂️ OSINT: Detector de Brechas de Seguridad")
st.markdown("""
Esta herramienta utiliza un modelo de IA (entrenado con datos históricos de filtraciones) 
para predecir la probabilidad de que un perfil haya sido comprometido.
""")

st.write("---")

col1, col2 = st.columns(2)

with col1:
    # Input 1: Trabajo (Selectbox para evitar errores)
    trabajo = st.selectbox("Selecciona tu Cargo Laboral", OPCIONES_TRABAJO)
    
    # Input 2: País (Selectbox con tu lista limpia)
    # Seleccionamos 'Spain' por defecto si está en la lista (índice 204 aprox), si no, el primero
    index_spain = OPCIONES_PAIS.index('Spain') if 'Spain' in OPCIONES_PAIS else 0
    pais = st.selectbox("Selecciona tu País", OPCIONES_PAIS, index=index_spain)

with col2:
    # Input 3: Contraseña (Simulada)
    contrasena = st.text_input(
        "Contraseña (Simulada)", 
        type="password", 
        help="Introduce una contraseña ficticia con la misma estructura (longitud, números) que la real."
    )
    
    # Input 4: Pastebin
    pastebin = st.selectbox("¿Tu correo aparece en Pastebin público?", ["Yes", "No"])

st.write("---")

# ----------------------------------------------------------------------------------
# 5. LÓGICA DE PREDICCIÓN
# ----------------------------------------------------------------------------------

if st.button("Calcular Riesgo 🚀", type="primary"):
    
    # 1. Calcular fuerza de contraseña interna
    fuerza = fuerza_contrasena(contrasena)
    
    # 2. Crear DataFrame con los nombres EXACTOS que espera el modelo
    # 'Country' es ahora la columna clave gracias a tu limpieza en el notebook
    input_data = pd.DataFrame([{
        "Job_Title": trabajo,
        "Password_Strength": fuerza,
        "Public_Pastebin": pastebin,
        "Country": pais  
    }])
    
    try:
        # 3. Transformar datos (OneHotEncoder)
        datos_procesados = preprocessor.transform(input_data)
        
        # 4. Predecir
        # predict_proba devuelve [prob_clase_0, prob_clase_1]. Queremos la clase 1 (Breached)
        probabilidad = modelo.predict_proba(datos_procesados)[0][1]
        porcentaje = round(probabilidad * 100, 2)
        
        # 5. Mostrar Resultados
        st.subheader(f"Probabilidad de Brecha: {porcentaje}%")
        st.progress(int(porcentaje))
        
        if probabilidad < 0.45:
            st.success("✅ **BAJO RIESGO**: Según los patrones de IA, tu perfil parece seguro.")
        elif probabilidad < 0.55:
            st.warning("⚠️ **RIESGO MEDIO**: Se detectan ciertos factores de vulnerabilidad.")
        else:
            st.error("🚨 **ALTO RIESGO**: Es muy probable que tus datos estén expuestos (o lo estén pronto).")
            
            # Mensaje extra si el riesgo es alto por Pastebin
            if pastebin == "Yes":
                st.info("💡 Consejo: Aparecer en Pastebin es el factor de riesgo más alto. Cambia tus credenciales inmediatamente.")

    except Exception as e:
        st.error(f"Ocurrió un error al procesar la predicción: {e}")
        st.write("Detalles del error para depuración:", e)