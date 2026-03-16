import streamlit as st
import pandas as pd

from database import Load_data

def main():
    dataframe = Load_data(ID_DB="1sGNTms97VI-JV7EqSipsKOoRNIGVGIrhXjQWH010EBM", ID_SHEET="1339436993")
    
    st.set_page_config(page_title="Dashboard de Carga", page_icon="📊", layout="wide")
    st.title("dashboard")   
    
    # Indices
    st.metric(label="Qtd coletas", value=str(len(dataframe[dataframe['Tipo'] == "Coleta"])))
    
    st.metric(label="Qtd entregas", value=str(len(dataframe[dataframe['Tipo'] == "Entrega"])))
    
    
    #frame
    st.dataframe(dataframe) 

    st.text("Valor total de carga: " + str(dataframe["Total NF-e"].sum()))
    
    
if __name__ == "__main__":    main()