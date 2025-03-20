import streamlit as st
import pandas as pd
import SQLAlchemy as sa

st.title("Data Logging Test App")

###################################################

server = st.secrets["dolphin_edu"]["server"]
database = st.secrets["dolphin_edu"]["database"]
username = st.secrets["dolphin_edu"]["username"]
password = st.secrets["dolphin_edu"]["password"]

# Create the connection URL
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Create the SQLAlchemy engine
engine = sa.create_engine(conn_str)

# SQL query
query = "SELECT TOP 10 * FROM [log].[openai_api_call];"

# Read SQL query into Pandas DataFrame using SQLAlchemy
df = pd.read_sql(query, con=engine)

# Zahodit Primary Key, který se definuje v databázi
df.drop(columns=["call_open_api_id"], inplace=True)

# Vytvoření prázdné kopie pro zápis
df2 = df.iloc[0:0].copy()


st.dataframe(df2)
