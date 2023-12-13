import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import pandas as pd

st.set_page_config(page_title="EJEMPLO CONTROLES",page_icon="❄️",layout="wide")

st.markdown('---')
st.header("INSERTAMOS GRÁFICOS EN STREAMLIT")

#Carga de datos
df_temp = pd.read_excel(r'Temperaturas.xls')

#Definición de objeto de tipo lista "data"
data = [go.Histogram(x=df_temp["T_Promedio"],xbins=dict(start=0,end=40,size=5),histnorm='probability',cumulative_enabled=True)] #cumulative_enabled=True para CDF / nbinsx para especificar número de bins directamente

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="Histograma Temperatura",height=500)

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig1 = go.Figure(data=data, layout=layout)


data = [go.Box(x=df_temp["Ciudad"],y=df_temp["T_Promedio"])] #pointpos=0 para ubicación de los puntos en el centro / boxpoints ="all" si se quieren visualizar todos los puntos

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="Box & whiskers Temperatura",height=500)

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig2 = go.Figure(data=data, layout=layout)


col1,col2 = st.columns(2)

# Plot!
with col1:
    st.plotly_chart(fig1, use_container_width=False)

with col2:
    st.plotly_chart(fig2, use_container_width=False)