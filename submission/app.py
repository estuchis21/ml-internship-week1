import streamlit as st

st.set_page_config(page_title="FlyRank ML Internship - Capstone Research Paper", layout="wide")

st.title("FlyRank ML Internship - Capstone Research Paper")

st.header("Abstract")
st.markdown("""
How can we accurately predict search content refresh priority using production scale metrics? We formulated this as a binary classification task leveraging a gradient boosting framework trained on behavioral engagement and ranking signals. Using strict temporal validation splits to prevent leakage, our model outperformed the baseline significantly. Specifically, the final model achieved superior ROC-AUC metrics compared to the heuristic baseline. These findings provide scalable, data-driven prioritization for content optimization pipelines.
""")

st.markdown("---")

st.header("1. Introduction / Problem Statement")
st.markdown("""
Definición del desafío empresarial y de ingeniería: optimizar los flujos de trabajo de actualización de contenido de búsqueda en ecosistemas web a gran escala utilizando datos reales de producción.
""")

st.markdown("---")

st.header("2. Data & Methodology")
st.markdown("""
* **Datos:** Versión de la versión utilizada, tablas empleadas, ventanas de fechas exactas y criterios de exclusión de datos seguros para el público.
* **Metodología:** Supuestos fundamentales del modelo, tubería de ingeniería de características, definición clara de etiquetas, especificación del modelo base, diseño de validación robusto y verificaciones de fugas de datos.
""")

st.markdown("---")

st.header("3. Results & Recommendations")
st.markdown("""
* **Resultados:** Comparativa directa entre el modelo y la línea base en la misma división de validación, respaldada por gráficos integrados (importancia de características, curvas ROC/AUC, distribuciones de puntajes).
* **Recomendaciones:** Plan de acción y propuesta de valor para los equipos de ingeniería y SEO basados en los conocimientos del modelo.
""")

st.markdown("---")
st.markdown("**(C) 2026 - Built on the FlyRank ML Internship dataset** [flyrank.ai](https://flyrank.ai)")