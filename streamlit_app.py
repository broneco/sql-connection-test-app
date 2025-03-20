import streamlit as st
import pandas as pd

st.title("Data Logging Test App")

###################################################

server = st.secrets["dolphin_edu"]["server"]
database = st.secrets["dolphin_edu"]["database"]
username = st.secrets["dolphin_edu"]["username"]
password = st.secrets["dolphin_edu"]["password"]

conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection(conn_str, type='sql')

# Query and display the data you inserted
API_usage_info = conn.query('SELECT TOP 10 * FROM [log].[openai_api_call]')
st.dataframe(API_usage_info)