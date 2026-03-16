import streamlit as st
import pandas as pd

from database import Load_data

def main():
    dataframe = Load_data(ID_DB="1sGNTms97VI-JV7EqSipsKOoRNIGVGIrhXjQWH010EBM", ID_SHEET="1339436993")
    st.title("dashboard")   
    
    st.dataframe(dataframe) 

    st.text("Valor total de carga: " + str(dataframe["Total NF-e"].sum()))