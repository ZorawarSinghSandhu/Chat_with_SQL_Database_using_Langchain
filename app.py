import streamlit as st
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Langchain: Chat with SQL Database")
st.title("Langchain: Chat with SQL Database")

MYSQL = "USE_MYSQL"
LOCALDB = "USE_LOCALDB"

radio_opt = ["Chat with SQLite3 Database - Student.db", "Chat with SQL Database"]

chosen_opt = st.sidebar.radio(label="Choose which database you want to chat with:", options=radio_opt)

if radio_opt.index(chosen_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Enter MySQL Host")
    mysql_username = st.sidebar.text_input("Enter MySQL Username")
    mysql_password = st.sidebar.text_input("Enter MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("Enter MySQL Database")
    
else:
    db_uri = LOCALDB
    
    
api_key = st.sidebar.text_input("Enter Groq API Key")

if not api_key:
    st.info("Please enter the Groq API Key")
    
if not db_uri:
    st.info("Please enter the Database Information")
    
